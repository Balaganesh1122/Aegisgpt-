import { useEffect, useState } from "react";
import { MessageSquare } from "lucide-react";

import {
  getConversations,
  type Conversation,
} from "@/services/conversation.service";

import { useChatContext } from "@/context/ChatContext";

export default function ConversationList() {
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [loading, setLoading] = useState(true);

  const {
    conversationId,
    loadConversation,
  } = useChatContext();

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const data = await getConversations();
      setConversations(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <p className="px-4 py-2 text-sm text-slate-400">
        Loading chats...
      </p>
    );
  }

  if (!conversations.length) {
    return (
      <p className="px-4 py-2 text-sm text-slate-400">
        No conversations yet
      </p>
    );
  }

  return (
    <div className="space-y-2">
      {conversations.map((conversation) => (
        <button
          key={conversation.id}
          onClick={() =>
            loadConversation(conversation.id)
          }
          className={`flex w-full items-center gap-3 rounded-lg px-3 py-2 text-left transition ${
            conversationId === conversation.id
              ? "bg-violet-600 text-white"
              : "text-slate-300 hover:bg-slate-800"
          }`}
        >
          <MessageSquare size={16} />

          <span className="truncate">
            {conversation.title}
          </span>
        </button>
      ))}
    </div>
  );
}