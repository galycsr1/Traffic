import React, { Component } from 'react';
import logo from './images/logo.svg';
import Videos from './components/videos.js';
import Map from './components/map.js';
import Controls from './components/controls.js';
import './styles/App.css';

class App extends Component {
  constructor(props) {

    super(props);
    this.state = {
      urls: [null, null, null, null],
      playing: false,
      played: 0,
      playbackRate: 1.0,
      cars: []
    }
  }

  playPause = () => {
    if(this.state.urls.filter(url => url == null).length > 0) {
      //return;
    }
    this.setState({ playing: !this.state.playing })
  }
  setPlaybackRate = e => {
    let rate = parseFloat(e.target.value);
    this.setState({ playbackRate: rate })
  }
  onSeekMouseDown = e => {
    this.setState({ seeking: true });
  }
  onSeekChange = e => {
    let seekTo = parseFloat(e.target.value);
    this.setState({ played: seekTo });   
  }
  onSeekMouseUp = e => {
    let seekTo = parseFloat(e.target.value);
    this.setState({ seeking: false });
    this.refs.videos.seekTo(seekTo);
  }
  onProgress = state => {
    if (!this.state.seeking) {
      this.setState(state);
    }
  }
  
  readFile = (i, event) => {
    const input = event.target;
    const url = URL.createObjectURL(input.files[0]);
    let urls = this.state.urls;
    urls[i] = url;
    this.setState({
      urls: urls
    });
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
                    readFile={this.readFile.bind(this)} 
                    playing={this.state.playing}
                    played ={this.state.played} 
                    playPause={this.playPause.bind(this)}
                    playbackRate={this.state.playbackRate} 
                    setPlaybackRate={this.setPlaybackRate.bind(this)} 
                    onSeekMouseDown={this.onSeekMouseDown.bind(this)}
                    onSeekChange={this.onSeekChange.bind(this)}
                    onSeekMouseUp={this.onSeekMouseUp.bind(this)}>
          </Controls>
          <Map ref="map"
               cars={this.state.cars}
               playing={this.state.playing}
               played ={this.state.played}
               playbackRate={this.state.playbackRate} 
               setPlaybackRate={this.setPlaybackRate.bind(this)}>
          </Map>
          <Videos ref="videos"
                  onProgress={this.onProgress.bind(this)}
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
