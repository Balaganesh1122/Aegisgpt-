import AuthLayout from "@/components/auth/AuthLayout";
import LoginForm from "@/components/auth/LoginForm";

export default function Login() {
  return (
    <AuthLayout
      title="🛡️ AegisGPT"
      subtitle="Sign in to continue"
    >
      <LoginForm />
    </AuthLayout>
  );
}