import React from "react";
import smile from "../Assets/smile.gif";
import Confetti from 'react-confetti'

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


  return (
    <>
      <div style={bodyStyle}>
        <div className="py-5 text-center" style={sectionStyle}>
          Congratulations May Class of 2023!!!
        </div>
        <div className="text-center">
          <img src={smile} alt="Smile GIF" />
        </div>
      </div>
      <Confetti {...confettiConfig} />
    </>
  );
}

export default Graduation;
