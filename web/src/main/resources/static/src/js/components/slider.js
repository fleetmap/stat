/**
 * Created by vlad on 21.05.16.
 */
var React = require('react');



var Slider = React.createClass({
    getInitialState: function () {
        return ({show: false, time: 12, day: 'ПН', active: 'id'})
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
    dayHandler: function (day, id) {
      return()=> {
          this.setState({day: day});
          document.getElementById(this.state.active);
          
          
          console.log(this.state);
      }
    },

    render: function () {

        return (
            <div id="slider">
                <div className="days">
                    <a id="mon" onClick={this.dayHandler('ПН', mon)}>ПН</a>
                    <a id="tue" onClick={this.dayHandler('ВТ', tue)}>ВТ</a>
                    <a id="wen" onClick={this.dayHandler('СР', wen)}>СР</a>
                    <a id="thu" onClick={this.dayHandler('ЧТ', thu)}>ЧТ</a>
                    <a id="fri" onClick={this.dayHandler('ПТ', fri)}>ПТ</a>
                    <a id="sat" onClick={this.dayHandler('СБ', sat)}>СБ</a>
                    <a id="sun" onClick={this.dayHandler('ВС', sun)}>ВС</a>
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