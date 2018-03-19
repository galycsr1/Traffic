import React, { Component } from 'react';
import Vehicle from './vehicle.js';
import '../styles/Map.css';
import loading_gif from '../images/loading.gif';

const MAP_HEIGHT = 500;
const MAP_WIDTH = 500;
const LANE_WIDTH = 130;
const DIRECTIONS = {
  TOP_TO_DOWN: 0,
  RIGHT_TO_LEFT: 1,
  DOWN_TO_UP: 2,
  LEFT_TO_RIGHT: 3
}

class Map extends Component { 
  
  render() {
    let mapStyle = {      
      height: MAP_HEIGHT + 'px',
      width: MAP_WIDTH + 'px'
    };
    let vehicles = [[], [], [], []];
    try {
      if(this.props.currentFrame != null) {
        let self = this;
        this.props.frames.map(function(directionFrames, index) {
          if(directionFrames != null) {
            if(directionFrames[self.props.currentFrame] != null) {
              let _vehicles = directionFrames[self.props.currentFrame].map(function(vehicle) {
                let x = vehicle.y;
                let y = vehicle.x;
                switch(vehicle.direction) {
                  case DIRECTIONS.TOP_TO_DOWN:
                    y = MAP_HEIGHT - y;
                    if(y > MAP_HEIGHT / 2) {
                      //return null;
                    }
                    break;
                  case DIRECTIONS.RIGHT_TO_LEFT:
                    x = x + y;
                    y = x - y;
                    x = x - y;
                    if(x < MAP_HEIGHT / 2) {
                      //return null;
                    }
                    break;
                  case DIRECTIONS.DOWN_TO_UP:
                    if(y < MAP_HEIGHT / 2) {
                      //return null;
                    }
                    break;
                  case DIRECTIONS.LEFT_TO_RIGHT:
                    x = x + y;
                    y = x - y;
                    x = x - y;
                    x = MAP_HEIGHT - x;
                    if(x > MAP_HEIGHT / 2) {
                      //return null;
                    }
                    break;
                  default:
                    break;
                }
                return (
                    <Vehicle key={vehicle.key} 
                             x={x}
                             y={y} 
                             direction={vehicle.direction} 
                             type={vehicle.type}
                             >
                    </Vehicle>
                );
              });
              vehicles[index] = _vehicles;
            }
          }
          return null;
        });  
      }       
    }
    catch(e) {
      console.log(e);
    }   
    //console.log(vehicles);
    let lane0Style = {
      top: 0,
      left: MAP_HEIGHT / 2 - LANE_WIDTH / 2,
      width: LANE_WIDTH,
      height: MAP_HEIGHT / 2
    };
    let lane1Style = {
      top: MAP_HEIGHT / 2 - LANE_WIDTH / 2,
      left: 0,
      width: MAP_HEIGHT / 2,
      height: LANE_WIDTH
    };
    let lane2Style = {
      top: MAP_HEIGHT / 2,
      left: MAP_HEIGHT / 2 - LANE_WIDTH / 2,
      width: LANE_WIDTH,
      height: MAP_HEIGHT / 2
    };
    let lane3Style = {
      top: MAP_HEIGHT / 2 - LANE_WIDTH / 2,
      left: MAP_HEIGHT / 2,
      width: MAP_HEIGHT / 2,
      height: LANE_WIDTH
    };
    let loading = '';
    let loadingStyle = {      
      backgroundImage: `url(${loading_gif})`,
      height: MAP_HEIGHT + 'px',
      width: MAP_WIDTH + 'px'
    };
    if(this.props.loading) {
      loading = (
        <div className="Loading" style={loadingStyle}></div>
      );
    }
    return (
      <div>
        <div className="Map" style={mapStyle}>
          <div>
            {vehicles[DIRECTIONS.TOP_TO_DOWN]}
          </div>
          <div>
            {vehicles[DIRECTIONS.RIGHT_TO_LEFT]}
          </div>
          <div>
            {vehicles[DIRECTIONS.DOWN_TO_UP]}
          </div>
          <div>
            {vehicles[DIRECTIONS.LEFT_TO_RIGHT]}
          </div>
          <div className="lanes">
            <div id="lane0" style={lane0Style}></div>
            <div id="lane1" style={lane1Style}></div>
            <div id="lane2" style={lane2Style}></div>
            <div id="lane3" style={lane3Style}></div>
          </div>
        </div>
        {loading}
      </div>
    );
  }
}

export default Map;
