import React, { Component } from 'react';
import { Input, Label, FormGroup, Button, Modal, ModalHeader, ModalBody, ModalFooter, Container, Row, Col } from 'reactstrap';
import Video from './video.js';
import '../styles/Videos.css';

class Videos extends Component {

  constructor(props) {
    super(props);
    this.state = {
        videos: [{},{},{},{}].map(function(obj, index) { return { showFilesModal: false, ref: 'video' + index }; })
    };
  }

  toggleFileModal = index => {
    let videos = this.state.videos;
    videos[index].showFilesModal = !this.state.videos[index].showFilesModal;
    this.setState({
      videos: videos
    });
  }
  seekTo = index => {    
    this.refs.video0.seekTo(index);
    this.refs.video1.seekTo(index);
    this.refs.video2.seekTo(index);
    this.refs.video3.seekTo(index);
  }

  render() {
    let self = this;

    let videos = self.state.videos.map(function(video, index) {
      return (
        <Video    key={video.ref}
                  ref={video.ref}
                  playing={self.props.playing} 
                  playbackRate={self.props.playbackRate} 
                  onEnded={self.props.onEnded}
                  url={self.props.urls[index]}
                  onProgress={self.props.onProgress}>          
        </Video>
      );
    });

    let videos_container = (
      <Container className="Videos">
        <Row>
          <Col xs={6} onClick={(e) => self.toggleFileModal(0)}>
            {videos[0]}
          </Col>
          <Col xs={6} onClick={(e) => self.toggleFileModal(1)}>
            {videos[1]}
          </Col>
        </Row>
        <Row>
          <Col xs={6} onClick={(e) => self.toggleFileModal(2)}>
            {videos[2]}
          </Col>
          <Col xs={6} onClick={(e) => self.toggleFileModal(3)}>
            {videos[3]}
          </Col>
        </Row>
      </Container>
    );

    let select_files_modals =  self.state.videos.map(function(video, index) {
      return (
        <Modal isOpen={self.state.videos[index].showFilesModal} className="FilesModal" key={'modal'+index} keyboard={true}>
          <ModalHeader toggle={(e) => self.toggleFileModal(index)}>Select Files</ModalHeader>
          <ModalBody>
            <FormGroup className="inputRow">
                  <Label>Frames JSON #{index+1}</Label>
                  <Input type="file" accept="*.meta" onChange={(event)=> { self.props.readFramesFile(index, event) }} />
              </FormGroup>
              <FormGroup className="inputRow">
                  <Label>Video file #{index+1}</Label>
                  <Input type="file" accept="video/*" onChange={(event)=> { self.props.readVideoFile(index, event) }} />
              </FormGroup>
          </ModalBody>
          <ModalFooter>
              <Button color="primary" onClick={(e) => self.toggleFileModal(index)}>Done</Button>
          </ModalFooter>      
        </Modal>
      );
    });

    return (
      <div>
        {videos_container}
        {select_files_modals}
      </div>
    );
  }
}

export default Videos;
