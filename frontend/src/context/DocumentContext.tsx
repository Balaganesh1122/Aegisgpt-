import {
  createContext,
  useContext,
  useEffect,
  useState,
  type ReactNode,
} from "react";

import {
  getDocuments,
  type Document,
} from "@/services/document.service";

interface SelectedDocument {
  id: number;
  original_filename: string;
}

interface DocumentContextType {
  documents: Document[];
  loading: boolean;

  selectedDocument?: SelectedDocument;

  setSelectedDocument: (
    document: SelectedDocument | undefined
  ) => void;

  refreshDocuments: () => Promise<void>;
}

const DocumentContext =
  createContext<DocumentContextType | null>(null);

export function DocumentProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [loading, setLoading] = useState(true);

  const [selectedDocument, setSelectedDocument] =
    useState<SelectedDocument>();

  const refreshDocuments = async () => {
    setLoading(true);

    try {
      const docs = await getDocuments();

      setDocuments(docs);

      // Auto-select latest uploaded document
      if (docs.length > 0) {
        setSelectedDocument({
          id: docs[0].id,
          original_filename: docs[0].original_filename,
        });
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    refreshDocuments();
  }, []);

  return (
    <DocumentContext.Provider
      value={{
        documents,
        loading,
        selectedDocument,
        setSelectedDocument,
        refreshDocuments,
      }}
    >
      {children}
    </DocumentContext.Provider>
  );
}

export function useDocument() {
  const context = useContext(DocumentContext);

  if (!context) {
    throw new Error(
      "useDocument must be used inside DocumentProvider"
    );
  }

  return context;
}