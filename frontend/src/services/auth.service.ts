import api from "@/api/axios";

export interface RegisterRequest {
  full_name: string;
  email: string;
  password: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export const registerUser = async (
  data: RegisterRequest
) => {
  const response = await api.post(
    "/auth/register",
    data
  );

  return response.data;
};

export const loginUser = async (
  data: LoginRequest
) => {
  const response = await api.post(
    "/auth/login",
    data
  );

  localStorage.setItem(
    "access_token",
    response.data.access_token
  );

  return response.data;
};

export const logout = () => {
  localStorage.removeItem("access_token");
};