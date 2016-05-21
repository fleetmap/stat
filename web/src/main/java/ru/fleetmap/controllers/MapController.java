package ru.fleetmap.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.support.PagedListHolder;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.fleetmap.core.District;
import ru.fleetmap.core.Geometry;
import ru.fleetmap.core.GeometryFilter;
import ru.fleetmap.repo.GeometryRepository;
import ru.fleetmap.services.GeometryLoader;

import java.io.IOException;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Created by debalid on 20.05.2016.
 */
@RestController
@RequestMapping("/api")
public class MapController {
    @Autowired
    private GeometryLoader geometryLoader;

    @Autowired
    private GeometryRepository geometryRepository;

    @RequestMapping("/test")
    public Geometry test() throws IOException {
        return geometryLoader.load();
    }

    @RequestMapping("/find")
    public Geometry find(GeometryFilter filter) throws IOException {
        return geometryRepository.findGeometryByFilter(filter);
    }

    @RequestMapping("/week_history")
    public List<Integer> weekHistory (String name) throws IOException {
        GeometryFilter filter = new GeometryFilter();
        filter.setTitle(name);
        Geometry geometry = geometryRepository.findGeometryByFilter(filter);
        List<Integer> history = geometry.features.parallelStream()
                .map(feature -> feature.properties.timeline)
                .findFirst()
                .map(districts -> districts.stream()
                        //.sorted((x, y) -> 31 * (day(x.getWeekDay()) - day(y.getWeekDay() + (x.getHour() - y.getHour()))))
                        .sorted(Comparator.comparing(x -> 24 * day(x.getWeekDay()) + x.getHour()))
                        .map(x -> x.getCount()/10)
                        .collect(Collectors.toList()))
                .orElseGet(Collections::emptyList);
        return history;
    }

    //костыль
    @RequestMapping("/max")
    public double max() throws IOException {
        double max = 0;
        for (Geometry.Feature f : geometryLoader.load().features) {
            for (District d : f.properties.timeline) {
                if (d.getNumber() > max) max = d.getNumber();
            }
        }
        return max;
    }

    private int day(String pt) {
        switch (pt.toLowerCase()) {
            case "пн":
                return 0;
            case "вт":
                return 1;
            case "ср":
                return 2;
            case "чт":
                return 3;
            case "пт":
                return 4;
            case "сб":
                return 5;
            case "вс":
                return 6;
            default: return 0;
        }
    }
}