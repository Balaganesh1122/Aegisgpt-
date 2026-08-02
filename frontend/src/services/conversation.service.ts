import api from "@/api/axios";

export interface Conversation {
  id: number;
  title: string;
  document_id: number;
  created_at: string;
}

export interface Message {
  id: number;
  role: "user" | "assistant";
  content: string;
  created_at: string;
}

export const getConversations = async (): Promise<Conversation[]> => {
  const response = await api.get("/chat/conversations");
  return response.data;
};

export const getConversationMessages = async (
  conversationId: number
): Promise<Message[]> => {
  const response = await api.get(
    `/chat/conversations/${conversationId}/messages`
  );

  return response.data;
};

export const deleteConversation = async (
  conversationId: number
) => {
  await api.delete(`/chat/conversations/${conversationId}`);
};