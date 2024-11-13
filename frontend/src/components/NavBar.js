import React from "react";
import { Link } from "react-router-dom";

const NavBar = ({ isLoggedIn }) => {
    return (
        <nav className="nav-bar">
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/team">Team</Link></li>
                {isLoggedIn ? (
                    <>
                        <li><Link to="/dashboard">My Money</Link></li>
                        <li><Link to="/logout">Logout</Link></li>
                    </>
                ) : (
                    <>
                        <li><Link to="/login">Login</Link></li>
                        <li><Link to="/signup">Sign up</Link></li>
                    </>
                )}
            </ul>
        </nav>
    );
};

export default NavBar;
