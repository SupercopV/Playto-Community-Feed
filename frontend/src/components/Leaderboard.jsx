import { useEffect, useState } from "react";
import { fetchLeaderboard } from "../api/leaderboard";

export default function Leaderboard() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetchLeaderboard().then(res => setUsers(res.data));
  }, []);

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="font-bold mb-2">🏆 Leaderboard (24h)</h2>

      {users.length === 0 && (
        <p className="text-sm text-gray-500">No activity yet</p>
      )}

      {users.map(user => (
        <div
          key={user.user_id}
          className="flex justify-between text-sm mb-1"
        >
          <span>{user.username}</span>
          <span>{user.total_karma}</span>
        </div>
      ))}
    </div>
  );
}
