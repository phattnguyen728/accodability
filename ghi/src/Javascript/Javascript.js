import React from 'react';
import { Link } from 'react-router-dom';

const Javascript = () => {
  const topics = [
    { name: 'Strings', route: 'javascript/strings' },
    { name: 'Variables', route: 'javascript/variables' },
    { name: 'Arrays', route: 'javascript/arrays' },
    { name: 'Objects', route: 'javascript/objects' },
  ];

  return (
    <>
      <div>
        <h2>JavaScript Topics</h2>
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

export default Javascript;
