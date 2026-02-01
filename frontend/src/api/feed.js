import api from "./client";

export const fetchFeed = () => api.get("feed/");
export const likePost = (postId) => api.post(`posts/${postId}/like/`);
