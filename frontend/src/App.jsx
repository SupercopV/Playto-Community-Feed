import Feed from "./components/Feed";
import Leaderboard from "./components/Leaderboard";

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-6 flex gap-6">
      
      {/* FEED */}
      <div className="w-2/3">
        <h1 className="text-xl font-bold mb-4">Community Feed</h1>
        <Feed />
      </div>

      {/* LEADERBOARD */}
      <div className="w-1/3">
        <Leaderboard />
      </div>

    </div>
  );
}



