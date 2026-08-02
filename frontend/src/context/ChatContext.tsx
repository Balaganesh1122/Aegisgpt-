import {
  createContext,
  useContext,
  useState,
  type ReactNode,
} from "react";

import { askQuestion } from "@/services/chat.service";
import {
  getConversationMessages,
} from "@/services/conversation.service";
import {
  getDocuments,
  type Document,
} from "@/services/document.service";

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export interface SelectedDocument {
  id: number;
  original_filename: string;
}

interface ChatContextType {
  messages: ChatMessage[];
  loading: boolean;

  conversationId?: number;
  selectedDocument?: SelectedDocument;

  documents: Document[];

  sendMessage: (question: string) => Promise<void>;

  loadConversation: (
    conversationId: number
  ) => Promise<void>;

  refreshDocuments: () => Promise<void>;

  setMessages: React.Dispatch<
    React.SetStateAction<ChatMessage[]>
  >;

  setConversationId: React.Dispatch<
    React.SetStateAction<number | undefined>
  >;

  setSelectedDocument: React.Dispatch<
    React.SetStateAction<
      SelectedDocument | undefined
    >
  >;
}

const ChatContext =
  createContext<ChatContextType | null>(null);

export function ChatProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [messages, setMessages] =
    useState<ChatMessage[]>([]);

  const [loading, setLoading] =
    useState(false);

  const [conversationId, setConversationId] =
    useState<number>();

  const [selectedDocument, setSelectedDocument] =
    useState<SelectedDocument>();

  const [documents, setDocuments] =
    useState<Document[]>([]);

  const refreshDocuments = async () => {
    try {
      const docs = await getDocuments();

      setDocuments(docs);

      if (docs.length > 0) {
        setSelectedDocument({
          id: docs[0].id,
          original_filename:
            docs[0].original_filename,
        });
      }
    } catch (error) {
      console.error(error);
    }
  };

  const sendMessage = async (
    question: string
    ) => {
    if (!selectedDocument) {
        alert("Please select a document first.");
        return;
    }

    setLoading(true);

    // Add user message
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
        document_id: selectedDocument.id,
        conversation_id: conversationId,
        top_k: 15,
        });

        if (response.conversation_id) {
        setConversationId(response.conversation_id);
        }

        // Add empty assistant message
        setMessages((prev) => [
        ...prev,
        {
            role: "assistant",
            content: "",
        },
        ]);

        const fullText = response.answer;

        for (let i = 0; i < fullText.length; i++) {
        await new Promise((resolve) =>
            setTimeout(resolve, 8)
        );

        setMessages((prev) => {
            const updated = [...prev];

            updated[updated.length - 1] = {
            role: "assistant",
            content: fullText.substring(0, i + 1),
            };

            return updated;
        });
        }
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

  const loadConversation = async (
    conversationId: number
  ) => {
    try {
      setLoading(true);

      const history =
        await getConversationMessages(
          conversationId
        );

      setMessages(
        history.map((message) => ({
          role: message.role,
          content: message.content,
        }))
      );

      setConversationId(conversationId);
    } finally {
      setLoading(false);
    }
  };

  return (
    <ChatContext.Provider
      value={{
        messages,
        loading,
        conversationId,
        selectedDocument,
        documents,
        sendMessage,
        loadConversation,
        refreshDocuments,
        setMessages,
        setConversationId,
        setSelectedDocument,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
}

export function useChatContext() {
  const context = useContext(ChatContext);

  if (!context) {
    throw new Error(
      "useChatContext must be used inside ChatProvider"
    );
  }

  return context;
}