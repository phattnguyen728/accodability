import React, { useState } from "react";
import Confetti from "react-confetti";
import ReactAudioPlayer from "react-audio-player";
import congratAudio from "../Assets/congrat.mp3";
import smile from "../Assets/smile.gif";

function Graduation() {
  const sectionStyle = {
    backgroundColor: "#81D4FA",
    color: "white",
    fontSize: "40px",
    padding: "20px",
  };

  const bodyStyle = {
    backgroundColor: "#B3E5FC",
  };

  const confettiConfig = {
    width: "2000%",
    height: "800%",
  };

  const [playClicked, setPlayClicked] = useState(false);

  const handlePlayButtonClick = () => {
    setPlayClicked(true);
  };

  return (
    <>
      <div style={bodyStyle}>
        <div className="py-5 text-center" style={sectionStyle}>
          Congratulations May Class of 2023!!!
        </div>
        <div className="text-center">
          {!playClicked && (
            <button onClick={handlePlayButtonClick}>Hit this button</button>
          )}
          {playClicked && (
            <>
              <img src={smile} alt="Smile GIF" />
              <Confetti {...confettiConfig} />
              <ReactAudioPlayer
                src={congratAudio}
                autoPlay={true}
                controls={false}
                volume={0.30}
                onEnded={() => {
                }}
              />
            </>
          )}
        </div>
      </div>
    </>
  );
}

export default Graduation;
