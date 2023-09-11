import React, { useState, useEffect } from "react";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import jwtDecode from "jwt-decode";

export default function CreatePostForm() {
  const { token } = useAuthContext();
  const [postContent, setPostContent] = useState("");
  const [userId, setUserId] = useState(null);
  const [postTitle, setPostTitle] = useState("");
  const [postHyperlink, setPostHyperlink] = useState("");

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

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!postContent) {
      console.error("Post content cannot be empty");
      return;
    }

    const newPost = {
        author_id: userId,
        title: postTitle,
        body: postContent,
        hyperlink: postHyperlink,
    };
    console.log(JSON.stringify(newPost));

    try {
      const response = await fetch(
        `${process.env.REACT_APP_API_HOST}/api/posts`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(newPost),
        }
      );

      if (response.ok) {
        console.log("Post created successfully");
        setPostTitle("");
        setPostHyperlink("");
        setPostContent("");
      } else {
        console.error(response);
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Create a Post</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="postTitle">Post Title:</label>
          <textarea
            id="postTitle"
            className="form-control"
            value={postTitle}
            onChange={(e) => setPostTitle(e.target.value)}
            placeholder="Write your title here"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="postHyperlink">Post Hyperlink:</label>
          <textarea
            id="postHyperlink"
            className="form-control"
            value={postHyperlink}
            onChange={(e) => setPostHyperlink(e.target.value)}
            placeholder="Add a hyperlink"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="postContent">Post Content:</label>
          <textarea
            id="postContent"
            className="form-control"
            value={postContent}
            onChange={(e) => setPostContent(e.target.value)}
            placeholder="Write your post here"
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Create Post
        </button>
      </form>
    </div>
  );
}
