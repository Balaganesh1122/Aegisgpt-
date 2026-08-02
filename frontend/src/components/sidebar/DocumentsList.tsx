import { useEffect } from "react";
import { FileText } from "lucide-react";

import { useChatContext } from "@/context/ChatContext";

export default function DocumentsList() {
  const {
    documents,
    refreshDocuments,
    selectedDocument,
    setSelectedDocument,
  } = useChatContext();

  useEffect(() => {
    refreshDocuments();
  }, []);

  if (!documents.length) {
    return (
      <div className="px-4 py-3 text-sm text-slate-400">
        No documents uploaded yet.
      </div>
    );
  }

  return (
    <div className="space-y-2">
      {documents.map((document) => {
        const active =
          selectedDocument?.id === document.id;

        return (
          <button
            key={document.id}
            onClick={() =>
              setSelectedDocument({
                id: document.id,
                original_filename:
                  document.original_filename,
              })
            }
            className={`flex w-full items-center gap-3 rounded-lg px-4 py-3 text-left transition ${
              active
                ? "bg-violet-600 text-white"
                : "text-slate-300 hover:bg-slate-800"
            }`}
          >
            <FileText size={18} />

            <span className="truncate">
              {document.original_filename}
            </span>
          </button>
        );
      })}
    </div>
  );
}