import React , {Component} from 'react';
import ZipList from './ZipList';
import MetroList from './MetroList';
import Countylist from './CountryList';
import StateList from './StateList';
import { Tab, Nav} from 'react-bootstrap';

class LeaderBoards extends Component {
    render(){
        return (
        
        <Tab.Container defaultActiveKey="first">
     
                
                <Nav variant="pills" className="flex-row justify-content-center">
                <Nav.Item>
                    <Nav.Link eventKey="first">
                    State
                    </Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="second">
                    Metro
                    </Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="third" >
                    County
                    </Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="fourth" >
                    Zip Code
                    </Nav.Link>
                </Nav.Item>
            </Nav>

              {/* <Col sm={12} md={8} lg={9}> */}
                <Tab.Content>
                  <Tab.Pane eventKey="first">
                    <StateList/>
                  </Tab.Pane>
                  <Tab.Pane eventKey="second">
                    <MetroList/>
                  </Tab.Pane>
                  <Tab.Pane eventKey="third">
                    <Countylist/>
                  </Tab.Pane>
                  <Tab.Pane eventKey="fourth">
                    <ZipList/>
                  </Tab.Pane>
                </Tab.Content>
              {/* </Col> */}
  
          </Tab.Container>
        );
    }
}
export default LeaderBoards;
