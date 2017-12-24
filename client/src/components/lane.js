import React, { Component } from 'react';
import Car from './car.js';
import '../styles/Map.css';

class Lane extends Component {
  render() {

    var cars = this.props.cars.map(function(car) {
        return (
            <Car key={car.key} x={car.x} y={car.y}></Car>
        );
    });
    return (
      <div className="lane">
        {cars}
      </div>
    );
  }
}

export default Lane;
