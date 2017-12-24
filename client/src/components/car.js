import React, { Component } from 'react';
import '../styles/Map.css';

class Car extends Component {
    
  render() {
    var style = {
        top: this.props.x + "px",
        left: this.props.y + "px"
    }

    return (
      <div className="car" style={style}>         
      </div>
    );
  }
}

export default Car;
