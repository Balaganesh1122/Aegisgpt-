import { useState } from "react";
import { Send } from "lucide-react";

import MessageBubble from "./MessageBubble";
import { useChatContext } from "@/context/ChatContext";

export default function ChatLayout() {
  const [question, setQuestion] = useState("");

  const {
    messages,
    loading,
    sendMessage,
    selectedDocumentId,
  } = useChatContext();

  const handleSend = async () => {
    if (!question.trim()) return;

    await sendMessage(question);

    setQuestion("");
  };

  return (
    <div className="flex h-full flex-col rounded-2xl border border-slate-800 bg-slate-900">
      {/* Header */}
      <div className="border-b border-slate-800 p-6">
        <h2 className="text-2xl font-bold text-white">
          🤖 AegisGPT Assistant
        </h2>

        <p className="mt-2 text-slate-400">
          {selectedDocumentId
            ? `Document ID: ${selectedDocumentId}`
            : "Select a document from the sidebar to start chatting."}
        </p>
      </div>

      {/* Messages */}
      <div className="flex-1 space-y-5 overflow-y-auto p-6">
        {messages.length === 0 && (
          <div className="mt-20 text-center text-slate-500">
            Ask your first question 🚀
          </div>
        )}

        {messages.map((message, index) => (
          <MessageBubble
            key={index}
            role={message.role}
            content={message.content}
          />
        ))}

        {loading && (
          <MessageBubble
            role="assistant"
            content="🤖 Thinking..."
          />
        )}
      </div>

      {/* Input */}
      <div className="border-t border-slate-800 p-5">
        <div className="flex gap-3">
          <input
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleSend();
              }
            }}
            placeholder="Ask anything about your document..."
            className="flex-1 rounded-xl border border-slate-700 bg-slate-800 px-5 py-3 text-white outline-none focus:border-violet-500"
          />

          <button
            onClick={handleSend}
            disabled={loading}
            className="rounded-xl bg-violet-600 px-5 text-white transition hover:bg-violet-500 disabled:opacity-50"
          >
            <Send size={18} />
          </button>
        </div>
      </div>
    </div>
  );
}