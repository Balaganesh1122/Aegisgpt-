import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import "./index.css";
import App from "./App";

import { ChatProvider } from "./context/ChatContext";
import { DocumentProvider } from "./context/DocumentContext";

import { Toaster } from "sonner";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <DocumentProvider>
      <ChatProvider>
        <App />

        <Toaster
          richColors
          position="top-right"
          closeButton
          duration={3000}
        />
      </ChatProvider>
    </DocumentProvider>
  </StrictMode>
);