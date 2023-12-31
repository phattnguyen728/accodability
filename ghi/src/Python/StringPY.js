import React from 'react';
import { Link } from 'react-router-dom';

const StringPython = () => {
  return (
    <div>
      <h2>String in Python</h2>
      <p>
        A collection of characters (letters, numbers, symbols) is known as a
        string. Strings must begin and end with quotation marks. Either single
        ' or double " will work, so long as you use the same at the beginning
        and end.
      </p>
      <Link to="/python">Back to Python Tutorial Home</Link>
    </div>
  );
};

export default StringPython;
