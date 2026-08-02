import api from "@/api/axios";

export interface Source {
  document_id: number;
  chunk_index: number;
}

export interface ChatRequest {
  question: string;
  document_id: number;
  conversation_id?: number;
  top_k?: number;
}

export interface ChatResponse {
  answer: string;
  conversation_id?: number;
  sources: Source[];
}

export const askQuestion = async (
  data: ChatRequest
): Promise<ChatResponse> => {
  const response = await api.post(
    "/chat",
    data
  );

  return response.data;
};