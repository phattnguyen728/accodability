import React from "react";
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

  return (
    <div style={bodyStyle}>
      <div className="py-5 text-center" style={sectionStyle}>
        Congratulations May Class of 2023!!!
      </div>
      <div className="text-center">
        <img src={smile} alt="Smile GIF" />
      </div>
    </div>
  );
}

export default Graduation;
