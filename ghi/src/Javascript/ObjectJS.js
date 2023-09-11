import React from 'react';
import { Link } from 'react-router-dom';

const ObjectJS = () => {
  return (
    <div>
      <h2>Objects in JavaScript</h2>
      <p>
        Objects are like keys on a keyring that open a specific door and behind each door is a room that can store many things. If each key is labeled, you can quickly open doors and access the stuff inside.
      </p>
      <Link to="/javascript">Back to JavaScript Tutorial Home</Link>
    </div>
  );
};

export default ObjectJS;
