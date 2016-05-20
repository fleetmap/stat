/**
 * Created by vlad on 21.05.16.
 */
var React = require('react');
var RCSlider = require('rc-slider');

const marks = {
    0: '0:00',
    3: '3:00',
    6: '6:00',
    9: '9:00',
    12: '12:00',
    15: '15:00',
    18: '18:00',
    21: '21:00',
    24: '24:00'
};

var Slider = React.createClass({


    render:function () {

        return(
            <div id="slider">
                <div className="days">
                    <a href="" id="mon">ПН</a>
                    <a href="" id="tue">ВТ</a>
                    <a href="" id="wen">СР</a>
                    <a href="" id="thu">ЧТ</a>
                    <a href="" id="fri">ПТ</a>
                    <a href="" id="sat">СБ</a>
                    <a href="" id="sun">ВС</a>
                </div>
                <div className="input">
                    <RCSlider min={0} max={24} defaultValue={12} marks={marks}/>
                </div>

            </div>
        )
    }
});
module.exports = Slider;