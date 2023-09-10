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
    <nav className="navbar navbar-expand-lg navbar-dark bg-secondary">
      <div className="container-fluid">
        <a className="navbar-brand" href="/">
          <img
            src="https://www.designfreelogoonline.com/wp-content/uploads/2019/08/00592-pointer-02.png"
            alt="Logo"
            width="30"
            height="24"
            className="d-inline-block align-text-top"
          ></img>
          Accodability
        </a>
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
            {token && (
              <li className="nav-item dropdown">
                <a
                  className="nav-link dropdown-toggle"
                  href="foo"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Messages
                </a>
                <ul className="dropdown-menu">
                  <li>
                    <a className="dropdown-item" href="/messages">
                      Inbox
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="/compose">
                      Create Message
                    </a>
                  </li>
                </ul>
              </li>
            )}
            {token && (
              <li className="nav-item dropdown">
                <a
                  className="nav-link dropdown-toggle"
                  href="foo"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Friends
                </a>
                <ul className="dropdown-menu">
                  <li>
                    <a className="dropdown-item" href="/addfriend">
                      Add Friends
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="/friends">
                      List Friends
                    </a>
                  </li>
                </ul>
              </li>
            )}
            {token && (
              <li className="nav-item dropdown">
                <a
                  className="nav-link dropdown-toggle"
                  href="foo"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Posts
                </a>
                <ul className="dropdown-menu">
                  <li>
                    <a className="dropdown-item" href="foo">
                      View Posts
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="/posts/create">
                      Create Posts
                    </a>
                  </li>
                </ul>
              </li>
            )}
            {token && (
              <li className="nav-item dropdown">
                <a
                  className="nav-link dropdown-toggle"
                  href="foo"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Comments
                </a>
                <ul className="dropdown-menu">
                  <li>
                    <a className="dropdown-item" href="/comments">
                      All Comments
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="/comments/yours">
                      Your Comments
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="/comments/create">
                      Create Comment
                    </a>
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
