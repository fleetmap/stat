package ru.fleetmap.services;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;
import ru.fleetmap.core.District;

import java.io.*;
import java.nio.charset.Charset;
import java.text.DecimalFormat;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Created by debalid on 20.05.2016.
 */
@Service
public class GeometryLoader {
    public static final String CSV_ENCODING = "cp1251";
    public static final String HEADER_NAME = "MO_Name";
    public static final String HEADER_WEEKDAY = "Weekday";
    public static final String HEADER_HOUR = "Hour";
    public static final String HEADER_NUMBER = "Number";

    @Value("${core.sampleDataResultCsv}")
    private String sampleDataCsvDestination;

    @Value("${core.carsharingMapJson}")
    private String carsharingMapJsonDestination;

    @Cacheable("districts")
    public List<District> load() throws IOException {
        List<District> districts = loadCsv();
        return districts;
    }

    private List<District> loadCsv() throws IOException {
        Iterable<CSVRecord> records;
        try (Reader csvReader = new InputStreamReader(new FileInputStream(sampleDataCsvDestination),
                Charset.forName(CSV_ENCODING))) {
            records = CSVFormat.DEFAULT
                    .withDelimiter(';')
                    .withHeader(HEADER_NAME, HEADER_WEEKDAY, HEADER_HOUR, HEADER_NUMBER)
                    .parse(csvReader);

            // пропускаем первую запись с загоолвками
            Iterator<CSVRecord> iterator = records.iterator();
            iterator.next();

            DecimalFormat decimalFormat = new DecimalFormat("#.#");

            List<District> districts = new ArrayList<District>();
            iterator.forEachRemaining(x -> {
                District district = new District();
                district.setTitle(x.get(HEADER_NAME));
                try {
                    district.setHour(decimalFormat.parse(x.get(HEADER_HOUR)).doubleValue());
                    district.setNumber(decimalFormat.parse(x.get(HEADER_HOUR)).doubleValue());
                } catch (ParseException e) {
                    e.printStackTrace();
                    throw new RuntimeException("Cannot parse double in " + x.toString());
                }
                district.setWeekDay(x.get(HEADER_WEEKDAY));
                districts.add(district);
            });
            return districts;
        }
    }

    private List<District> setGeometry(List<District> loaded) {
        JSON
    }

    public void setSampleDataCsvDestination(String sampleDataCsvDestination) {
        this.sampleDataCsvDestination = sampleDataCsvDestination;
    }

    public void setCarsharingMapJsonDestination(String carsharingMapJsonDestination) {
        this.carsharingMapJsonDestination = carsharingMapJsonDestination;
    }
}
