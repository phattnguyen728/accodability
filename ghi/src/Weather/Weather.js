import React, { useState, useEffect } from "react";
import "./weather.css";

function WeatherApi() {
  const [city, setCity] = useState(null);
  const [search, setSearch] = useState("");

  useEffect(() => {
    const fetchApi = async () => {
      const url = `http://api.openweathermap.org/data/2.5/weather?q=${search}&units=metric&appid=4ebb9418ca605fa1931880e565ec065c`;
      const response = await fetch(url);
      const resJson = await response.json();

      const tempInFahrenheit = (resJson.main.temp * 9 / 5) + 32;
      const tempMinInFahrenheit = (resJson.main.temp_min * 9 / 5) + 32;
      const tempMaxInFahrenheit = (resJson.main.temp_max * 9 / 5) + 32;

      setCity({
        ...resJson.main,
        temp: tempInFahrenheit,
        temp_min: tempMinInFahrenheit,
        temp_max: tempMaxInFahrenheit,
      });
    };
    fetchApi();
  }, [search]);

  const background =
    "https://img.freepik.com/free-photo/panoramic-view-field-covered-grass-trees-sunlight-cloudy-sky_181624-9801.jpg?t=st=1694413664~exp=1694414264~hmac=93bde9a56e1a9ed69c16adf70f976317037d86e12a8e4708d262c7b46eda6f2b";

  const sectionStyle = {
    backgroundImage: `url(${background})`,
    backgroundPosition: "center",
    backgroundSize: "cover",
    backgroundRepeat: "no-repeat",
    minHeight: "100vh",
  };

  return (
    <>
      <div className="py-5 text-center" style={sectionStyle}>
        <div className="box">
          <div className="InputData">
            <input
              type="search"
              className="InputField"
              placeholder="Enter city and state"
              onChange={(event) => {
                setSearch(event.target.value);
              }}
            />
            {!city ? (
              <div>
                <h3><b>No Data Found</b></h3>
                <div id="clouds">
                  <div className="cloud x1"></div>
                  <div className="cloud x2"></div>
                  <div className="cloud x3"></div>
                  <div className="cloud x4"></div>
                  <div className="cloud x5"></div>
                </div>
              </div>
            ) : (
              <div>
                <div className="info">
                  <h2 className="location">
                    <i className="fas fa-street-view"></i>The current weather in {search} is
                  </h2>
                  <h1 className="temp">
                    Low: {city.temp_min} °F | High: {city.temp_max} °F
                  </h1>
                  <h3 className="tempmin_max">Current: {city.temp} °F</h3>
                </div>
                <div className="wave- one"></div>
                <div className="wave- two"></div>
                <div className="wave- three"></div>
                <div id="clouds">
                  <div className="cloud x1"></div>
                  <div className="cloud x2"></div>
                  <div className="cloud x3"></div>
                  <div className="cloud x4"></div>
                  <div className="cloud x5"></div>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
}

export default WeatherApi;
