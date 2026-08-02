import { useState } from "react";

import { askQuestion } from "@/services/chat.service";

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export function useChat() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);

  const [loading, setLoading] = useState(false);

  const [conversationId, setConversationId] =
    useState<number>();

  const sendMessage = async (
    question: string,
    documentId: number
  ) => {
    setLoading(true);

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: question,
      },
    ]);

    try {
      const response = await askQuestion({
        question,
        document_id: documentId,
        conversation_id: conversationId,
        top_k: 5,
      });

      if (response.conversation_id) {
        setConversationId(response.conversation_id);
      }

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: response.answer,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Something went wrong while contacting the AI.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return {
    messages,
    loading,
    sendMessage,
  };
}