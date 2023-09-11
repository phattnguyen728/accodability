import React from 'react';
import { Link } from 'react-router-dom';

const VariableJS = () => {
  return (
    <div>
      <h2>Variables in JavaScript</h2>
      <p>
        The word "variable" means "can change"; they're used to store values that can change.

        A variable is like a box with a sticky note stuck to it. Referencing the name on the sticky note will allow you to access whatever is inside the box (variable). Like the x and y variables used in mathematics, they're a simple name to represent the data we want to refer to.

      </p>
      <Link to="/javascript">Back to JavaScript Tutorial Home</Link>
    </div>
  );
};

export default VariableJS;
