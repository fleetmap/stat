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
                center: [51.505, -0.09],
                zoom: 13
            });
            L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(this.map);

        }
    }
);


module.exports = Map;