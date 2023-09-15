import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import Home from "./Home";
import Nav from "./Nav";
import SignUpForm from "./Users/SignUp.js";
import SignInForm from "./Users/SignIn.js";
import MessageInbox from "./Messages/MessagesInbox";
import MessageForm from "./Messages/MessageForm";
import FriendList from "./Friends/FriendList";
import FriendRequestForm from "./Friends/FriendRequestForm";
import GetComments from "./Comments/GetComments";
import GetCommentsByUser from "./Comments/GetCommentsByUser";
import CommentForm from "./Comments/CommentForm";
import CreatePostForm from "./Posts/CreatePostForm";
import ViewAllPostsForm from "./Posts/ViewAllPostsForm";
import FindAlyn from "./Wanted/FindAlyn";
import WeatherApi from "./Weather/Weather";
import Tutorial from "./Tutorial/Tutorial";
import Javascript from "./Javascript/Javascript";
import ArrayJS from "./Javascript/ArrayJS";
import ObjectJS from "./Javascript/ObjectJS";
import StringJS from "./Javascript/StringJS";
import VariableJS from "./Javascript/VariableJS";
import Python from "./Python/Python";
import ArrayPython from "./Python/ArrayPY";
import ObjectPython from "./Python/ObjectPY";
import StringPython from "./Python/StringPY";
import VariablePython from "./Python/VariablePY";
import Footer from "./Footer";
import Graduation from "./Grad/Graduation";

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
            <Route path="/addfriend" element={<FriendRequestForm />} />
            <Route path="/messages" element={<MessageInbox />} />
            <Route path="/compose" element={<MessageForm />} />
            <Route path="/comments" element={<GetComments />} />
            <Route path="/comments/yours" element={<GetCommentsByUser />} />
            <Route path="/comments/create" element={<CommentForm />} />
            <Route path="/posts/create" element={<CreatePostForm />} />
            <Route path="/posts/view" element={<ViewAllPostsForm />} />
            <Route path="/signin" element={<SignInForm />} />
            <Route path="/alyn" element={<FindAlyn />} />
            <Route path="/weather" element={<WeatherApi />} />
            <Route path="/tutorial" element={<Tutorial />} />
            <Route path="/javascript" element={<Javascript />} />
            <Route path="/javascript/arrays" element={<ArrayJS />} />
            <Route path="/javascript/strings" element={<StringJS />} />
            <Route path="/javascript/variables" element={<VariableJS />} />
            <Route path="/javascript/objects" element={<ObjectJS />} />
            <Route path="/python" element={<Python />} />
            <Route path="/python/arrays" element={<ArrayPython />} />
            <Route path="/python/strings" element={<StringPython />} />
            <Route path="/python/variables" element={<VariablePython />} />
            <Route path="/python/objects" element={<ObjectPython />} />
            <Route path="/congrats" element={<Graduation />} />
          </Routes>
        </div>
        <div style={{ backgroundColor: "#1789a2" }}>
          <Footer />
        </div>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
