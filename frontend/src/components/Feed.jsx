import { useEffect, useState } from "react";
import { fetchFeed } from "../api/feed";
import PostCard from "./PostCard";

export default function Feed() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetchFeed()
      .then(res => {
        console.log("FEED RESPONSE:", res.data);
        setPosts(res.data);
      })
      .catch(err => {
        console.error("FEED ERROR:", err);
      });
  }, []);

  if (posts.length === 0) {
    return <p className="text-gray-500">No posts yet</p>;
  }

  return (
    <div>
      {posts.map(post => (
        <PostCard key={post.id} post={post} />
      ))}
    </div>
  );
}


