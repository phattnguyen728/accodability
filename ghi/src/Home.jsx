import React from "react";
import { Link } from "react-router-dom";
import alyn2 from "./Assets/alyn2.png";

function Home() {
  const background =
    "https://img.freepik.com/premium-vector/mountains-panoramic-view-abstract-illustration_185757-1312.jpg?w=2000";

  const sectionStyle = {
    backgroundImage: `url(${background})`,
    backgroundPosition: "center",
    backgroundSize: "cover",
    backgroundRepeat: "no-repeat",
  };

  const styleGif = {
    borderRadius: "50%",
    width: "350px",
    height: "350px",
    background: "black",
  };

  return (
    <>
      <div className=" py-5 text-center" style={sectionStyle}>
        <h1 className="display-5 fw-bold">Accodability</h1>
        <div className="col-lg-6 mx-auto">
          <p className="lead mb-4">Learn to code on your own wave 🌊 </p>
          <img
            src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXRtMjA1bXQ0M2dsN3dhYmU1d2Uzb3hkY3ZwMmxmbDIxeHMwMGdzMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iIT5Y3Tz5AJ6yr4j55/giphy.gif"
            alt="ac-gif"
            style={styleGif}
          ></img>
        </div>
      </div>
      <div className="container-fluid py-3 text-center bg-light">
        <div className="row">
          <div className="col">
            <div className="card border-dark mb-3">
              <div className="card-header text-bg-secondary">Add Friends</div>
              <img
                src="https://media.istockphoto.com/id/1321230821/vector/illustration-of-fist-bump-the-fist-bump-is-a-greeting-that-touches-fists-and-fists.jpg?s=612x612&w=0&k=20&c=TIpaEvrQ-QOsMYEpm9GtOyjF7AzRhvtYBb_4oMqIxeU="
                className="card-img-top"
                alt="friends-alt"
              />
              <div className="card-body text-bg-light mb-3">
                <h5 className="card-title">Find Self-Learners Like You!</h5>
                <p className="card-text">
                  Use our built-in friends feature to find other programmers
                  interested in maximizing their ability to learn and grow.
                </p>
              </div>
            </div>
          </div>
          <div className="col">
            <div className="card border-dark mb-3">
              <div className="card-header text-bg-secondary">
                Post & Comment
              </div>
              <img
                src="https://media.istockphoto.com/id/1370336623/vector/line-browser-window-in-black-color-internet-stroke-page-concept-for-desktop-and-tablet-empty.jpg?s=612x612&w=0&k=20&c=ddP76kqkB4kLmp9g_Ae5iHidcoYBnczwa-cSaodqSQQ="
                className="card-img-top"
                alt="posts-alt"
              />
              <div className="card-body text-bg-light mb-3">
                <h5 className="card-title">Community Curated Resources</h5>
                <p className="card-text">
                  View, share, and comment on programming related resources from
                  all over the web. Our community will help you find the best
                  content and tutorials to help you along your journey.
                </p>
              </div>
            </div>
          </div>
          <div className="col">
            <div className="card border-dark mb-3">
              <div className="card-header text-bg-secondary">Send Messages</div>
              <img
                src="https://media.istockphoto.com/id/1153246546/vector/paper-plane-continuous-one-line-drawing.jpg?s=612x612&w=0&k=20&c=sWgKoEl6AeTUsaBt0CcrVXiO_rWbVsQXJYJT__-7zGk="
                className="card-img-top"
                alt="messages-alt"
              />
              <div className="card-body text-bg-light mb-3">
                <h5 className="card-title">Collaborate & Conquer</h5>
                <p className="card-text">
                  Send messages to your friends and favorite posters. There is
                  always something and someone to learn from!
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <Link to="/alyn">
          <img
            src={alyn2}
            alt="Click to view Alyn's page"
            height="15px"
            width="15px"
          />
        </Link>
      </div>
    </>
  );
}
export default Home;
