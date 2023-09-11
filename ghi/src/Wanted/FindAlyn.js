import React from 'react';
import ReactPlayer from 'react-player';

function FindAlyn() {
  return (
    <div>
      <h2>We Found Alyn in a Hopeful Place</h2>
      <ReactPlayer
        url="alyn.mov"
        controls={true}
        width="640px"
        height="360px"
        playing={true}
      />
    </div>
  );
}

export default FindAlyn;
