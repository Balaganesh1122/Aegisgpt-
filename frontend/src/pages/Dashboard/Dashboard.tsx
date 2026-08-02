import { useState } from "react";

import DashboardLayout from "@/components/layout/DashboardLayout";
import ChatLayout from "@/components/chat/ChatLayout";
import UploadPanel from "@/components/upload/UploadPanel";

export default function Dashboard() {
  const [showUpload, setShowUpload] = useState(false);

  return (
    <>
      <DashboardLayout
        onUpload={() => setShowUpload(true)}
      >
        <ChatLayout />
      </DashboardLayout>

      {showUpload && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70">
          <div className="relative w-full max-w-3xl rounded-2xl bg-slate-950 p-6">
            <button
              onClick={() => setShowUpload(false)}
              className="absolute right-4 top-4 rounded-lg bg-red-600 px-3 py-1 text-white"
            >
              ✕
            </button>

            <UploadPanel
                onSuccess={() => setShowUpload(false)}
            />
          </div>
        </div>
      )}
    </>
  );
}