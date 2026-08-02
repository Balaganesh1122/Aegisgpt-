import { Copy, Check, Bot, User } from "lucide-react";
import { useState } from "react";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeHighlight from "rehype-highlight";

import "highlight.js/styles/github-dark.css";

interface MessageBubbleProps {
  role: "user" | "assistant";
  content: string;
}

export default function MessageBubble({
  role,
  content,
}: MessageBubbleProps) {
  const isUser = role === "user";

  const [copied, setCopied] = useState(false);

  const copyMessage = async () => {
    await navigator.clipboard.writeText(content);

    setCopied(true);

    setTimeout(() => {
      setCopied(false);
    }, 2000);
  };

  return (
    <div
      className={`flex gap-3 ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      {!isUser && (
        <div className="mt-1 flex h-10 w-10 items-center justify-center rounded-full bg-violet-600">
          <Bot size={20} />
        </div>
      )}

      <div
        className={`group relative max-w-[80%] rounded-2xl px-5 py-4 shadow-lg ${
          isUser
            ? "bg-violet-600 text-white"
            : "border border-slate-700 bg-slate-800 text-slate-100"
        }`}
      >
        {!isUser && (
          <button
            onClick={copyMessage}
            className="absolute right-3 top-3 rounded-md p-2 opacity-0 transition hover:bg-slate-700 group-hover:opacity-100"
            title="Copy"
          >
            {copied ? (
              <Check
                size={16}
                className="text-green-400"
              />
            ) : (
              <Copy
                size={16}
                className="text-slate-400"
              />
            )}
          </button>
        )}

        <article className="prose prose-invert prose-sm max-w-none break-words">
          <>
            <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                rehypePlugins={[rehypeHighlight]}
            >
                {content}
            </ReactMarkdown>

            {!isUser &&
                content.length > 0 &&
                content.length < 5000 && (
                <span className="ml-1 animate-pulse text-violet-400">
                    ▌
                </span>
                )}
            </>
        </article>
      </div>

      {isUser && (
        <div className="mt-1 flex h-10 w-10 items-center justify-center rounded-full bg-violet-500">
          <User size={20} />
        </div>
      )}
    </div>
  );
}