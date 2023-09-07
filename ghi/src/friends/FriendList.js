import React, { useState, useEffect } from "react";
import { useAuthContext, useToken } from "@galvanize-inc/jwtdown-for-react";
import jwtDecode from "jwt-decode";

function FriendList() {
  const { token } = useAuthContext();
  const [friends, setFriends] = useState([]);
  const [userId, setUserId] = useState(null);

  // const [search, setSearch] = useState("");
  // const [users, setUsers] = useState([]);

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
    console.log(response);
    if (response.ok) {
      const data = await response.json();

      setFriends(data);
    } else {
      console.error(response);
    }
  };

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
    const response = await fetch(acceptUrl, fetchConfig).then(() => {
      fetchFriends();
      // console.log(response);
    });
  };
  useEffect(() => {
    fetchFriends();
  }, [token]);

  return (
    <div>
      <h2>Friend List</h2>
      {friends.length === 0 ? (
        <p>No friends yet.</p>
      ) : (
        <table className="table table-dark table-hover table-striped">
          <thead>
            <tr>
              <th>user_id</th>
              <th>username</th>
              <th>status</th>
            </tr>
          </thead>
          <tbody>
            {friends.map((friend) => {
              return (
                <tr key={friend.id}>
                  <td>{friend.sender_id}</td>
                  <td>{friend.username}</td>
                  <td>{friend.status}</td>
                  {friend.status === "pending" && (
                    <td>
                      <button
                        name="approve"
                        className="btn btn-success"
                        onClick={() => {
                          handleApprove(`${friend.sender_id}`, friend.id);
                        }}
                      >
                        Approve
                      </button>
                    </td>
                  )}
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
