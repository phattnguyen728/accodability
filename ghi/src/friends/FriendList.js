import React, { useState, useEffect } from "react";
import { useAuthContext, useToken } from "@galvanize-inc/jwtdown-for-react";

function FriendList() {
  const { token } = useAuthContext();
  const [friends, setFriends] = useState([]);
  // const [search, setSearch] = useState("");
  // const [users, setUsers] = useState([]);

  const fetchFriends = async () => {
    const fetchConfig = {
      method: "get",
      headers: {
        Authentication: `Bearer ${token}`,
      },
      credentials: "include",
    };
    const url = `${process.env.REACT_APP_API_HOST}/friends`;
    console.log(token);
    console.log(fetchConfig);
    console.log(url);
    const response = await fetch(url, fetchConfig);
    console.log(response);
    if (response.ok) {
      const data = await response.json();

      setFriends(data);
    } else {
      console.error(response);
    }
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
              <th>Friends</th>
            </tr>
          </thead>
          <tbody>
            {friends.map((friend) => {
              return (
                <tr key={friend.id}>
                  <td>{friend.sender_id}</td>
                  <td>{friend.username}</td>
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
