import React, { Component } from 'react';
import Car from './car.js';
import '../styles/Map.css';

class Map extends Component {
  render() {
    var cars = this.props.cars.map(function(car) {
        return (
            <Car key={car.key} x={car.x} y={car.y}></Car>
        );
    });
    return (
      <div className="Map">
        {cars}
      </div>
    );
  }
}

export default Map;
