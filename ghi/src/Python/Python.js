import React from 'react';
import { Link } from 'react-router-dom';

const Python = () => {
  const topics = [
    { name: 'Strings', route: 'python/strings' },
    { name: 'Variables', route: 'python/variables' },
    { name: 'Arrays', route: 'python/arrays' },
    { name: 'Objects', route: 'python/objects' },
  ];

  return (
    <>
      <div>
        <h2>Python Topics</h2>
        <ul>
          {topics.map((topic) => (
            <li key={topic.route}>
              <Link to={`/${topic.route}`}>{topic.name}</Link>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
};

export default Python;
