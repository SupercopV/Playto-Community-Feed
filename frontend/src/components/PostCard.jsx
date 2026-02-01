import { likePost } from "../api/feed";

export default function PostCard({ post }) {
  const handleLike = async () => {
    await likePost(post.id);
    alert("Post liked!");
  };

  return (
    <div className="bg-white p-4 rounded shadow mb-4">
      <p className="font-semibold">{post.author}</p>
      <p className="mb-2">{post.content}</p>

      {/* LIKE BUTTON */}
      <button
        onClick={handleLike}
        className="text-sm text-blue-600 hover:underline"
      >
        ❤️ Like
      </button>

      {/* COMMENTS */}
      <div className="ml-4 mt-2">
        {post.comments.map(comment => (
          <div key={comment.id} className="text-sm mt-1">
            <b>{comment.author}</b>: {comment.content}
          </div>
        ))}
      </div>
    </div>
  );
}


