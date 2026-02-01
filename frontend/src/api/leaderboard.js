import api from "./client";

export const fetchLeaderboard = () => api.get("leaderboard/");
