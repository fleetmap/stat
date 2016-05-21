/**
 * Created by vlad on 21.05.16.
 */
var React = require('react');


var Slider = React.createClass({
    getInitialState: function () {
        return ({show: false, time: 12, day: 'ПН'})
    },

    mouseDown: function () {
        this.setState({show: true});
    },
    mouseUp: function () {
        this.setState({show: false});
    },
    onChange: function () {
        this.setState({time: document.getElementById('inputRange').value})
    },
    dayHandler: function (day) {
      return()=> {
          this.setState({day: day});
          console.log(this.state);
      }
    },

    render: function () {

        return (
            <div id="slider">
                <div className="days">
                    <a onClick={this.dayHandler('ПН')}>ПН</a>
                    <a onClick={this.dayHandler('ВТ')}>ВТ</a>
                    <a onClick={this.dayHandler('СР')}>СР</a>
                    <a onClick={this.dayHandler('ЧТ')}>ЧТ</a>
                    <a onClick={this.dayHandler('ПТ')}>ПТ</a>
                    <a onClick={this.dayHandler('СБ')}>СБ</a>
                    <a onClick={this.dayHandler('ВС')}>ВС</a>
                </div>
                <div className="input">
                    <span>0:00</span>
                    <input id="inputRange" type="range" min="0" max="24" step="1" onMouseDown={this.mouseDown} onMouseUp={this.mouseUp}
                           onChange={this.onChange}/>
                    <span>23:59</span>

                </div>
                <div className="time">{this.state.time}:00</div>

            </div>
        )
    }
});
module.exports = Slider;