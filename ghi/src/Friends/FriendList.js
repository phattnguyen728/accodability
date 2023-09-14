import React, { useState, useEffect } from "react";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import jwtDecode from "jwt-decode";
// import "./Friends.css";

function FriendList() {
  const { token } = useAuthContext();
  const [friends, setFriends] = useState([]);
  const [userId, setUserId] = useState(null);
  const [userProfiles, setUserProfiles] = useState({});

  const handleApprove = async (sender_id, friendRequestId) => {
    const updateFriend = {
      sender_id: parseInt(sender_id, 10),
      receiver_id: userId,
    };
    const acceptUrl = `${process.env.REACT_APP_API_HOST}/friends/${friendRequestId}`;
    const fetchConfig = {
      method: "put",
      headers: {
        Authentication: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
      credentials: "include",
      body: JSON.stringify(updateFriend),
    };

    const response = await fetch(acceptUrl, fetchConfig);
    if (response.ok) {
      const fetchConfig = {
        method: "get",
        headers: {
          Authentication: `Bearer ${token}`,
        },
        credentials: "include",
      };
      const url = `${process.env.REACT_APP_API_HOST}/friends`;
      const response = await fetch(url, fetchConfig);

      if (response.ok) {
        const data = await response.json();

        setFriends(data);
      } else {
        console.error(response);
      }
    }
  };
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
  }, [token, friends]);

  useEffect(() => {
    const fetchFriends = async () => {
      const fetchConfig = {
        method: "get",
        headers: {
          Authentication: `Bearer ${token}`,
        },
        credentials: "include",
      };
      const url = `${process.env.REACT_APP_API_HOST}/friends`;
      const response = await fetch(url, fetchConfig);
      if (response.ok) {
        const data = await response.json();
        setFriends(data);
      } else {
        console.error(response);
      }
    };

    fetchFriends();
  }, [token]);

  useEffect(() => {
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
    friends.forEach((friend) => {
      const senderId = friend.sender_id;
      fetchUserProfile(senderId);
    });
  }, [friends, token]);

  return (
    <div>
      <h2>Friend List</h2>
      {friends.length === 0 ? (
        <p>No friends yet.</p>
      ) : (
        <table className="table table-striped table-bordered table-hover caption-top custom-table">
          <thead>
            <tr className="table-info">
              <th style={{ width: "20%" }}>Sender ID</th>
              <th style={{ width: "30%" }}>Username</th>
              <th style={{ width: "30%" }}>Status</th>
              <th style={{ width: "20%" }}> </th>
            </tr>
          </thead>
          <tbody>
            {friends.map((friend) => {
              return (
                <tr key={friend.id}>
                  <td>{friend.sender_id}</td>
                  <td>{userProfiles[friend.sender_id]?.username}</td>
                  <td>{friend.status}</td>
                  <td
                    className={
                      friend.status === "pending" ? "" : "hidden-button"
                    }
                  >
                    {friend.status === "pending" ? (
                      <button
                        name="approve"
                        className="btn btn-info"
                        onClick={() => {
                          handleApprove(`${friend.sender_id}`, friend.id);
                        }}
                      >
                        Approve
                      </button>
                    ) : null}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default FriendList;
