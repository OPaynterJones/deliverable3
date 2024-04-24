import React from "react";
import "./NavBar.css";
import { NavLink } from "react-router-dom";
import { backendUrl } from "../../config";

const NavBar = ({ title }) => {
  const handleLogout = async () => {
    const response = await fetch(`${backendUrl}/logout`, {
      method: "POST",
      credentials: "include",
    });

    if (!response.ok) {
      console.log(await response.json());
    }

    window.location.reload();
  };

  return (
    <div className="navBar-container">
      <nav className="navBar">
        <div className="app-name">Society Matchmaker</div>
        <h1 className="title">{title}</h1>
        <div className="links">
          <NavLink to="/choose-your-interests">Add interests</NavLink>
          <button onClick={handleLogout}>Logout</button>
        </div>
      </nav>
    </div>
  );
};

export default NavBar;
