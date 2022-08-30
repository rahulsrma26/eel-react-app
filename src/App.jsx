import { useState, useEffect } from 'react'
import { eel } from "./eel.js";
import logo from "./assets/react.svg"
import './App.css';


function App() {
  const [msg, setMsg] = useState("Loading...");

  useEffect(() => {
    eel.get_text('Called from React!')(res => setMsg(res));
  }, []);

  return (
    <div className="App">
      <h1>
        {msg}
      </h1>
      <img src={logo} className="App-logo" alt="logo" />
    </div>
  )
}

export default App
