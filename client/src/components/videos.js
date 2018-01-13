import React, { Component } from 'react';
import Video from './video.js';
import '../styles/Videos.css';

class Videos extends Component {

  seekTo = n => {    
    this.refs.video0.seekTo(n);
    this.refs.video1.seekTo(n);
    this.refs.video2.seekTo(n);
    this.refs.video3.seekTo(n);
  }

  render() {
    return (
      <div className="Videos">
        <Video ref="video0"
                  onProgress={this.props.onProgress}
                  playing={this.props.playing} 
                  playbackRate={this.props.playbackRate} 
                  onEnded={this.props.onEnded}
                  url={this.props.urls[0]}
                  onProgress={this.props.onProgress}>          
        </Video>
        <Video ref="video1"
                  playing={this.props.playing} 
                  playbackRate={this.props.playbackRate} 
                  onEnded={this.props.onEnded}
                  url={this.props.urls[1]}
                  onProgress={this.props.onProgress}>          
        </Video>
        <Video ref="video2"
                  playing={this.props.playing} 
                  playbackRate={this.props.playbackRate} 
                  onEnded={this.props.onEnded}
                  url={this.props.urls[2]}
                  onProgress={this.props.onProgress}>          
        </Video>
        <Video ref="video3"
                  playing={this.props.playing} 
                  playbackRate={this.props.playbackRate} 
                  onEnded={this.props.onEnded}
                  url={this.props.urls[3]}
                  onProgress={this.props.onProgress}>          
        </Video>
      </div>
    );
  }
}

export default Videos;
