import React, { useState, useEffect } from 'react';
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';


function pag0_app({ args }) {
    const [count, setCount] = useState(args.count || 0);
  
    useEffect(() => {
      Streamlit.setComponentValue(count);
      Streamlit.setFrameHeight();
    }, [count]);
  
    return (
      <>
        <div>
          <a href="https://vite.dev" target="_blank">
            <img src={viteLogo} className="logo" alt="Vite logo" />
          </a>
          <a href="https://react.dev" target="_blank">
            <img src={reactLogo} className="logo react" alt="React logo" />
          </a>
        </div>
        <h1>Vite + React</h1>
        <div className="card">
          <button onClick={() => setCount(count + 1)}>
            count is {count}
          </button>
          <p>
            Edit <code>src/App.jsx</code> and save to test HMR
          </p>
        </div>
        <p className="read-the-docs">
          Click on the Vite and React logos to learn more
        </p>
      </>
    )
  }
  
  export default withStreamlitConnection(pag0_app);