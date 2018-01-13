import React, { Component } from 'react';
import Vehicle from './vehicle.js';
import '../styles/Map.css';

class Map extends Component {
  render() {
    let vehicles = [];
    try {
      if(this.props.currentFrame != null) {
        let self = this;
        this.props.frames.map(function(directionFrames) {
          if(directionFrames != null) {
            let _vehicles = directionFrames[self.props.currentFrame].map(function(vehicle) {
              return (
                  <Vehicle key={vehicle.key} 
                           x={vehicle.x} 
                           y={vehicle.y} 
                           direction={vehicle.direction} 
                           type={vehicle.type}>
                  </Vehicle>
              );
            });
            vehicles = vehicles.concat(_vehicles);
          }
          return null;
        });  
      }       
    }
    catch(e) {
      console.log(e);
    }   
    return (
      <div className="Map">
        {vehicles}
      </div>
    );
  }
}

export default Map;
