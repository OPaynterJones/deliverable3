import React, { useState, useEffect } from "react";
import InputField from "../../Components/AnimtedInputField/InputField";
import "./LoginPage.css"; // Import CSS file

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [isCreateAccount, setIsCreateAccount] = useState(false);
  const [containerHeight, setContainerHeight] = useState("21rem");
  const [submitButtonWidth, setButtonWidth] = useState("6rem");

  useEffect(() => {
    setContainerHeight(isCreateAccount ? "25rem" : "21rem");
  }, [isCreateAccount]);

  useEffect(() => {
    setButtonWidth(isCreateAccount ? "10rem" : "6rem"); // fix this
  }, [isCreateAccount]);

  const handleSubmit = (event) => {
    event.preventDefault();
    if (isCreateAccount) {
      console.log(
        "Creating account with email:",
        email,
        "and password:",
        password
      );
    } else {
      console.log("Logging in with email:", email, "and password:", password);
    }
  };

  const toggleMode = () => {
    setIsCreateAccount(!isCreateAccount);
  };

  return (
    <div className="login-container" style={{ height: containerHeight }}>
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
            onClick={toggleMode}
          >
            {isCreateAccount ? "Back to Login" : "Create New Account"}
          </button>
          <button
            type="submit"
            className="login-create-button"
            style={{ width: submitButtonWidth }}
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
