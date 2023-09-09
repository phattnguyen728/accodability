import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";

function SignInForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { login, token } = useToken();

  let passwordAlert = document.getElementById("password-alert");

  function handleUsernameChange(event) {
    const { value } = event.target;
    setUsername(value);
    if (passwordAlert) {
      passwordAlert.classList.add("d-none");
    }
  }

  function handlePasswordChange(event) {
    const { value } = event.target;
    setPassword(value);
    if (passwordAlert) {
      passwordAlert.classList.add("d-none");
    }
  }

  async function handleSubmit(event) {
    event.preventDefault();
    await login(username, password);
    setTimeout(() => {
      if (token === null) {
        passwordAlert.classList.remove("d-none");
      }
    }, 500);
  }

  useEffect(() => {
    if (token) {
      navigate("/");
    }
  }, [token, navigate]);

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
          <div
            className="alert alert-danger alert-dismissible d-none fade show"
            role="alert"
            id="password-alert"
          >
            <strong>Alert:</strong> Your username or password is incorrect;
            please re-enter and verify.
          </div>
        </div>
      </div>
    </div>
  );
}
export default SignInForm;
