import api from "@/api/axios";

export interface Document {
  id: number;
  filename: string;
  original_filename: string;
  created_at: string;
}

export interface UploadResponse {
  message: string;
  document: Document;
}

export const uploadDocument = async (
  file: File
): Promise<UploadResponse> => {
  const formData = new FormData();

  formData.append("file", file);

  const response = await api.post(
    "/documents/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
      timeout: 120000,
    }
  );

  return response.data;
};

export const getDocuments = async (): Promise<Document[]> => {
  const response = await api.get("/documents/");

  return response.data;
};