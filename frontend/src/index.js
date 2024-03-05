import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom/client";
import {
  BrowserRouter,
  Routes,
  Route,
  useLocation,
  Navigate,
  Outlet,
} from "react-router-dom";
import LoginPage from "./pages/LoginPage/LoginPage";
import ForYouPage from "./pages/ForYouPage/ForYouPage";
import "./global-styles.css";

// ------------- STYLING -------------
function BodyStyleManager() {
  const location = useLocation();
  const currentPage = location.pathname.substring(1);

  React.useEffect(() => {
    document.body.className = currentPage + "-page-body";
  }, [currentPage]);

  return null;
}

// ------------- AUTHENTICATION LOGIC -------------

// ------------- ROUTING  -------------

const RequireAuth = () => {
  const [authenticated, setAuthenticated] = useState(null);

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

        console.log("already logged in, going to outlet");
        setAuthenticated(true);
      } catch (error) {
        console.error(error.message);
        console.log("no existing session, going to login");
        setAuthenticated(false);
      }
    };

    checkAuth();
  }, []);

  if (authenticated === null) {
    return null;
  }

  if (!authenticated) {
    console.log("no existing session, goign to login");
    return <Navigate to="/login" />;
  }

  console.log("already looged in, going to outlet");
  return <Outlet />;
};

// ------------- MAIN ROUTING -------------
const App = () => (
  <BrowserRouter>
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route element={<RequireAuth />}>
        <Route path="/for-you" element={<ForYouPage />} />
        <Route path="*" element={<Navigate to="/for-you" replace />} />
      </Route>
    </Routes>
    <BodyStyleManager />
  </BrowserRouter>
);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
