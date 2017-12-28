import React, { Component } from 'react';
import Vehicle from './vehicle.js';
import '../styles/Map.css';

class Map extends Component {
  render() {
    var vehicles = '';
    if(this.props.frame != null) {
      try {
        vehicles = this.props.frame.map(function(vehicle) {
          return (
              <Vehicle key={vehicle.key} 
                       x={vehicle.x} 
                       y={vehicle.y} 
                       direction={vehicle.direction} 
                       type={vehicle.type}>
              </Vehicle>
          );
        });
      }
      catch(e) {
        console.log(e);
      }
    } 
    return (
      <div className="Map">
        {vehicles}
      </div>
    );
  }
}

export default Map;
