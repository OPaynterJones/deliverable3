import React from "react";
import "./NavBar.css";

const NavBar = ({ title }) => {
  const handleLogout = async () => {
    try {
      const response = await fetch("/logout", {
        method: "POST",
        credentials: "include",
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
    <div className="navBar-container">
      <nav className="navBar">
        <div className="app-name">Society Matchmaker</div>
        <h1 className="title">{title}</h1>
        <div className="links">
          <a href="#">Find your events</a>
          <a href="#">Profile</a>
          <button onClick={handleLogout}>Logout</button>
        </div>
      </nav>
    </div>
  );
};

export default NavBar;
