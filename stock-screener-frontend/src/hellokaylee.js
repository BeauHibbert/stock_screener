import React, { useState, useEffect } from 'react';
import axios from 'axios';

function HelloWorld() {
  const [aggs, setAggs] = useState();
  const [macd, setMacd] = useState();

  useEffect(() => {
    axios.get('http://localhost:8000/api/get-aggs/')
      .then(response => {
        setAggs(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  useEffect(() => {
    axios.get('http://localhost:8000/api/get-macd/')
      .then(response => {
        setMacd(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Hello, Beau!, Love Kaylee</h1>
      <p>{aggs}</p>
      <p>{macd}</p>
    </div>
  );
}

export default HelloWorld;