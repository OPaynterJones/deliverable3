import React from "react";
import "./NavBar.css";

const NavBar = () => {
  const handleLogout = async () => {
    try {
      const response = await fetch("/logout", {
        method: "POST", // Use POST for logout endpoint
        credentials: "include", // Important for sending cookies
      });

      if (response.status === 200) {
        window.location.reload();
      } else {
        console.error("Error logging out:", await response.text());
      }
    } catch (error) {
      console.error("Error logging out:", error);
    }
  };

  return (
    <nav className="navBar">
      <div className="title">Society Matchmaker</div>
      <div className="links">
        <a href="#">Find your events</a>
        <a href="#">Profile</a>
        <button onClick={handleLogout}>Logout</button>
      </div>
    </nav>
  );
};

export default NavBar;
