import { useState } from "react";

interface LoginProps {
  onLoginSuccess: () => void;
}

// apps/owner/src/pages/Login/index.tsx
export function Login() {
  return (
<div
      className="min-h-screen flex items-center justify-center bg-cover bg-center"
      style={{
        backgroundImage: `url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1740&q=80')`,
      }}
    >
      <div className="bg-white/80 backdrop-blur-md p-8 rounded-2xl shadow-xl w-full max-w-sm">
        <h1 className="text-3xl font-bold text-center mb-6">Welcome Back</h1>
        <form className="space-y-4">
          <div>
            <label className="block text-gray-700">Email</label>
            <input
              type="email"
              placeholder="Enter your email"
              className="w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500"
            />
          </div>
          <div>
            <label className="block text-gray-700">Password</label>
            <input
              type="password"
              placeholder="Enter your password"
              className="w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500"
            />
          </div>
          <button
            type="submit"
            className="w-full bg-orange-500 text-white py-2 rounded-lg hover:bg-orange-600 transition"
          >
            Login
          </button>
        </form>
        <p className="text-center text-gray-600 text-sm mt-4">
          Don't have an account? <a href="#" className="text-orange-500">Sign up</a>
        </p>
      </div>
    </div>
  );
}
