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
    public List<Double> weekHistory (String name) throws IOException {
        GeometryFilter filter = new GeometryFilter();
        filter.setTitle(name);
        Geometry geometry = geometryRepository.findGeometryByFilter(filter);
        List<Double> history = geometry.features.parallelStream()
                .map(feature -> feature.properties.timeline)
                .findFirst()
                .map(districts -> districts.stream().map(District::getNumber).collect(Collectors.toList()))
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
}