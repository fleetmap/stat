package ru.fleetmap.core;

import com.fasterxml.jackson.annotation.JsonIgnore;

/**
 * Created by debalid on 20.05.2016.
 */
public class District {
    private String title;
    private String weekDay;
    private Integer hour;
    private Double Number;
    private Integer count;

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Double getNumber() {
        return Number;
    }

    public void setNumber(Double number) {
        Number = number;
    }

    public Integer getHour() {
        return hour;
    }

    public void setHour(Integer hour) {
        this.hour = hour;
    }

    public String getWeekDay() {
        return weekDay;
    }

    public void setWeekDay(String weekDay) {
        this.weekDay = weekDay;
    }

    public Integer getCount() {
        return count;
    }

    public void setCount(Integer count) {
        this.count = count;
    }
}
