import React, { useState, useEffect } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";

function CommentForm() {
  const [userData, setUserData] = useState("");
  const [postData, setPostData] = useState([]);
  const [post, setPost] = useState("");
  const [comment, setComment] = useState("");
  const { token } = useToken();

  function handleCommentChange(event) {
    const { value } = event.target;
    setComment(value);
    let successMessage = document.getElementById("create-success");
    successMessage = successMessage.classList.add("d-none");
  }

  function handlePostChange(event) {
    const { value } = event.target;
    setPost(value);
    let successMessage = document.getElementById("create-success");
    successMessage = successMessage.classList.add("d-none");
  }

  async function getPostData() {
    const url = `${process.env.REACT_APP_API_HOST}/api/posts`;
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    if (response.ok) {
      const data = await response.json();
      setPostData(data);
    } else {
      console.error("An error occurred fetching post data");
    }
  }

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
    } else {
      console.log("An error occurred fetching logged-in user data");
    }
  }

  useEffect(() => {
    getPostData();
    getUserData();
  }, [token]);

  async function handleSubmit(event) {
    event.preventDefault();
    const data = {
      author_id: userData,
      post_id: post,
      body: comment,
    };

    const locationUrl = `${process.env.REACT_APP_API_HOST}/api/posts/${post}/comments`;
    const fetchConfig = {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(locationUrl, fetchConfig);
    if (response.ok) {
      const newComment = await response.json();
      console.log(newComment);
      setPost("");
      setComment("");
      let successMessage = document.getElementById("create-success");
      successMessage = successMessage.classList.remove("d-none");
    }
  }

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Create New Comment</h1>
          <form onSubmit={handleSubmit} id="new-comment-form">
            <div className="mb-3">
              <select
                onChange={handlePostChange}
                value={post}
                required
                className="form-select"
                id="post"
              >
                <option value="">Choose a post...</option>
                {postData.map((post) => {
                  return (
                    <option key={post.id} value={post.id}>
                      {post.title}
                    </option>
                  );
                })}
              </select>
            </div>
            <div className="form-floating mb-3">
              <input
                onChange={handleCommentChange}
                value={comment}
                required
                type="text"
                id="comment"
                className="form-control"
              />
              <label htmlFor="comment" className="form-label">
                Comment
              </label>
            </div>
            <button className="btn btn-primary">Create Comment</button>
          </form>
          <div
            className="alert alert-success alert-dismissible d-none fade show"
            role="alert"
            id="create-success"
          >
            <strong>Success:</strong> A new comment has been created.
          </div>
        </div>
      </div>
    </div>
  );
}
export default CommentForm;
