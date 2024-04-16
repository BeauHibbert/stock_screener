import React, { useState, useEffect } from 'react';
import axios from 'axios';

function HelloWorld() {
  const [open, setOpen] = useState();
  const[close, setClose] = useState();



  useEffect(() => {
    axios.get('http://localhost:8000/api/get-open/', {
      params: {
        symbol: 'aapl'
      }
    })
      .then(response => {
        console.log("res.data", response.data)
        setOpen(response.data.open);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);


  useEffect(() => {
    axios.get('http://localhost:8000/api/get-close/', {
      params: {
        symbol: 'aapl'
      }
    })
      .then(response => {
        console.log("res.data", response.data)
        setClose(response.data.close);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);



  return (
    <div>
      <h1>Open and Close info</h1>
      <p>{open}</p>
      <p>{close}</p>
    </div>
  );
}

export default HelloWorld;