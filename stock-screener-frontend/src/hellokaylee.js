import React, { useState, useEffect } from 'react';
import axios from 'axios';

function HelloWorld() {
  const [onc, setOnc] = useState();



  useEffect(() => {
    axios.get('http://localhost:8000/api/get-onc/', {
      params: {
        symbol: 'aapl'
      }
    })
      .then(response => {
        console.log("res.data", response.data)
        setOnc(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);



  return (
    <div>
      <h1>Open and Close info</h1>
      <p>{onc}</p>
    </div>
  );
}

export default HelloWorld;