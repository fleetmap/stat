package ru.fleetmap;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import ru.fleetmap.services.GeometryLoader;

import javax.xml.stream.events.StartDocument;
import java.io.IOException;

@SpringBootApplication
public class StatApplication {
	@Autowired
	private GeometryLoader geometryLoader;

	public static void main(String[] args) throws IOException {
		SpringApplication.run(StatApplication.class, args);
		//(new StatApplication()).geometryLoader.load();
	}
}
