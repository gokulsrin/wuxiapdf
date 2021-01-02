import React, { Component, PureComponent } from 'react';
import ReactDOM from 'react-dom';

class Wuxia extends Component{
    constructor(props){
        super(props)
        this.state = {url: "nothing"};
    }
    getInputValue = () =>{
        console.log(document.getElementById("webid").value);
        var string = document.getElementById("webid").value;
        this.setState({url:string});
    }
    render(){
        var display = null;
        display = (
            <div>
                <input type = "text" placeholder = "enter url" id = "webid"></input>
                <button type = "button" onClick= {this.getInputValue}> Submit</button>
            
                <p> {this.state.url}</p>
            </div>
        )
        return display;
    }
}
export default Wuxia;