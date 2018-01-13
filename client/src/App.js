import React, { Component } from 'react';
import axios from 'axios';
import logo from './images/logo.svg';
import Videos from './components/videos.js';
import Map from './components/map.js';
import Controls from './components/controls.js';
import './styles/App.css';

const FRAME_TIME = 0.066666666666;

class App extends Component {
  constructor(props) {

    super(props);
    this.state = {
      frames: [null, null, null, null],
      urls: [null, null, null, null],
      playing: false,
      played: 0,
      playbackRate: 1.0,      
      currentFrame: null,
      numOfFrames: 0,
      seeking: false
    }
  }

  playPause = () => {
    if(this.state.currentFrame == null || this.state.urls.filter(url => url != null).length === 0) {
      return;
    }
    if(!this.state.playing) {
      var timeout = FRAME_TIME * this.state.playbackRate;
      let self = this;
      var playFrame = function() {
        if(self.state.playing) {
          self.setState({
            currentFrame: self.state.currentFrame + 1
          });
          timeout = FRAME_TIME / self.state.playbackRate;
          setTimeout(playFrame, timeout * 1000);
        }
      }
      setTimeout(playFrame, timeout);
    }
    this.setState({ playing: !this.state.playing });
  }
  onEnded = () => {
    this.setState({ 
      playing: false,
      currentFrame: 0
    });    
  }
  setPlaybackRate = e => {
    let rate = parseFloat(e.target.value);
    this.setState({ playbackRate: rate });
  }
  onSeekMouseDown = e => {
    //this.setState({ seeking: true });
  }
  onSeekChange = e => {
    let seekTo = parseFloat(e.target.value);
    this.setState({ 
      played: seekTo,
      currentFrame: Math.floor(this.state.numOfFrames * seekTo)
    });
    this.refs.videos.seekTo(seekTo);
  }
  onSeekMouseUp = e => {
    //let seekTo = parseFloat(e.target.value);
    //this.setState({ seeking: false });
    //this.refs.videos.seekTo(seekTo);
  }
  onProgress = state => {
    console.log(state);
    if (!this.state.seeking) {
      console.log(state);
      this.setState(state);
    }
  }
  
  readVideoFile = (i, event) => {
    const input = event.target;
    const url = URL.createObjectURL(input.files[0]);
    let urls = this.state.urls;
    urls[i] = url;
    this.setState({
      urls: urls
    });
  }

  readFramesFile = (i, event) => {
    const input = event.target;
    const file = input.files[0];
    var reader = new FileReader();
    let self = this;
    reader.onload = function(){
      const text = reader.result;
      /*self.setState({
        frames: JSON.parse(text),
        currentFrame: 0
      });*/
      axios.post('http://localhost:8080/', {
        route: 'getFrames',
        input: text
      })
      .then(function (response) {
        //console.log(response);
        try {
          let _frames = self.state.frames;
          _frames[i] = self.parseFrames(response.data, (i + 1) * 90);
          self.setState({
            frames: _frames,
            currentFrame: 0,
            numOfFrames: _frames[i].length
          });
        }
        catch(e) {
          console.log(e);
        }
      })
      .catch(function (error) {
        console.log(error);
      });
    };
    reader.readAsText(file);
  }

  parseFrames = (json, direction) => {
    let i = 0;
    let frames = [];
    json.map(function(frame) {
      let cars = [];
      frame.map(function(car) {
        cars.push({
          y: Math.floor(car.bounding_box[0] / 2),
          x: 500 - Math.floor(car.bounding_box[1] / 2),
          type: car.type,
          direction: direction,
          tracking_id: car.tracking_id,
          key: i
        });
        i++;
        return null;
      });
      frames.push(cars);
      return null;
    });
    return frames;
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">NoTraffic</h1>
        </header>
        <div>
        <Controls ref="controls"
                    readVideoFile={this.readVideoFile.bind(this)} 
                    readFramesFile={this.readFramesFile.bind(this)} 
                    playing={this.state.playing}
                    played={this.state.played} 
                    playPause={this.playPause.bind(this)}
                    playbackRate={this.state.playbackRate} 
                    setPlaybackRate={this.setPlaybackRate.bind(this)} 
                    onSeekMouseDown={this.onSeekMouseDown.bind(this)}
                    onSeekChange={this.onSeekChange.bind(this)}
                    onSeekMouseUp={this.onSeekMouseUp.bind(this)}>
          </Controls>
          <Map ref="map"
               frames={this.state.frames}
               currentFrame={this.state.currentFrame}
               playing={this.state.playing}
               played ={this.state.played}
               playbackRate={this.state.playbackRate} 
               setPlaybackRate={this.setPlaybackRate.bind(this)}>
          </Map>
          <Videos ref="videos"
                  onProgress={this.onProgress.bind(this)}
                  onEnded={this.onEnded.bind(this)}
                  playing={this.state.playing}
                  playbackRate={this.state.playbackRate} 
                  setPlaybackRate={this.setPlaybackRate.bind(this)} 
                  urls={this.state.urls}>
          </Videos>          
          
        </div>
      </div>
    );
  }
}

export default App;
