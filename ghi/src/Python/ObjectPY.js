import React from 'react';
import { Link } from 'react-router-dom';

const ObjectPython = () => {
  return (
    <div>
      <h2>Objects in Python</h2>
      <p>
        Dictionaries are similar to objects in JavaScript. They are collections of key-value pairs where each key maps to a specific value.
      </p>
      <Link to="/python">Back to Python Tutorial Home</Link>
    </div>
  );
};

export default ObjectPython;
