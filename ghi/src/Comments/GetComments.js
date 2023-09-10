import React, { useState, useEffect } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";

function GetComments() {
  const [postData, setPostData] = useState([]);
  const [commentData, setCommentData] = useState([]);
  const [typePost, setTypePost] = useState("");
  const [searchPost, setSearchPost] = useState("");
  const [post, setPost] = useState("");
  const { token } = useToken();

  let successMessage = document.getElementById("search-success");
  let searchResults = document.getElementById("search-results");

  function handleTypePostChange(event) {
    const { value } = event.target;
    setTypePost(value);
    setSearchPost("");
    setPost("");
    setCommentData([]);
    if (successMessage) {
      successMessage.classList.add("d-none");
    }
    if (searchResults) {
      searchResults.classList.add("d-none");
    }
  }

  async function getCommentData(post) {
    if (!post) {
      setCommentData([]);
    }
    const url = `${process.env.REACT_APP_API_HOST}/api/posts/${post}/comments`;
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
      console.log("An error occurred fetching comment data");
    }
  }

  let posts = [];

  if (searchPost !== "") {
    posts = postData.filter(
      (post) => post.title.toLowerCase().search(searchPost.toLowerCase()) !== -1
    );
  }
  if (typePost === "" || searchPost === "") {
    posts = [];
  }

  useEffect(() => {
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
    if (token) {
      getPostData();
    }
  }, [token]);

  return (
    <div className="container-fluid">
      <h1>Search for Comments</h1>
      <div className="input-group mb-3">
        <input
          onChange={handleTypePostChange}
          value={typePost}
          type="text"
          className="form-control"
          placeholder="Search by Post title..."
          aria-label="Search by Post title..."
          aria-describedby="button-addon2"
        />
        <button
          className="btn btn-outline-secondary"
          onClick={(event) => {
            setSearchPost(event.target.value);
            if (successMessage) {
              successMessage.classList.remove("d-none");
            }
            if (searchResults) {
              searchResults.classList.remove("d-none");
            }
          }}
          value={typePost}
          type="button"
          id="button-addon2"
        >
          Search
        </button>
      </div>
      <div
        className="alert alert-success alert-dismissible d-none fade show"
        role="alert"
        id="search-success"
      >
        <strong>Success:</strong> Your search results are below.
      </div>
      <div className="mb-3 d-none" id="search-results">
        <select
          onChange={(event) => {
            setPost(event.target.value);
            getCommentData(event.target.value);
          }}
          value={post}
          required
          className="form-select"
          id="post"
        >
          <option value="">Your search results...</option>
          {posts.map((post_search) => {
            return (
              <option key={post_search.id} value={post_search.id}>
                {post_search.title}
              </option>
            );
          })}
        </select>
      </div>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Author ID</th>
            <th>Comment</th>
            <th>Date Created</th>
          </tr>
        </thead>
        <tbody>
          {commentData.map((comment) => {
            return (
              <tr key={comment.id}>
                <td>{comment.author_id}</td>
                <td>{comment.body}</td>
                <td>{comment.created_at}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default GetComments;
