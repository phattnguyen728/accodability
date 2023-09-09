import React, { useState } from "react";

function ServiceHistory(props) {
  const [typeVin, setTypeVin] = useState("");
  const [searchVin, setSearchVin] = useState("");
  const [postData, setpostData] = useState([]);
  const [commentData, setCommentDAta] = useState([]);

  function handleTypeVinChange(event) {
    const { value } = event.target;
    setTypeVin(value);
    setSearchVin("");
  }

  let appointments = [];

  if (searchVin !== "") {
    appointments = props.appts.filter((appt) => appt.vin == searchVin);
  }
  if (typeVin == "" || searchVin == "") {
    appointments = props.appts;
  }

  return (
    <div className="container-fluid">
      <h1>Service History</h1>
      <div className="input-group mb-3">
        <input
          onChange={handleTypeVinChange}
          value={typeVin}
          type="text"
          className="form-control"
          placeholder="Search by VIN..."
          aria-label="Search by VIN..."
          aria-describedby="button-addon2"
        />
        <button
          className="btn btn-outline-secondary"
          onClick={(event) => setSearchVin(event.target.value)}
          value={typeVin}
          type="button"
          id="button-addon2"
        >
          Search
        </button>
      </div>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>VIN</th>
            <th>Is VIP?</th>
            <th>Customer</th>
            <th>Date</th>
            <th>Time</th>
            <th>Technician</th>
            <th>Reason</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {appointments.map((appt) => {
            return (
              <tr key={appt.id}>
                <td>{appt.vin}</td>
                <td>{appt.vip}</td>
                <td>{appt.customer}</td>
                <td>{appt.date}</td>
                <td>{appt.time}</td>
                <td>
                  {appt.technician.first_name} {appt.technician.last_name}
                </td>
                <td>{appt.reason}</td>
                <td>{appt.status}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default ServiceHistory;
