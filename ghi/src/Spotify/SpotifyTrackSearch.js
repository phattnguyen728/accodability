import React, { useEffect } from "react";

const SpotifyPlayer = ({ accessToken }) => {
  useEffect(() => {
    // Load the Spotify Web Playback SDK script
    const script = document.createElement("script");
    script.src = "https://sdk.scdn.co/spotify-player.js";
    script.async = true;
    document.body.appendChild(script);

    // Initialize the Spotify SDK when the script is loaded
    script.onload = () => {
      window.onSpotifyWebPlaybackSDKReady = () => {
        const player = new Spotify.Player({
          name: "My Spotify Web Player",
          getOAuthToken: (callback) => {
            callback(accessToken);
          },
        });

        // Error handling
        player.addListener("initialization_error", ({ message }) => {
          console.error("Initialization Error:", message);
        });
        player.addListener("authentication_error", ({ message }) => {
          console.error("Authentication Error:", message);
        });
        player.addListener("account_error", ({ message }) => {
          console.error("Account Error:", message);
        });
        player.addListener("playback_error", ({ message }) => {
          console.error("Playback Error:", message);
        });

        // Ready
        player.addListener("ready", ({ device_id }) => {
          console.log("Ready with Device ID", device_id);

          // Play a Spotify track
          const playTrack = async () => {
            const trackUri =
              "https://open.spotify.com/track/3a1lNhkSLSkpJE4MSHpDu9"; // Replace with the Spotify track URI
            const response = await fetch(
              `https://api.spotify.com/v1/me/player/play?device_id=${device_id}`,
              {
                method: "PUT",
                body: JSON.stringify({ uris: [trackUri] }),
                headers: {
                  "Content-Type": "application/json",
                  Authorization: `Bearer ${accessToken}`,
                },
              }
            );

            if (!response.ok) {
              console.error("Failed to play track:", response.statusText);
            }
          };

          // Example: Play a track when a button is clicked
          document
            .getElementById("play-button")
            .addEventListener("click", () => {
              playTrack();
            });
        });

        // Connect to the Spotify player
        player.connect();
      };
    };

    // Cleanup when the component unmounts
    return () => {
      document.body.removeChild(script);
    };
  }, [accessToken]);

  return (
    <div>
      <h2>Spotify Player</h2>
      <button id="play-button">Play Song</button>
    </div>
  );
};

export default SpotifyPlayer;
