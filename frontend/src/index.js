import React, { useEffect, useState } from "react";
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
import ChooseYourInterestsPage from "./pages/ChoseYourInterests/ChoseYourInterestsPage";
import "./global-styles.css";
import { checkSession } from "./api/authAPI";

// ------------- STYLING -------------
function BodyStyleManager() {
  const location = useLocation();
  const currentPage = location.pathname.substring(1);

  React.useEffect(() => {
    document.body.className = currentPage.startsWith("societies")
      ? "society-page-body"
      : currentPage + "-page-body";
  }, [currentPage]);

  return null;
}

// ------------- AUTHENTICATION LOGIC -------------

// ------------- ROUTING  -------------

const RequireAuth = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const checkLoggedIn = async () => {
      const response = await checkSession();
      setIsAuthenticated(response.sessionValid);
      setIsLoading(false);
    };

    checkLoggedIn();
  }, []);

  if (isLoading) {
    return <div></div>;
  }

  return isAuthenticated ? <Outlet /> : <Navigate to="/login" />;
};
// ------------- MAIN ROUTING -------------
const App = () => (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Navigate to="/for-you" replace />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/societies/:society_name" element={<SocietyPage />} />
      <Route
        path="/chose-your-interests"
        element={<ChooseYourInterestsPage />}
      />
      <Route element={<RequireAuth />}>
        <Route path="/for-you" element={<ForYouPage />} />
      </Route>
    </Routes>
    <BodyStyleManager />
  </BrowserRouter>
);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
