/**
 * Created by vlad on 20.05.16.
 */
var React = require('react');
var L = require('leaflet');
var Map = React.createClass({
        map: null,
        render: function () {
            return (
                <div id="map"></div>
            )
        },
        componentDidMount: function () {
            this.map = L.map('map', {
                center: [55.75, 37.61],
                zoom: 13
            });
            L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(this.map);
        },

        changeShapshot: function (map, hour, weekDay) {
            var xmlhttp = new XMLHttpRequest();
            var url = "/api/find?hour=" + hour + "&weekDay=" + weekDay;

            xmlhttp.onreadystatechange = function () {
                console.log('ready');
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                    var obj = JSON.parse(xmlhttp.responseText);

                    function pickHex(color1, color2, weight) {
                        var p = weight;
                        var w = p * 2 - 1;
                        var w1 = (w / 1 + 1) / 2;
                        var w2 = 1 - w1;
                        var rgb = [Math.round(color1[0] * w1 + color2[0] * w2),
                            Math.round(color1[1] * w1 + color2[1] * w2),
                            Math.round(color1[2] * w1 + color2[2] * w2)];
                        return rgb;
                    }

                    L.geoJson(obj, {
                        style: function (feature) {
                            var color = pickHex([255, 0, 0], [0, 255, 0], feature.properties.timeLine[0].number / 6.0); //magic
                            return {
                                color: "rgb(" + color[0] + "," + color[1] + "," + color[2] + ")"
                            }
                        }
                    }).addTo(map);
                }
            };
            xmlhttp.open("GET", url, true);
            xmlhttp.send();
        }
    }
);


module.exports = Map;