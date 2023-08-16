import React, { useState } from "react";
// import

const FriendRequest = ({ userID }) => {
  const [friendId, setFriendId] = useState("");
  const [message, setMessage] = useState("");
  const [friendsList, setFriendsList] = useState([]);
  //do we need to grab friends list from database?

  // method:POST
  //     const handleSendFriendRequest = async () => {
  //         try{
  //             const url = 'http://localhost8000:/api/friendsList';
  //             const response = await fetch(url);
  //             if (response.ok){
  //                 const data = await response.json();
  //                 setFriendsList(data.friendsList)
  //                 // need to finalize parameter for friendslist
  //             }
  //         }
  //         catch(error){
  //            console.error('Error: could not send friend request', error);
  //            setMessage(' error sending friend request)
  //         }
  //     }
  // }
  const handleSendFriendRequest = async (event) => {
    event.preventDefault();
    const data = {};
    data.friendsList = friendsList;
    const friendsListUrl = "http://localhost:8000/api/friendsList/";
    const fetchConfig = {
      method: "POST",
      //   body: JSON.stringify(data),

      body: JSON.stringify({
        user_id: userId,
        friend_id: friendId,
      }),

      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(friendsListUrl, fetchConfig);
    if (response.ok) {
      const friendsList = await response.json();
      setFriendsList([]);
      setMessage("Friend Request Sent!");
    } else {
      console.error(response);
      setMessage("Error, could not send friend request.");
    }
  };

  return (
    <div>
      <h2>Send Friend Request</h2>
      <input
        type="number"
        placeholder="Friend's User ID"
        value={friendId}
        onChange={(e) => setFriendId(e.target.value)}
      />
      <button onClick={handleSendRequest}>Send Request</button>
      <p>{message}</p>
    </div>
  );
};
export default FriendRequest;
