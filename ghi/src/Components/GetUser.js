import React, { useState, useEffect } from "react";

export default function UserProfile({ usernameEmailOrId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {

    const fetchUser = async () => {
      try {
        const response = await fetch(
          `${process.env.REACT_APP_API_HOST}/users/${usernameEmailOrId}`
        );

        if (response.ok) {
          const userData = await response.json();
          setUser(userData);
        } else {
          console.error(response);
        }
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };


    fetchUser();
  }, [usernameEmailOrId]);

  if (loading) {
    return <p>Loading user data...</p>;
  }

  if (!user) {
    return <p>User not found</p>;
  }


  return (
    <div>
      <h2>User Profile</h2>
      <p>ID: {user.id}</p>
      <p>First Name: {user.first_name}</p>
      <p>Last Name: {user.last_name}</p>
      <p>Username: {user.username}</p>
      <p>Email: {user.email}</p>
    </div>
  );
}
