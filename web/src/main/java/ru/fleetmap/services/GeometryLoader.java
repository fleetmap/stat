package ru.fleetmap.services;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.context.annotation.ComponentScan;
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
                Charset.forName("cp1251"))) {
            records = CSVFormat.DEFAULT
                    .withDelimiter(';')
                    .withHeader("MO_Name", "Weekday", "Hour", "Number")
                    .parse(csvReader);

            // пропускаем первую запись с загоолвками
            Iterator<CSVRecord> iterator = records.iterator();
            iterator.next();

            DecimalFormat decimalFormat = new DecimalFormat("#.#");

            List<District> districts = new ArrayList<District>();
            iterator.forEachRemaining(x -> {
                District district = new District();
                district.setTitle(x.get("MO_Name"));
                try {
                    district.setHour(decimalFormat.parse(x.get("Hour")).doubleValue());
                    district.setNumber(decimalFormat.parse(x.get("Number")).doubleValue());
                } catch (ParseException e) {
                    e.printStackTrace();
                    throw new RuntimeException("Cannot parse double in " + x.toString());
                }
                district.setWeekDay(x.get("Weekday"));
                districts.add(district);
            });
            return districts;
        }
    }

    public void setSampleDataCsvDestination(String sampleDataCsvDestination) {
        this.sampleDataCsvDestination = sampleDataCsvDestination;
    }

    public void setCarsharingMapJsonDestination(String carsharingMapJsonDestination) {
        this.carsharingMapJsonDestination = carsharingMapJsonDestination;
    }
}
