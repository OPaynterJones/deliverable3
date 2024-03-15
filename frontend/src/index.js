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
import SocietyPage from "./pages/SocietyPage/SocietyPage";
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

        setAuthenticated(true);
      } catch (error) {
        console.error(error.message);
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
      <Route path="/" element={<Navigate to="/for-you" replace />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/society/:society_name" element={<SocietyPage />} />
      <Route element={<RequireAuth />}>
        <Route path="/for-you" element={<ForYouPage />} />
      </Route>
    </Routes>
    <BodyStyleManager />
  </BrowserRouter>
);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
