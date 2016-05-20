package ru.fleetmap.repo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import ru.fleetmap.core.Geometry;
import ru.fleetmap.core.GeometryFilter;
import ru.fleetmap.services.GeometryLoader;

import java.io.IOException;

/**
 * Created by debalid on 21.05.2016.
 */
@Component
public class GeometryRepository {
    @Autowired
    private GeometryLoader geometryLoader;

    public Geometry findGeometryByFilter(GeometryFilter filter) throws IOException {
        Geometry geometry = geometryLoader.load();
        if (filter.getTitle() != null) {
            geometry.features
                    .removeIf(x -> !x.properties.name.toLowerCase().equals(filter.getTitle().toLowerCase()));
        }

        if (filter.getHour() != null) {
            geometry.features.forEach(x -> {
                x.properties.timeline.removeIf(d -> !d.getHour().equals(filter.getHour()));
            });
        }

        if (filter.getWeekDay() != null) {
            geometry.features.forEach(x -> {
                x.properties.timeline.removeIf(d -> !d.getWeekDay().toLowerCase().equals(filter.getWeekDay().toLowerCase()));
            });
        }

        geometry.features
                .removeIf(x -> x.properties.timeline.isEmpty());

        return geometry;
    }
}
