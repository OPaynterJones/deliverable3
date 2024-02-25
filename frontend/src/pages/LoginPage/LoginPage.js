import React, { useState } from "react";
import InputField from "../../Components/AnimtedInputField/InputField";

// this is a fudge lol
document.body.style.display = "flex";
document.body.style.justifyContent = "center";
document.body.style.alignContent = "center";
document.body.style.minHeight = "100vh";

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Form submitted with email:", email, "and password:", password);
  };

  return (
    <div
      style={{
        width: "680px",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <h2
        style={{
          fontSize: "24px",
          fontWeight: "400",
          fontFamily: "'Google Sans','Noto Sans Myanmar UI',arial,sans-serif",
          textAlign: "center",
        }}
      >
        Sign in or register
      </h2>
      <form onSubmit={handleSubmit}>
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
        <button
          type="submit"
          style={{ width: "100%", boxSizing: "border-box" }}
        >
          Login
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
