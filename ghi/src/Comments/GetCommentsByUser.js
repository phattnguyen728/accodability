import React, { useState, useEffect } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";

function GetCommentsByUser() {
  const [userData, setUserData] = useState("");
  const [userName, setUserName] = useState("");
  const [commentData, setCommentData] = useState([]);
  const { token } = useToken();

  async function getCommentDataRefresh() {
    let userDataId = userData;
    const url = `${process.env.REACT_APP_API_HOST}/api/users/${userDataId}/comments/`;
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    if (response.ok) {
      const data = await response.json();
      setCommentData(data);
    } else {
      console.error("An error occurred fetching post data");
    }
  }

  async function deleteComment(event) {
    const data = event.target.value;
    const array = data.split(",");
    const postId = parseInt(array[0]);
    const id = parseInt(array[1]);
    const url = `${process.env.REACT_APP_API_HOST}/api/posts/${postId}/comments/${id}`;
    const response = await fetch(url, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    if (response.ok) {
      getCommentDataRefresh();
    } else {
      console.error("An error occurred deleting this comment");
    }
  }

  useEffect(() => {
    async function getUserData() {
      const url = `${process.env.REACT_APP_API_HOST}/currentuser`;
      const response = await fetch(url, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      if (response.ok) {
        const data = await response.json();
        setUserData(data.id);
        setUserName(data.username);
      } else {
        console.log("An error occurred fetching logged-in user data");
      }
    }
    async function getCommentData(userData) {
      const url = `${process.env.REACT_APP_API_HOST}/api/users/${userData}/comments/`;
      const response = await fetch(url, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      if (response.ok) {
        const data = await response.json();
        setCommentData(data);
      } else {
        console.error("An error occurred fetching post data");
      }
    }
    if (token) {
      getUserData();
      getCommentData();
    }
  }, [token]);

  return (
    <div className="container-fluid">
      <h1>{userName}'s Comments</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Post ID</th>
            <th>Comment</th>
            <th>Created At</th>
            <th>Delete?</th>
          </tr>
        </thead>
        <tbody>
          {commentData.map((comment) => {
            return (
              <tr key={comment.id}>
                <td>{comment.post_id}</td>
                <td>{comment.body}</td>
                <td>{comment.created_at}</td>
                <td>
                  <button
                    onClick={deleteComment}
                    className="btn btn-danger"
                    value={[comment.post_id, comment.id]}
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

export default GetCommentsByUser;
