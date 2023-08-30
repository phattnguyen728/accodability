import { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Construct from "./Construct.js";
import ErrorNotification from "./ErrorNotification";
import "./App.css";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import Home from "./Home";
import Nav from "./Nav";
import SignUpForm from "./SignUp";

function App() {
  // const [launchInfo, setLaunchInfo] = useState([]);
  // const [error, setError] = useState(null);

  // useEffect(() => {
  //   async function getData() {
  //     let url = `${process.env.REACT_APP_API_HOST}/api/launch-details`;
  //     console.log("fastapi url: ", url);
  //     let response = await fetch(url);
  //     console.log("------- hello? -------");
  //     let data = await response.json();

  //     if (response.ok) {
  //       console.log("got launch data!");
  //       setLaunchInfo(data.launch_details);
  //     } else {
  //       console.log("drat! something happened");
  //       setError(data.message);
  //     }
  //   }
  //   getData();
  // }, []);
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, "");

  return (
    <BrowserRouter basename={basename}>
      <AuthProvider>
        <Nav />
        <div>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/signup" element={<SignUpForm />} />
          </Routes>
          {/* <ErrorNotification error={error} />
          <Construct info={launchInfo} /> */}
        </div>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
