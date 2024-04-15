import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./LoginPage.css";
import InputField from "../../Components/AnimtedInputField/InputField";
import { fetchSocieties } from "../../api/getAPI";
import { checkSession } from "../../api/authAPI";

const LoginPage = () => {
  const navigate = useNavigate();
  const [isAuthenticated, setAuthenticated] = useState(null);
  const [isCreateAccount, setIsCreateAccount] = useState(false);
  const [isCommitteeMember, setIsCommitteeMember] = useState(false);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [statusMessage, setStatusMessage] = useState(null);

  const [societies, setSocieties] = useState([]);

  // check if user is logged in when page is mounted
  useEffect(() => {
    const checkLoggedIn = async () => {
      try {
        const response = await checkSession();
        console.log(response);
        setAuthenticated(response.sessionValid);
      } catch (err) {
        console.log(err);
      }
    };
    checkLoggedIn();
  }, []);

  // redirect if authentication status changes
  useEffect(() => {
    if (isAuthenticated) {
      navigate("/for-you", { replace: "true" });
    }
  }, [isAuthenticated, navigate]);

  // Make request to backend with data
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      let dataToSend = { email, password };
      const selector = document.querySelector(".society-dropdown");
      if (isCommitteeMember && selector) {
        dataToSend.affiliatedSociety = selector.value;
      }
      const response = await fetch(
        isCreateAccount
          ? `http://${window.location.hostname}:5000/register`
          : `http://${window.location.hostname}:5000/login`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(dataToSend), // TODO can clean up now this is done, using auth header
          credentials: "include",
        }
      );

      const data = await response.json();
      setStatusMessage(data.message);

      if (!isCreateAccount && response.ok) {
        setTimeout(() => {
          window.location.reload();
        }, 1000);
      }
    } catch (error) {
      console.error(error.message);
    }
  };

  // get available socities
  useEffect(() => {
    if (isCommitteeMember) {
      try {
        fetchSocieties().then(setSocieties);
      } catch (error) {
        console.error("Error fetching societies:", error);
      }
    }
  }, [isCommitteeMember]);

  return (
    setAuthenticated && (
      <div
        className="login-container"
        style={{ height: isCreateAccount ? "26rem" : "21rem" }}
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
              doc
              fieldToAskFor="Confirm Password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
          )}
          <div className="additional-login-info">
            <div className="button-container1">
              <button
                type="button"
                className="create-account-button"
                onClick={() => {
                  setStatusMessage(null);
                  setIsCreateAccount(!isCreateAccount);
                }}
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
            {isCreateAccount && (
              <>
                <div className="committee-member-checkbox">
                  <label htmlFor="committee-member">
                    I'm a committee member
                  </label>
                  <input
                    type="checkbox"
                    id="committee-member"
                    value={isCommitteeMember}
                    onChange={(e) => setIsCommitteeMember(e.target.checked)}
                  />
                </div>
                {isCommitteeMember && (
                  <select className="society-dropdown">
                    <option value="" disabled>
                      Select Society
                    </option>
                    {societies.map((societyName) => (
                      <option
                        key={societyName}
                        value={societyName}
                        className="dropdown-option"
                      >
                        {societyName}
                      </option>
                    ))}
                  </select>
                )}
              </>
            )}
            {statusMessage && (
              <p className="success-message">{statusMessage}</p>
            )}
          </div>
        </form>
      </div>
    )
  );
};

export default LoginPage;
