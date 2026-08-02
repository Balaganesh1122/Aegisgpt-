import { UploadCloud } from "lucide-react";
import { useRef, useState } from "react";
import { toast } from "sonner";

import { uploadDocument } from "@/services/document.service";
import { useChatContext } from "@/context/ChatContext";

interface UploadPanelProps {
  onSuccess: () => void;
}

export default function UploadPanel({
  onSuccess,
}: UploadPanelProps) {
  const fileInputRef =
    useRef<HTMLInputElement>(null);

  const [uploading, setUploading] =
    useState(false);

  const { refreshDocuments } =
    useChatContext();

  const handleChooseFile = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = async (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file =
      event.target.files?.[0];

    if (!file) return;

    setUploading(true);

    try {
      const result =
        await uploadDocument(file);

      await refreshDocuments();

      toast.success(
        result.message ??
          "PDF uploaded successfully!"
      );

      onSuccess(); // closes popup
    } catch (error: any) {
      console.error(error);

      toast.error(
        error?.response?.data?.detail ??
          "Upload failed."
      );
    } finally {
      setUploading(false);

      if (fileInputRef.current) {
        fileInputRef.current.value = "";
      }
    }
  };

  return (
    <div className="flex h-full items-center justify-center">
      <div className="w-full max-w-2xl rounded-3xl border-2 border-dashed border-slate-700 bg-slate-900/40 p-12 text-center">

        <div className="mx-auto flex h-20 w-20 items-center justify-center rounded-full bg-violet-600/20">
          <UploadCloud
            size={42}
            className="text-violet-400"
          />
        </div>

        <h2 className="mt-8 text-3xl font-bold text-white">
          Upload Your Documents
        </h2>

        <p className="mt-4 text-slate-400">
          Drag & Drop PDF files here or click below.
        </p>

        <input
          ref={fileInputRef}
          type="file"
          accept=".pdf"
          className="hidden"
          onChange={handleFileChange}
        />

        <button
          onClick={handleChooseFile}
          disabled={uploading}
          className="mt-8 rounded-xl bg-violet-600 px-8 py-3 font-semibold text-white hover:bg-violet-500 disabled:opacity-50"
        >
          {uploading
            ? "Uploading..."
            : "Choose PDF"}
        </button>

        <p className="mt-6 text-sm text-slate-500">
          Supported format: PDF
        </p>
      </div>
    </div>
  );
}