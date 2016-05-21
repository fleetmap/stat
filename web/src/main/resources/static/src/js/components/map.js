/**
 * Created by vlad on 20.05.16.
 */
var React = require('react');
var L = require('leaflet');
var chart = require('./chart');
var Map = React.createClass({

        getInitialState: function () {
            return ({show: false, time: 12, day: 'ПН', active: null})
        },
        map: null,
        mouseDown: function () {
            this.setState({show: true});
        },
        mouseUp: function () {
            this.setState({show: false});
        },
        onChange: function () {
            this.setState({time: document.getElementById('inputRange').value});
            clearTimeout(this.timer);
            this.timer = setTimeout(() => this.changeShapshot(this.map, this.state.time, this.state.day), 1000);
        },
        dayHandler: function (day, id) {
            return ()=> {
                var elem = document.getElementById(this.state.active);
                if (elem !== undefined && elem != null) {
                    elem.style.color = 'black';
                }
                this.setState({day: day, active: id});
                document.getElementById(id).style.color = 'red';
                clearTimeout(this.timer);
                this.timer = setTimeout(this.changeShapshot(this.map, this.state.time, this.state.day), 1000);
            }
        },
        changeShapshot: function (map, hour, weekDay) {
            if (hour == 24) hour = 0;
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

                    if (this.state.layer != null)
                        this.map.removeLayer(this.state.layer);
                    var layer = L.geoJson(obj, {
                        style: function (feature) {
                            var color = pickHex([0, 255, 0], [255, 0, 0], feature.properties.timeLine[0].number); //magic
                            return {
                                fillColor: "rgb(" + color[0] + "," + color[1] + "," + color[2] + ")",
                                color: 'black',
                                weight: 1,
                                fillOpacity: 0.65
                            }
                        },
                        onEachFeature: chart.bindPopUp
                    });
                    layer.addTo(map);
                    this.setState({layer: layer});

                }
            }.bind(this);
            xmlhttp.open("GET", url, true);
            xmlhttp.send();
        },
        render: function () {
            return (
                <div className="application">
                    <div id="slider">
                        <div className="days">
                            <a id="mon" onClick={this.dayHandler('ПН', 'mon')}>ПН</a>
                            <a id="tue" onClick={this.dayHandler('ВТ', 'tue')}>ВТ</a>
                            <a id="wen" onClick={this.dayHandler('СР', 'wen')}>СР</a>
                            <a id="thu" onClick={this.dayHandler('ЧТ', 'thu')}>ЧТ</a>
                            <a id="fri" onClick={this.dayHandler('ПТ', 'fri')}>ПТ</a>
                            <a id="sat" onClick={this.dayHandler('СБ', 'sat')}>СБ</a>
                            <a id="sun" onClick={this.dayHandler('ВС', 'sun')}>ВС</a>
                        </div>
                        <div className="input">
                            <span>0:00</span>
                            <input id="inputRange" type="range" min="0" max="24" step="1" onMouseDown={this.mouseDown}
                                   onMouseUp={this.mouseUp}
                                   onChange={this.onChange}/>
                            <span>23:59</span>

                        </div>
                        <div className="time">{this.state.time}:00</div>

                    </div>
                    <div id="map"></div>
                </div>

            )
        }
        ,
        componentDidMount: function () {
            this.map = L.map('map', {
                center: [55.75, 37.61],
                zoom: 13
            });
            this.map.on('popupopen', chart.onPopUpOpen);
            L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(this.map);
        }
    }
    )
    ;


module.exports = Map;