import React, { useState, useEffect } from "react";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";

function FriendList() {
  const { token } = useAuthContext();
  const [friends, setFriends] = useState([]);
  const [search, setSearch] = useState("");
  const [users, setUsers] = useState([]);

  const fetchFriends = async () => {
    const response = await fetch("http://localhost:8000/friends/", {
      headers: { Authentication: `Bearer ${token}` },
    })
      .then((resp) => resp.json(), setFriends(data))
      .catch((error) => console.error(error));
    // if (response.ok) {
    //   const data = await response.json();

    //   setFriends(data.friends);
    //   //   setFriends(data.pending_requests)
    //   // need to know what this is ^ called on routers/friends.py
    //   // what is returned in the json body
    //   //   setFriends([]);
    // } else {
    //   console.error(response);
    //   // "Error, could not send friend request."
    // }
  };

  const handleSearch = async (event) => {
    const value = event.target.value;
    setSearch(value);
  };

  const fetchUsers = async () => {
    const response = await fetch("http://localhost:8000/users/", {
      method: "GET",
    });
    if (response.ok) {
      const data = await response.json();
      //   setUsers(data.something);
    }
  };
  const searchSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch("http://localhost:8000/users/");
    // console.log(response);
    if (response.ok) {
      const data = await response.json();
      let search_list = [];
      // x == singular apointment objects in appointmentsJSON: data.appointments
      for (let x of data[0]) {
        // if the vin matches the search term add that term to the search list
        if (x.username === search) {
          search_list.push(x);
        }
        // if the search term has letters or numbers refresh the view state to just those with the search term
        if (search != "") {
          setUsers(search_list);
        }
        // else if the search bar is blank just render teh whole list. Eliminates need to refresh for
        // the page to see everything again
        else {
          fetchUsers();
          // return true;
        }
      }
    }
  };
  useEffect(() => {
    fetchFriends();
    fetchUsers();
  }, []);

  const deleteFriend = async (id) => {
    const friendUrl = `http://localhost:8000/friends/`;
    const response = await fetch(friendUrl, { method: "DELETE" }).then(() => {
      fetchFriends();
    });
  };

  return (
    <div className="my-5 container">
      <div className="form-floating mb-3">
        <form onSubmit={searchSubmit} id="search-vin-form">
          <input
            value={search}
            onChange={handleSearch}
            placeholder="Search Users"
            type="text"
            id="search"
            name="search"
            className="form-control"
          />
          <label htmlFor="search"></label>
          <button className="btn btn-md btn-primary">Search Users</button>
        </form>
      </div>
      <table className="table table-dark table-hover table-striped">
        <thead>
          <tr>
            <th>Friends</th>
          </tr>
        </thead>
        <tbody>
          {friends.map((friend) => {
            return (
              <tr key={friend.sender_id}>
                <td>{friend.username}</td>
                <td>
                  <button
                    className="btn btn-danger"
                    onClick={() => {
                      deleteFriend(friend.sender_id);
                    }}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
export default FriendList;

<ul>
  {friends.map((sender_id) => (
    <li key={sender_id}>Friend ID: {sender_id}</li>
  ))}
</ul>;

// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import { useAuthContext, useToken } from "@galvanize-inc/jwtdown-for-react";
// // import

// function FriendList() {
//   const { token } = useAuthContext();
//   const [friends, setFriends] = useState([]);
//   // const [search, setSearch] = useState("");
//   // const [users, setUsers] = useState([]);

//   const fetchOptions = {
//     method: 'get',
//     body: JSON.stringify(data),
//     headers:{
//       'Content-Type': 'application/json',
//     };
//   };

//   const fetchFriends = async () => {
//     // const headers = { Authorization: token };
//     // const response = await fetch("http://localhost:8000/friends", {
//     //   headers: { access_token: `${token}` },
//       // headers: { access_token: token },
//       // headers: { Authentication: `${token}` },
//     const response = await fetch('http:/localhost:8000/friends', fetchOptions);
//     };
//     if (response.ok) {
//       const data = await response.json();

//       setFriends(data);
//     } else {
//       console.error(response);
//     }
//   };
//   useEffect(() => {
//     if (token) {
//       fetchFriends();
//     }
//   }, []);

//   // const [friends, setFriends] = useState([]);

//   // useEffect(() => {
//   //   const headers = { Authorization: `${token}` };
//   //   fetch("https://localhost:8000/friends", { headers })
//   //     .then((response) => response.json())
//   //     .then((data) => setFriends(data))
//   //     .catch((error) => console.error(error));

//   // }, []);
//   return (
//     <div>
//       <h2>Friend List</h2>
//       {friends.length === 0 ? (
//         <p>No friends yet.</p>
//       ) : (
//         <table className="table table-dark table-hover table-striped">
//           <thead>
//             <tr>
//               <th>Friends</th>
//             </tr>
//           </thead>
//           <tbody>
//             {friends.map((friend) => {
//               return (
//                 <tr key={friend.sender_id}>
//                   <td>{friend.username}</td>
//                 </tr>
//               );
//             })}
//           </tbody>
//         </table>
//       )}
//     </div>
//   );
// }

// export default FriendList;
