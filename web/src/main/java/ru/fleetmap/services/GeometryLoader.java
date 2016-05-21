package ru.fleetmap.services;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;
import ru.fleetmap.core.District;
import ru.fleetmap.core.Geometry;

import java.io.*;
import java.nio.charset.Charset;
import java.text.DecimalFormat;
import java.text.ParseException;
import java.util.*;
import java.util.stream.Collectors;

import static com.fasterxml.jackson.databind.DeserializationFeature.*;

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
    public static final String HEADER_PROVIDER = "Provider";
    public static final String HEADER_COUNT = "Count";

    @Value("${core.sampleDataResultCsv}")
    private String sampleDataCsvDestination;

    @Value("${core.carsharingMapJson}")
    private String carsharingMapJsonDestination;

    @Cacheable("geometry")
    public Geometry load() throws IOException {
        List<District> districts = loadCsv();
        return loadGeometry(districts);
    }

    private List<District> loadCsv() throws IOException {
        Iterable<CSVRecord> records;
        try (Reader csvReader = new InputStreamReader(GeometryLoader.class.getResourceAsStream(sampleDataCsvDestination),
                Charset.forName(CSV_ENCODING))) {

            records = CSVFormat.DEFAULT
                    .withDelimiter(';')
                    .withHeader(HEADER_NAME, HEADER_WEEKDAY, HEADER_HOUR, HEADER_NUMBER, HEADER_COUNT)
                    .parse(csvReader);

            // пропускаем первую запись с загоолвками
            Iterator<CSVRecord> iterator = records.iterator();
            iterator.next();

            DecimalFormat decimalFormat = new DecimalFormat("#.#");

            List<District> districts = new ArrayList<>();
            iterator.forEachRemaining(x -> {
                District district = new District();
                district.setTitle(x.get(HEADER_NAME));
                try {
                    district.setHour(decimalFormat.parse(x.get(HEADER_HOUR)).intValue());
                    district.setNumber(Double.parseDouble(x.get(HEADER_NUMBER)));
                    district.setWeekDay(x.get(HEADER_WEEKDAY));
                    district.setCount(decimalFormat.parse(x.get(HEADER_COUNT)).intValue());
                } catch (ParseException e) {
                    e.printStackTrace();
                    throw new RuntimeException("Cannot parse double in " + x.toString());
                }
                districts.add(district);
            });

            return districts;
        }
    }

    private Geometry loadGeometry(List<District> loadedDistricts) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        Geometry geometry = mapper
                .configure(FAIL_ON_UNKNOWN_PROPERTIES, false)
                .readValue(GeometryLoader.class.getResourceAsStream(carsharingMapJsonDestination), Geometry.class);

        geometry.features.forEach(x -> {
            x.properties.timeline = loadedDistricts.parallelStream() // медленно!
                    .filter(y -> y.getTitle().toLowerCase().equals(x.properties.name.toLowerCase()))
                    .collect(Collectors.toList());
        });
        return geometry;
    }

    public void setSampleDataCsvDestination(String sampleDataCsvDestination) {
        this.sampleDataCsvDestination = sampleDataCsvDestination;
    }

    public void setCarsharingMapJsonDestination(String carsharingMapJsonDestination) {
        this.carsharingMapJsonDestination = carsharingMapJsonDestination;
    }
}
