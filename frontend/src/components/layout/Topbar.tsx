import { Search, UserCircle2, LogOut } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { logout } from "@/services/auth.service";

export default function Topbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login", { replace: true });
  };

  return (
    <header className="flex h-16 items-center justify-between border-b border-slate-800 bg-slate-900 px-6">
      <div className="relative w-80">
        <Search
          size={18}
          className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"
        />

        <input
          placeholder="Search documents..."
          className="w-full rounded-lg border border-slate-700 bg-slate-800 py-2 pl-10 pr-4 text-white outline-none focus:border-violet-500"
        />
      </div>

      <div className="flex items-center gap-6">
        <div className="flex items-center gap-3">
          <UserCircle2
            size={34}
            className="text-violet-400"
          />

          <div>
            <p className="font-medium">Bala Ganesh</p>
            <p className="text-sm text-slate-400">
              Administrator
            </p>
          </div>
        </div>

        <button
          onClick={handleLogout}
          className="flex items-center gap-2 rounded-lg bg-red-600 px-4 py-2 text-white transition hover:bg-red-500"
        >
          <LogOut size={18} />
          Logout
        </button>
      </div>
    </header>
  );
}