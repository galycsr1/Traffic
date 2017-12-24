import React, { Component } from 'react';
import ReactPlayer from 'react-player';
import '../styles/Videos.css';

class Video extends Component {

    seekTo = n => {    
        if(this.refs.player) {
            this.refs.player.seekTo(n);
        }
    }

    render() {
        if(this.props.url == null) {
            return (
                <div className="Video">
                    <p>No Video Selected</p>                    
                </div>
            );
        }
        else {
            return (
                <div className="Video">
                    <ReactPlayer
                        ref="player"
                        width='100%'
                        height='100%'
                        url={this.props.url}
                        playing={this.props.playing}
                        playbackRate={this.props.playbackRate}
                        onProgress={this.props.onProgress} 
                        />
                </div>
            );
        }
    }
}

export default Video;
