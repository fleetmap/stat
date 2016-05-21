/**
 * Created by vlad on 20.05.16.
 */
var React = require('react');
var Map = require('./components/map');


var FleetStatistic = React.createClass({
        render: function () {
            return (
                    <Map/>
            )

        }
    }
);

module.exports = FleetStatistic;