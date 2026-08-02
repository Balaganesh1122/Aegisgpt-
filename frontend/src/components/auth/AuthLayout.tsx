import type { ReactNode } from "react";

interface AuthLayoutProps {
  children: ReactNode;
  title?: string;
  subtitle?: string;
}

export default function AuthLayout({
  children,
  title = "🛡️ AegisGPT",
  subtitle = "Enterprise AI Document Intelligence",
}: AuthLayoutProps) {
  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-950 p-6">
      <div className="w-full max-w-md rounded-2xl border border-slate-800 bg-slate-900 p-8 shadow-2xl">
        <div className="mb-8 text-center">
          <h1 className="text-4xl font-bold text-white">
            {title}
          </h1>

          <p className="mt-3 text-slate-400">
            {subtitle}
          </p>
        </div>

        {children}
      </div>
    </div>
  );
}