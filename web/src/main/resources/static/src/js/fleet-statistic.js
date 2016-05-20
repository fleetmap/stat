/**
 * Created by vlad on 20.05.16.
 */
var React = require('react');
var Map = require('./components/map');
var Slider = require('./components/slider');

var FleetStatistic = React.createClass({
        render: function () {
            return (
                <div className="application">
                    <Slider/>
                    <Map/>
                </div>
            )

        }
    }
);

module.exports = FleetStatistic;