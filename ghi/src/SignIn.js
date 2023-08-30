import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";

function SignInForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { login } = useToken();

  function handleUsernameChange(event) {
    const { value } = event.target;
    setUsername(value);
  }

  function handlePasswordChange(event) {
    const { value } = event.target;
    setPassword(value);
  }

  async function handleSubmit(event) {
    event.preventDefault();
    login(username, password);
    event.target.reset();
    navigate("/");
  }

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Account Login</h1>
          <form onSubmit={handleSubmit} id="login-form">
            <div className="form-floating mb-3">
              <input
                onChange={handleUsernameChange}
                value={username}
                required
                type="text"
                id="username"
                className="form-control"
                required
              />
              <label htmlFor="username" className="form-label">
                Username
              </label>
            </div>
            <div className="form-floating mb-3">
              <input
                onChange={handlePasswordChange}
                value={password}
                type="password"
                id="password"
                className="form-control"
                required
              />
              <label htmlFor="password" className="form-label">
                Password
              </label>
            </div>
            <button className="btn btn-primary">Login</button>
          </form>
        </div>
      </div>
    </div>
  );
}
export default SignInForm;
