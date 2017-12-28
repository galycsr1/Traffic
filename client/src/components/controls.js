import React, { Component } from 'react';
import { Input, Label, Form, FormGroup, Button, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import '../styles/Controls.css';

class Controls extends Component {
    constructor(props) {
        super(props);
        this.state = {
            showFileModal: false
        };
    }
    toggleFileModal = (event) => {
        this.setState({
            showFileModal: !this.state.showFileModal
        });
    }
    render() {
        return (
          <div className="Controls">
            <Form>
                <FormGroup>
                    <Button color="danger" onClick={this.toggleFileModal}>Select files</Button> {' '}
                    <Button color="info" onClick={this.props.playPause}>{this.props.playing ? 'Pause' : 'Play'}</Button>
                </FormGroup>
                <FormGroup>
                    <Label>Seek</Label>
                    <input
                        type='range' min={0} max={1} step='any'
                        value={this.props.played}
                        onMouseDown={this.props.onSeekMouseDown}
                        onChange={this.props.onSeekChange}
                        onMouseUp={this.props.onSeekMouseUp}
                        />
                </FormGroup>
                <FormGroup>
                    <Label>Speed</Label>
                    <input
                        type='range' min={0.1} max={10} step="0.1" 
                        value={this.props.playbackRate} 
                        onChange={this.props.setPlaybackRate} 
                        />
                        <span> x{this.props.playbackRate}</span>
                </FormGroup>
                <FormGroup>
                    <Label>Progress</Label>
                    <progress max={1} value={this.props.played} />
                </FormGroup>
            </Form>

            <Modal isOpen={this.state.showFileModal} className="FilesModal">
                <ModalHeader toggle={this.toggleFileModal}>Select Files</ModalHeader>
                <ModalBody>
                    <Form>
                        <FormGroup>
                            <Label>Frames JSON</Label>
                            <Input type="file" accept="*.json" onChange={(event)=> { this.props.readFramesFile(event) }} />
                        </FormGroup>
                        <FormGroup>
                            <Label>Video file #1</Label>
                            <Input type="file" accept="video/*" onChange={(event)=> { this.props.readVideoFile(0, event) }} />
                        </FormGroup>
                        <FormGroup>
                            <Label>Video file #2</Label>
                            <Input type="file" accept="video/*" onChange={(event)=> { this.props.readVideoFile(1, event) }} />
                        </FormGroup>
                        <FormGroup>
                            <Label>Video file #3</Label>
                            <Input type="file" accept="video/*" onChange={(event)=> { this.props.readVideoFile(2, event) }} />
                        </FormGroup>
                        <FormGroup>
                            <Label>Video file #4</Label>
                            <Input type="file" accept="video/*" onChange={(event)=> { this.props.readVideoFile(3, event) }} />
                        </FormGroup>
                    </Form>
                </ModalBody>
                <ModalFooter>
                    <Button color="primary" onClick={this.toggleFileModal}>Done</Button>
                </ModalFooter>      
            </Modal>

          </div>
        );
      }
    }
    
    export default Controls;



