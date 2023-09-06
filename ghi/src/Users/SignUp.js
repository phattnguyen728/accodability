import React, { useState } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";

function SignUpForm() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [email, setEmail] = useState("");
  const { register } = useToken();
  const navigate = useNavigate();

  function handleFirstNameChange(event) {
    const { value } = event.target;
    setFirstName(value);
    let successMessage = document.getElementById("create-success");
    successMessage = successMessage.classList.add("d-none");
    let passwordAlert = document.getElementById("password-alert");
    passwordAlert = passwordAlert.classList.add("d-none");
  }

  function handleLastNameChange(event) {
    const { value } = event.target;
    setLastName(value);
    let successMessage = document.getElementById("create-success");
    successMessage = successMessage.classList.add("d-none");
    let passwordAlert = document.getElementById("password-alert");
    passwordAlert = passwordAlert.classList.add("d-none");
  }

  function handleUsernameChange(event) {
    const { value } = event.target;
    setUsername(value);
    let successMessage = document.getElementById("create-success");
    successMessage = successMessage.classList.add("d-none");
    let passwordAlert = document.getElementById("password-alert");
    passwordAlert = passwordAlert.classList.add("d-none");
  }

  function handlePasswordChange(event) {
    const { value } = event.target;
    setPassword(value);
    let successMessage = document.getElementById("create-success");
    successMessage = successMessage.classList.add("d-none");
    let passwordAlert = document.getElementById("password-alert");
    passwordAlert = passwordAlert.classList.add("d-none");
  }

  function handleConfirmPasswordChange(event) {
    const { value } = event.target;
    setConfirmPassword(value);
    let successMessage = document.getElementById("create-success");
    successMessage = successMessage.classList.add("d-none");
    let passwordAlert = document.getElementById("password-alert");
    passwordAlert = passwordAlert.classList.add("d-none");
  }

  function handleEmailChange(event) {
    const { value } = event.target;
    setEmail(value);
    let successMessage = document.getElementById("create-success");
    successMessage = successMessage.classList.add("d-none");
    let passwordAlert = document.getElementById("password-alert");
    passwordAlert = passwordAlert.classList.add("d-none");
  }

  async function handleSubmit(event) {
    event.preventDefault();
    if (password !== confirmPassword) {
      let passwordAlert = document.getElementById("password-alert");
      passwordAlert = passwordAlert.classList.remove("d-none");
    }
    if (password === confirmPassword) {
      const accountData = {
        first_name: firstName,
        last_name: lastName,
        username: username,
        password: password,
        email: email,
      };
      register(accountData, `${process.env.REACT_APP_API_HOST}/users`);
      event.target.reset();
      let successMessage = document.getElementById("create-success");
      successMessage = successMessage.classList.remove("d-none");
    }
  }

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Account Registration</h1>
          <form onSubmit={handleSubmit} id="add-user-form">
            <div className="form-floating mb-3">
              <input
                onChange={handleFirstNameChange}
                value={firstName}
                required
                type="text"
                id="firstName"
                className="form-control"
              />
              <label htmlFor="firstName" className="form-label">
                First Name
              </label>
            </div>
            <div className="form-floating mb-3">
              <input
                onChange={handleLastNameChange}
                value={lastName}
                required
                type="text"
                id="lastName"
                className="form-control"
              />
              <label htmlFor="lastName" className="form-label">
                Last Name
              </label>
            </div>
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
            <div className="form-floating mb-3">
              <input
                onChange={handleConfirmPasswordChange}
                value={confirmPassword}
                type="password"
                id="confirmPassword"
                className="form-control"
                required
              />
              <label htmlFor="password" className="form-label">
                Confirm Password
              </label>
            </div>
            <div className="form-floating mb-3">
              <input
                onChange={handleEmailChange}
                value={email}
                type="text"
                id="email"
                className="form-control"
                required
              />
              <label htmlFor="email" className="form-label">
                E-Mail Address
              </label>
            </div>
            <button className="btn btn-primary">Create Account</button>
          </form>
          <div
            className="alert alert-success alert-dismissible d-none fade show"
            role="alert"
            id="create-success"
          >
            <strong>Success:</strong> You account has been created.
          </div>
          <div
            className="alert alert-danger alert-dismissible d-none fade show"
            role="alert"
            id="password-alert"
          >
            <strong>Alert:</strong> Your passwords do not match; please re-enter
            and verify.
          </div>
        </div>
      </div>
    </div>
  );
}
export default SignUpForm;
