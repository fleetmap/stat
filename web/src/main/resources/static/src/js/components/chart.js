/**
 * Created by debalid on 21.05.2016.
 */
var Chart = require('chart.js');
var L = require('leaflet');

// watch css!
var chartWidth = 400;
var chartHeight = 300;

var loadHistory = function(districtName, id) {
    var xmlhttp = new XMLHttpRequest();
    var url = "/api/week_history?name=" + districtName;

    xmlhttp.onreadystatechange = function () {
        console.log('ready');
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var arr = JSON.parse(xmlhttp.responseText);
            //console.log('chart', arr);
            //popup.id - div id for chart
            lineChart(arr, id);
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
};

var bindPopUp = function (feature, layer) {
    var id = generateUUID();
    layer.bindPopup(buildPopUp(feature, id,
        "<div id='d"+ id + "' style='min-height: " + chartHeight + "'>" +
        "<canvas id='c" + id +"' width='" + chartWidth+ "' height='" + chartHeight + "'></canvas>" +
        "</div>"
    ));
};

var onPopUpOpen = function (event) {
    var popup = event.popup;
    loadHistory(popup.feature.properties.NAME, popup.id);
};

var buildPopUp = function(feature, id, content) {
    var p = L.popup({
        minWidth: chartWidth,
        minHeight: chartHeight,
        zIndex: 1000000 //because
    });
    p.setContent(content);
    p.feature = feature;
    p.id = id;
    return p;
};

function generateUUID() {
    var d = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
}

var lineChart = function(array, id) {//7 * 24 points
    var ctx = document.getElementById('c' + id).getContext("2d");
    var data = {
        labels: ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
        datasets: [
            {
                // очень много опций доступно
                label: "История",
                data: array
            }
        ]
    };
    var line = new Chart(ctx, {
        type: 'line',
        data: data
    });
};

module.exports = {
    loadHistory,
    bindPopUp,
    onPopUpOpen
};