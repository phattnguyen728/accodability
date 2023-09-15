import React, { useState, useEffect } from "react";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import jwtDecode from "jwt-decode";

export default function MessageForm() {
  const { token } = useAuthContext();
  const [recipient, setRecipient] = useState(null);
  const [searchQuery, setSearchQuery] = useState("");
  const [messageContent, setMessageContent] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [userId, setUserId] = useState(null);

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

    const recipientId = parseInt(recipient.id, 10);
    const newMessage = {
      sender_id: userId,
      receiver_id: recipientId,
      message_content: messageContent,
    };
    console.log(JSON.stringify(newMessage));

    try {
      const response = await fetch(
        `${process.env.REACT_APP_API_HOST}/messages`,
        {
          method: "post",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(newMessage),
        }
      );

      if (response.ok) {
        console.log("Message sent successfully");
        setSearchQuery("");
        setRecipient(null);
        setMessageContent("");
      } else {
        console.error(response);
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div style={{ paddingLeft: '20px' }}>
      <h2>Send a Message</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
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
            <button
              type="button"
              className="btn btn-info"
              onClick={handleSearch}
            >
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
        <div className="form-group">
          <label htmlFor="messageContent">Message Content:</label>
          <textarea
            id="messageContent"
            className="form-control"
            value={messageContent}
            onChange={(e) => setMessageContent(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="btn btn-info">
          Send Message
        </button>
      </form>
    </div>
  );
}
