import { NavLink, Link } from "react-router-dom";
import alyn2 from "./Assets/alyn2.png";
import Wave from "react-wavify";

function Footer() {
  return (
    <>
      <div className="bg-white mt-5 pt-5">
        <Wave fill="url(#gradient)" className="fixed-bottom">
          <defs>
            <linearGradient id="gradient" gradientTransform="rotate(90)">
              <stop offset="40%" stopColor="#aae0ee" />
              <stop offset="95%" stopColor="#1789a2" />
            </linearGradient>
          </defs>
        </Wave>
      </div>
      <nav
        className="navbar navbar-expand-lg navbar-dark fixed-bottom"
        style={{ backgroundColor: "aae0ee" }}
      >
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <img
              src="https://www.designfreelogoonline.com/wp-content/uploads/2019/08/00592-pointer-02.png"
              alt="Logo"
              width="30"
              height="24"
              className="d-inline-block align-text-top"
            ></img>
            Accodability 🌊
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
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <NavLink className="nav-link" aria-current="page" to="foo">
                  About
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" aria-current="page" to="foo">
                  Contact
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" aria-current="page" to="foo">
                  FAQ
                </NavLink>
              </li>
            </ul>
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <Link to="/alyn">
                  <img
                    src={alyn2}
                    alt="Click to view Alyn's page"
                    height="5px"
                    width="5px"
                  />
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </>
  );
}

export default Footer;
