import React, { useState, useEffect } from 'react';
import axios from 'axios';

function HelloWorld() {
  const [from, setFrom] = useState();
  const [open, setOpen] = useState();
  const[close, setClose] = useState();
  const[high, setHigh] = useState();
  const[low, setLow] = useState();



  useEffect(() => {
    axios.get('http://localhost:8000/api/get-from/', {
      params: {
        symbol: 'aapl'
      }
    })
      .then(response => {
        console.log("res.data", response.data)
        setFrom(response.data.from);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

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

  useEffect(() => {
    axios.get('http://localhost:8000/api/get-high/', {
      params: {
        symbol: 'aapl'
      }
    })
      .then(response => {
        console.log("res.data", response.data)
        setHigh(response.data.high);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  useEffect(() => {
    axios.get('http://localhost:8000/api/get-low/', {
      params: {
        symbol: 'aapl'
      }
    })
      .then(response => {
        console.log("res.data", response.data)
        setLow(response.data.low);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);



  return (
    <div>
      <h1>Open and Close info</h1>
      {/* <p>{from}</p> */}
      <p>{open}</p>
      <p>{close}</p>
      <p>{high}</p>
      <p>{low}</p>
    </div>
  );
}

export default HelloWorld;