import { NavLink, useNavigate } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";

function Nav() {
  const { token, logout } = useToken();
  const navigate = useNavigate();

  function deleteToken(event) {
    logout();
    navigate("/");
  }

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-success">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">
          Accodability
        </NavLink>
        <NavLink className="navbar-brand" to="/addfriend">
          Add Friend
        </NavLink>
        <NavLink className="navbar-brand" to="/friends">
          Friends
        </NavLink>
        <NavLink className="navbar-brand" to="/messages">
          Messages
        </NavLink>
        <NavLink className="navbar-brand" to="/compose">
          Create Message
        </NavLink>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            {!token && (
              <li className="nav-item">
                <NavLink
                  className="nav-link active"
                  aria-current="page"
                  to="/signup"
                >
                  Sign Up
                </NavLink>
              </li>
            )}
            {!token && (
              <li className="nav-item">
                <NavLink
                  className="nav-link active"
                  aria-current="page"
                  to="/signin"
                >
                  Sign In
                </NavLink>
              </li>
            )}
            {token && (
              <li className="nav-item">
                <NavLink
                  className="nav-link active"
                  aria-current="page"
                  to="/comments/create"
                >
                  Create Comment
                </NavLink>
              </li>
            )}
            {token && (
              <button
                className="btn btn-dark"
                onClick={(event) => deleteToken(event)}
                type="button"
              >
                Logout
              </button>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Nav;
