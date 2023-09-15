import React, { useState, useEffect } from "react";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import jwtDecode from "jwt-decode";

const FriendRequest = () => {
  const { token } = useAuthContext();
  const [recipient, setRecipient] = useState(null);
  const [userId, setUserId] = useState(null);
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState([]);

  useEffect(() => {
    if (token) {
      try {
        const decodedToken = jwtDecode(token);
        const userId = parseInt(decodedToken.sub, 10);
        setUserId(userId);
      } catch (error) {
        console.error("Error decoding token:", error.message);
      }
    }
  }, [token]);

  const handleSearch = async () => {
    if (!searchQuery) {
      return;
    }

    try {
      const response = await fetch(
        `${process.env.REACT_APP_API_HOST}/users/${searchQuery}`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
          },
          credentials: "include",
        }
      );

      if (response.ok) {
        const userData = await response.json();
        setSearchResults(userData ? [userData] : []);
      } else {
        console.error(response);
        setSearchResults([]);
      }
    } catch (error) {
      console.error(error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!recipient) {
      console.error("Recipient not selected");
      return;
    }

    const newFriend = {
      sender_id: userId,
      receiver_id: parseInt(recipient.id, 10),
      username: recipient.username,
    };

    const friendsListUrl = `${process.env.REACT_APP_API_HOST}/friends`;
    const fetchConfig = {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify(newFriend),
    };

    try {
      const response = await fetch(friendsListUrl, fetchConfig);

      if (response.ok) {
        setSearchQuery("");
        setRecipient(null);
        setSearchResults([]);
        console.log("Friend Request Sent!");
      } else {
        console.error(response);
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div style={{ paddingLeft: '20px' }}>
      <h2>Send Friend Request</h2>
      <div>
        <label htmlFor="searchQuery">Recipient:</label>
        <div className="input-group">
          <input
            id="searchQuery"
            type="text"
            className="form-control"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search by username, email, or ID"
            required
          />
          <button type="button" className="btn btn-info" onClick={handleSearch}>
            Search
          </button>
        </div>
      </div>
      {searchResults.length > 0 && (
        <div>
          <p>Search Results:</p>
          <ul>
            {searchResults.map((user) => (
              <li
                key={user.id}
                onClick={() => setRecipient(user)}
                style={{ cursor: "pointer" }}
              >
                {`${user.first_name} ${user.last_name}`}
              </li>
            ))}
          </ul>
        </div>
      )}
      {recipient && (
        <div>
          <p>Selected Recipient:</p>
          <p>Full Name: {`${recipient.first_name} ${recipient.last_name}`}</p>
        </div>
      )}
      <button type="submit" className="btn btn-info" onClick={handleSubmit}>
        Send Request
      </button>
    </div>
  );
};

export default FriendRequest;
