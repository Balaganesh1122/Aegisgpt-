import { MessageSquarePlus, Upload } from "lucide-react";

import ConversationList from "@/components/sidebar/ConversationList";
import DocumentsList from "@/components/sidebar/DocumentsList";
import { useChatContext } from "@/context/ChatContext";

interface SidebarProps {
  onUpload: () => void;
}

export default function Sidebar({
  onUpload,
}: SidebarProps) {
  const {
    setMessages,
    setConversationId,
  } = useChatContext();

  const handleNewChat = () => {
    setMessages([]);
    setConversationId(undefined);
  };

  return (
    <aside className="flex w-72 flex-col border-r border-slate-800 bg-slate-900">
      <div className="border-b border-slate-800 p-6">
        <h1 className="text-2xl font-bold text-violet-400">
          🛡️ AegisGPT
        </h1>

        <p className="mt-2 text-sm text-slate-400">
          AI Document Assistant
        </p>
      </div>

      <div className="space-y-3 p-5">
        <button
          onClick={handleNewChat}
          className="flex w-full items-center gap-3 rounded-xl bg-violet-600 px-4 py-3 transition hover:bg-violet-500"
        >
          <MessageSquarePlus size={18} />
          New Chat
        </button>

        <button
          onClick={onUpload}
          className="flex w-full items-center gap-3 rounded-xl border border-slate-700 px-4 py-3 transition hover:bg-slate-800"
        >
          <Upload size={18} />
          Upload PDF
        </button>
      </div>

      <div className="border-t border-slate-800 px-5 pt-5">
        <h2 className="mb-3 text-sm font-semibold uppercase tracking-wider text-slate-400">
          Recent Chats
        </h2>

        <ConversationList />
      </div>

      <div className="flex-1 overflow-auto border-t border-slate-800 px-5 pt-5">
        <h2 className="mb-3 text-sm font-semibold uppercase tracking-wider text-slate-400">
          Documents
        </h2>

        <DocumentsList />
      </div>

      <div className="border-t border-slate-800 p-4 text-center text-xs text-slate-500">
        AegisGPT v1.0
      </div>
    </aside>
  );
}