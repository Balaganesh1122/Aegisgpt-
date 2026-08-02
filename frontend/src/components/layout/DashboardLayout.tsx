import type { ReactNode } from "react";

import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

interface DashboardLayoutProps {
  children: ReactNode;
  onUpload: () => void;
}

export default function DashboardLayout({
  children,
  onUpload,
}: DashboardLayoutProps) {
  return (
    <div className="flex h-screen bg-slate-950 text-white">
      <Sidebar onUpload={onUpload} />

      <div className="flex flex-1 flex-col">
        <Topbar />

        <main className="flex-1 overflow-auto p-6">
          {children}
        </main>
      </div>
    </div>
  );
}