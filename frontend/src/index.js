import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import LoginPage from "./pages/LoginPage/LoginPage";
import ForYouPage from "./pages/ForYouPage/ForYouPage";
import "./global-styles.css";

function BodyStyleManager() {
  const location = useLocation();
  const currentPage = location.pathname.substring(1); // Remove the leading slash

  // Set the body class dynamically
  React.useEffect(() => {
    document.body.className = currentPage + "-page-body";
  }, [currentPage]);

  return null;
}

const App = () => (
  <BrowserRouter>
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/foryou/" element={<ForYouPage />} />
    </Routes>
    <BodyStyleManager />
  </BrowserRouter>
);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
