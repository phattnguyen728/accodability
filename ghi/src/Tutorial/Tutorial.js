import React from "react";
import "./tutorial.css";
import { Link } from "react-router-dom";


function Tutorial() {
  return (
    <div className="tutorial">
      <div className="background-image">
        <div className="header">
          <h2 className="header-text">Want to learn coding?</h2>
        </div>

        <div className="columns">
          {/* Left Column for JavaScript */}
          <div className="left-column">
            <h2>Do you like Coffee?</h2>
            <div className="image-container">
              <img
                src="https://img.freepik.com/free-photo/fresh-coffee-steams-wooden-table-close-up-generative-ai_188544-8923.jpg?w=2000&t=st=1694424160~exp=1694424760~hmac=e1dcb8176a91eba1b1e43bbed233bd1879cba58f9da13f126a6b92ea5ab02431"
                alt="Coffee"
                className="image"
              />
            </div>
            <p>Do you get the jitters?</p>
            <div className="image-container">
              <img
                src="https://img.freepik.com/free-vector/coffee-love-foam-with-beans-cartoon-icon-illustration_138676-2575.jpg?w=2000&t=st=1694424172~exp=1694424772~hmac=7b2eac045ce56385ae1b280b8461f870d58897b033af0bbb02ca056c9eaf7186"
                alt="Coffee Jitters"
                className="image"
              />
            </div>
            <p>Do you go JAVA JAVA JAVA JAVA?</p>
            <p>Well click the image below for a taste</p>
            <div className="image-container">
              <Link to="/javascript">
                <img
                  src="https://img.freepik.com/free-photo/fresh-coffee-steams-wooden-table-close-up-generative-ai_188544-8923.jpg?w=2000&t=st=1694424160~exp=1694424760~hmac=e1dcb8176a91eba1b1e43bbed233bd1879cba58f9da13f126a6b92ea5ab02431"
                  alt="Coffee"
                  className="image"
                />
              </Link>
            </div>
          </div>

          {/* OR Text */}
          <div className="or-text">
            <h3>OR</h3>
          </div>

          {/* Right Column for Python */}
          <div className="right-column">
            <h2>Do you like Reptiles</h2>
            <div className="image-container">
              <img
                src="https://img.freepik.com/free-vector/cute-snake-illustration_478747-314.jpg?w=2000&t=st=1694424191~exp=1694424791~hmac=1fd5b2676e0adbbb566a25f2adeb36dd5d01806cc5ea886d695f4fa47d81848d"
                alt="Snake"
                className="image"
              />
            </div>
            <p>Are you ssssure?</p>
            <div className="image-container">
              <img
                src="https://img.freepik.com/free-vector/green-snake-cartoon-character-isolated-white-background_1308-64260.jpg?size=626&ext=jpg&ga=GA1.2.836317560.1694413651&semt=sph"
                alt="Coding"
                className="image"
              />
            </div>
            <p>Then maybe thisssssss is for you</p>
            <p>Pleasssssse slither on to the image below and take a byte</p>
            <div className="image-container">
              <Link to="/python">
                <img
                  src="https://img.freepik.com/free-photo/programming-script-text-coding-word_53876-121207.jpg?w=2000&t=st=1694424183~exp=1694424783~hmac=02aec2d1fd4de5f919d9fcd503b2f9ae295b622ad5cb22afeb5ce6db88e96bb8"
                  alt="Python"
                  className="image"
                />
              </Link>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}

export default Tutorial;
