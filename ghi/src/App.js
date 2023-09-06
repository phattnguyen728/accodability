import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import Home from "./Home";
import Nav from "./Nav";
import SignUpForm from "./Users/SignUp.js";
import FriendList from "./Friends/FriendList.js";
import SignInForm from "./Users/SignIn.js";
import MessageInbox from "./Messages/MessagesInbox";
import MessageForm from "./Messages/MessageForm";

function App() {
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, "");

  return (
    <BrowserRouter basename={basename}>
      <AuthProvider baseUrl={process.env.REACT_APP_API_HOST}>
        <Nav />
        <div>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/signup" element={<SignUpForm />} />
            <Route path="/friends" element={<FriendList />} />
            <Route path="/messages" element={<MessageInbox />} />
            <Route path="/compose" element={<MessageForm />} />
            <Route path="/signin" element={<SignInForm />} />
          </Routes>
        </div>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
