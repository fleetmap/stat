package ru.fleetmap.core;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;
import java.util.List;

/**
 * Created by debalid on 21.05.2016.
 */
public class Geometry implements Serializable {
    @JsonProperty("features")
    public List<Feature> features;
    @JsonProperty("type")
    public String type;

    public static class Feature {
        @JsonProperty("properties")
        public Properties properties;
        @JsonProperty("geometry")
        public Polygon polygon;
        @JsonProperty("type")
        public String type;

        public static class Properties {
            @JsonProperty("NAME")
            public String name;

            @JsonProperty("timeLine")
            public List<District> timeline;
        }

        public static class Polygon {
            @JsonProperty("type")
            public String type;
            @JsonProperty("coordinates")
            public List<List<List<Double>>> coordinates;
        }
    }
}
