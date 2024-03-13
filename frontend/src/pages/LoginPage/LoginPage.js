import React, { useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import "./LoginPage.css";
import InputField from "../../Components/AnimtedInputField/InputField";

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [isCreateAccount, setIsCreateAccount] = useState(false);
  const [isAuthenticated, setAuthenticated] = useState(null);

  // check if user is logged in when login page mounts

  useEffect(() => {
    const checkAuth = async () => {
      console.log("authenticating user");
      try {
        const response = await fetch("http://localhost:5000/check_session", {
          method: "GET",
          credentials: "include",
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.message);
        }

        console.log("already logged in");
        setAuthenticated(true);
      } catch (error) {
        console.error(error.message);
        console.log("no sesssion exists");
        setAuthenticated(false);
      }
    };
    checkAuth();
  }, []);

  if (isAuthenticated) {
    return <Navigate to="/for-you" replace />;
  }

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch(
        isCreateAccount
          ? "http://localhost:5000/register"
          : "http://localhost:5000/login",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email, password }), // TODO can clean up now this is done, using auth header
          credentials: "include",
        }
      );

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message);
      }

      if (isCreateAccount) {
        console.log("Register successful");
        // TODO display new message
      } else {
        console.log("Login successful");
        window.location.reload();
      }
    } catch (error) {
      console.error(error.message);
    }
  };

  return (
    <div
      className="login-container"
      style={{ height: isCreateAccount ? "25rem" : "21rem" }}
    >
      <h2 className="login-title">Sign in </h2>{" "}
      <h2 className="login-subtitle"> or create your account</h2>
      <form onSubmit={handleSubmit} className="login-form">
        <InputField
          type="email"
          fieldToAskFor="University Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <InputField
          type="password"
          fieldToAskFor="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {isCreateAccount && (
          <InputField
            className="confirm-password-field"
            type="password"
            fieldToAskFor="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
        )}
        <div className="button-container">
          <button
            type="button"
            className="create-account-button"
            onClick={() => setIsCreateAccount(!isCreateAccount)}
          >
            {isCreateAccount ? "Back to Login" : "Create New Account"}
          </button>
          <button
            type="submit"
            className="login-create-button"
            style={{ width: isCreateAccount ? "10rem" : "6rem" }}
          >
            <span style={{ opacity: isCreateAccount ? 0 : 1 }}>Login</span>
            <span style={{ opacity: isCreateAccount ? 1 : 0 }}>
              Create Account
            </span>
          </button>
        </div>
      </form>
    </div>
  );
};

export default LoginPage;
