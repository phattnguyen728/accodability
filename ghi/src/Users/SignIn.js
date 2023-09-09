import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";

function SignInForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { login, token } = useToken();
  const [showPasswordAlert, setShowPasswordAlert] = useState(false);
  const [loginSuccess, setLoginSuccess] = useState(false);

  function handleUsernameChange(event) {
    const { value } = event.target;
    setUsername(value);
    setShowPasswordAlert(false);
  }

  function handlePasswordChange(event) {
    const { value } = event.target;
    setPassword(value);
    setShowPasswordAlert(false);
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setLoginSuccess(false);
    setShowPasswordAlert(false);

    await login(username, password);

    if (token === null) {
      setShowPasswordAlert(true);
    } else {
      setLoginSuccess(true);

      setTimeout(() => {
        navigate("/");
      }, 500);
    }
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
            className={`alert alert-danger alert-dismissible ${
              showPasswordAlert ? "" : "d-none"
            } fade show`}
            role="alert"
            id="password-alert"
          >
            <strong>Alert:</strong> Your username or password is incorrect;
            please re-enter and verify.
          </div>
          {loginSuccess && (
            <div className="alert alert-success" role="alert">
              Login successful. Redirecting...
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default SignInForm;
