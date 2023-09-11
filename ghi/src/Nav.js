import { NavLink, useNavigate, Link } from "react-router-dom";
import useToken from "@galvanize-inc/jwtdown-for-react";

function Nav() {
  const { token, logout } = useToken();
  const navigate = useNavigate();

  function deleteToken(event) {
    logout();
    navigate("/");
  }

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-secondary">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">
          <img
            src="https://www.designfreelogoonline.com/wp-content/uploads/2019/08/00592-pointer-02.png"
            alt="Logo"
            width="30"
            height="24"
            className="d-inline-block align-text-top"
          ></img>
          Accodability
        </Link>
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
        <NavLink className="navbar-brand" to="/weather">
          Weather
        </NavLink>
        <NavLink className="navbar-brand" to="/tutorial">
          Tutorial
        </NavLink>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            {token && (
              <li className="nav-item dropdown">
                <Link
                  className="nav-link dropdown-toggle"
                  to="foo"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Messages
                </Link>
                <ul className="dropdown-menu">
                  <li>
                    <Link className="dropdown-item" to="/messages">
                      Inbox
                    </Link>
                  </li>
                  <li>
                    <Link className="dropdown-item" to="/compose">
                      Create Message
                    </Link>
                  </li>
                </ul>
              </li>
            )}
            {token && (
              <li className="nav-item dropdown">
                <Link
                  className="nav-link dropdown-toggle"
                  to="foo"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Friends
                </Link>
                <ul className="dropdown-menu">
                  <li>
                    <Link className="dropdown-item" to="/addfriend">
                      Add Friends
                    </Link>
                  </li>
                  <li>
                    <Link className="dropdown-item" to="/friends">
                      List Friends
                    </Link>
                  </li>
                </ul>
              </li>
            )}
            {token && (
              <li className="nav-item dropdown">
                <Link
                  className="nav-link dropdown-toggle"
                  to="foo"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Posts
                </Link>
                <ul className="dropdown-menu">
                  <li>
                    <Link className="dropdown-item" to="/posts/view">
                      View Posts
                    </Link>
                  </li>
                  <li>
                    <Link className="dropdown-item" to="/posts/create">
                      Create Posts
                    </Link>
                  </li>
                </ul>
              </li>
            )}
            {token && (
              <li className="nav-item dropdown">
                <Link
                  className="nav-link dropdown-toggle"
                  to="foo"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Comments
                </Link>
                <ul className="dropdown-menu">
                  <li>
                    <Link className="dropdown-item" to="/comments">
                      All Comments
                    </Link>
                  </li>
                  <li>
                    <Link className="dropdown-item" to="/comments/yours">
                      Your Comments
                    </Link>
                  </li>
                  <li>
                    <Link className="dropdown-item" to="/comments/create">
                      Create Comment
                    </Link>
                  </li>
                </ul>
              </li>
            )}
          </ul>
          <ul className="navbar-nav mb-2 mb-lg-0">
            {!token && (
              <li className="nav-item">
                <NavLink className="nav-link" aria-current="page" to="/signup">
                  Sign Up
                </NavLink>
              </li>
            )}
            {!token && (
              <li className="nav-item">
                <NavLink className="nav-link" aria-current="page" to="/signin">
                  Sign In
                </NavLink>
              </li>
            )}
            {token && (
              <button
                className="btn btn-light"
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
