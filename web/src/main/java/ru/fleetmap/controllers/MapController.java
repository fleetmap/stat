package ru.fleetmap.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.fleetmap.core.District;
import ru.fleetmap.services.GeometryLoader;

import java.io.IOException;
import java.util.List;

/**
 * Created by debalid on 20.05.2016.
 */
@RestController
@RequestMapping("/api")
public class MapController {
    @Autowired
    private GeometryLoader geometryLoader;

    @RequestMapping("/test")
    public List<District> test() throws IOException {
        return geometryLoader.load();
    }

    public void setGeometryLoader(GeometryLoader geometryLoader) {
        this.geometryLoader = geometryLoader;
    }
}