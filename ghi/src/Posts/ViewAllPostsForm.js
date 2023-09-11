import React, { useState, useEffect } from "react";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import jwtDecode from "jwt-decode";

export default function GetPostsForm() {
  const { token } = useAuthContext();
  const [postData, setPostData] = useState([]);
  const [searchPost, setSearchPost] = useState("");
  const [selectedPost, setSelectedPost] = useState("");
  const [comments, setComments] = useState([]);
  const [userId, setUserId] = useState(null);

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
  }, [token, userId]);

  useEffect(() => {
    async function fetchPosts() {
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
      fetchPosts();
    }
  }, [token]);

  useEffect(() => {
    async function fetchCommentsForSelectedPost(selectedPostId) {
      if (!selectedPostId) {
        setComments([]);
        return;
      }

      const url = `${process.env.REACT_APP_API_HOST}/api/posts/${selectedPostId}/comments`;
      const response = await fetch(url, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setComments(data);
      } else {
        console.error("An error occurred fetching comment data");
      }
    }

    fetchCommentsForSelectedPost(selectedPost);
  }, [selectedPost, token]);

  return (
    <div className="container-fluid">
      <h1>Search for Posts</h1>
      <div className="input-group mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Search by Post title..."
          value={searchPost}
          onChange={(e) => setSearchPost(e.target.value)}
        />
        <button
          className="btn btn-outline-secondary"
          type="button"
          onClick={() => setSelectedPost("")}
        >
          Clear
        </button>
        <button
          className="btn btn-outline-secondary"
          type="button"
          onClick={() => {
            setSelectedPost("");
            setSearchPost(searchPost);
          }}
        >
          Search
        </button>
      </div>
      <div className="mb-3">
        <select
          className="form-select"
          value={selectedPost}
          onChange={(e) => setSelectedPost(e.target.value)}
        >
          <option value="">Select a Post...</option>
          {postData.map((post) => (
            <option key={post.id} value={post.id}>
              {post.title}
            </option>
          ))}
        </select>
      </div>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Post Title</th>
            <th>Post Content</th>
          </tr>
        </thead>
        <tbody>
          {comments.map((comment) => (
            <tr key={comment.id}>
              <td>{comment.title}</td>
              <td>{comment.body}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
