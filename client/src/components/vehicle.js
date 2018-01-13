import React, { Component } from 'react';
import '../styles/Map.css';
import car_image from '../images/car.png';
import bus_image from '../images/bus.png';

class Vehicle extends Component {
    
  render() {
    var style = {
        top: this.props.y + 'px',
        left: this.props.x + 'px',
        transform: 'rotate(' + this.props.direction + 'deg)',
        backgroundImage: `url(${this.getVehicleImage(this.props.type)})`,
        width: this.getVehicleDimensions(this.props.type).width + 'px',
        height: this.getVehicleDimensions(this.props.type).height + 'px'
    }
	
    return (
      <div className="vehicle" style={style} >        
      </div>
    );
  }

  getVehicleImage = type => {
    switch(type) {
      case 'car':
        return car_image;
      case 'bus':
        return bus_image;
      default:
        return null;
    }
  }

  getVehicleDimensions = type => {
    switch(type) {
      case 'car':
        return {
          width: 20,
          height: 40
        };
      case 'bus':
        return {
          width: 35,
          height: 90
        };
      default:
        return {
          width: 0,
          height: 0
        };
    }
  }
}

export default Vehicle;
