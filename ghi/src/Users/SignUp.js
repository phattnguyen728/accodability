import React, { useState, useEffect } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";

function SignUpForm() {
  const [userData, setUserData] = useState([]);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [email, setEmail] = useState("");
  const { register } = useToken();
  const navigate = useNavigate();

  let successMessage = document.getElementById("create-success");
  let passwordAlert = document.getElementById("password-alert");
  let accountAlert = document.getElementById("account-alert");
  let emailAlert = document.getElementById("email-alert");

  function handleFirstNameChange(event) {
    const { value } = event.target;
    setFirstName(value);
    successMessage.classList.add("d-none");
    passwordAlert.classList.add("d-none");
    accountAlert.classList.add("d-none");
    emailAlert.classList.add("d-none");
  }

  function handleLastNameChange(event) {
    const { value } = event.target;
    setLastName(value);
    successMessage.classList.add("d-none");
    passwordAlert.classList.add("d-none");
    accountAlert.classList.add("d-none");
    emailAlert.classList.add("d-none");
  }

  function handleUsernameChange(event) {
    const { value } = event.target;
    setUsername(value);
    successMessage.classList.add("d-none");
    passwordAlert.classList.add("d-none");
    accountAlert.classList.add("d-none");
    emailAlert.classList.add("d-none");
  }

  function handlePasswordChange(event) {
    const { value } = event.target;
    setPassword(value);
    successMessage.classList.add("d-none");
    passwordAlert.classList.add("d-none");
    accountAlert.classList.add("d-none");
    emailAlert.classList.add("d-none");
  }

  function handleConfirmPasswordChange(event) {
    const { value } = event.target;
    setConfirmPassword(value);
    successMessage.classList.add("d-none");
    passwordAlert.classList.add("d-none");
    accountAlert.classList.add("d-none");
    emailAlert.classList.add("d-none");
  }

  function handleEmailChange(event) {
    const { value } = event.target;
    setEmail(value);
    successMessage.classList.add("d-none");
    passwordAlert.classList.add("d-none");
    accountAlert.classList.add("d-none");
    emailAlert.classList.add("d-none");
  }

  async function getUserData() {
    const url = `${process.env.REACT_APP_API_HOST}/users`;
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setUserData(data);
    } else {
      console.error("An error occurred fetching user data");
    }
  }

  useEffect(() => {
    getUserData();
  }, []);

  async function handleSubmit(event) {
    event.preventDefault();
    if (password !== confirmPassword) {
      passwordAlert.classList.remove("d-none");
    }
    for (let idx in userData) {
      if (userData[idx]["username"] == username) {
        accountAlert.classList.remove("d-none");
        return;
      }
      if (userData[idx]["email"] == email) {
        emailAlert.classList.remove("d-none");
        return;
      }
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
      successMessage.classList.remove("d-none");
      setTimeout(() => {
        navigate("/");
      }, 1000);
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
          <div
            className="alert alert-danger alert-dismissible d-none fade show"
            role="alert"
            id="account-alert"
          >
            <strong>Alert:</strong> Username already exists; please enter an
            alternate username.
          </div>
          <div
            className="alert alert-danger alert-dismissible d-none fade show"
            role="alert"
            id="email-alert"
          >
            <strong>Alert:</strong> Email already exists; please use your
            original account.
          </div>
        </div>
      </div>
    </div>
  );
}
export default SignUpForm;
