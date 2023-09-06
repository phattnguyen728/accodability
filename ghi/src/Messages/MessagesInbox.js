import React, { useState, useEffect } from "react";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import UserProfile from "../Components/GetUser";

export default function MessageInbox() {
  const { token } = useAuthContext();
  const [messages, setMessages] = useState([]);
  const [userProfiles, setUserProfiles] = useState({});

  const fetchMessages = async () => {
    const fetchConfig = {
      method: "get",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      credentials: "include",
    };
    const url = `${process.env.REACT_APP_API_HOST}/messages`;

    const response = await fetch(url, fetchConfig);

    if (response.ok) {
      const data = await response.json();
      setMessages(data["Message Inbox"]);
    } else {
      console.error(response);
    }
  };

  const fetchUserProfile = async (senderId) => {
    const fetchConfig = {
      method: "get",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      credentials: "include",
    };
    const url = `${process.env.REACT_APP_API_HOST}/users/${senderId}`;

    const response = await fetch(url, fetchConfig);

    if (response.ok) {
      const userProfile = await response.json();
      setUserProfiles((currentProfiles) => {
        const updatedProfiles = { ...currentProfiles };
        updatedProfiles[senderId] = userProfile;
        return updatedProfiles;
      });
    } else {
      console.error(response);
    }
  };

  useEffect(() => {
    fetchMessages();
  }, [token]);

  useEffect(() => {
    messages.forEach((message) => {
      const senderId = message.sender_id;
      fetchUserProfile(senderId);
    });
  }, [messages]);

  return (
    <div>
      <h2>Message Inbox</h2>
      {messages.length === 0 ? (
        <p>No messages yet.</p>
      ) : (
        <table className="table table-dark table-hover table-striped">
          <thead>
            <tr>
              <th>Sender ID</th>
              <th>Message Content</th>
              <th>From Username</th>
              <th>Email</th>
              <th>FullName</th>
            </tr>
          </thead>
          <tbody>
            {messages.map((message, index) => (
              <tr key={index}>
                <td>{message.sender_id}</td>
                <td>{message.message_content}</td>
                <td>{userProfiles[message.sender_id]?.username}</td>
                <td>{userProfiles[message.sender_id]?.email}</td>
                <td>
                  {userProfiles[message.sender_id]
                    ? `${userProfiles[message.sender_id].first_name} ${
                        userProfiles[message.sender_id].last_name
                      }`
                    : ""}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
