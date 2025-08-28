import React from 'react'
import './ScenarioForm.css'
import CustomInput from './CustomInput'

const inputs = document.querySelectorAll('.input')

Array.from(inputs).forEach(input => {
    input.addEventListener('click', () => {input.classList.toggle('active')})
});

export default function ScenarioForm () {
    return(
        <div className="container">
            <h1 className="scn">Scenario</h1>
            <p className="scntxt">You are the team manager for an upcoming project at your company. During an ideation meeting, a junior employee presents an idea. What would you do?</p>

            <CustomInput option="A. Ignore and move on"/>
            <CustomInput option="B. Acknowledge and bring attention"/>

            <input type="submit" value="Submit" className="formSubmit" />
        </div>
    )
}