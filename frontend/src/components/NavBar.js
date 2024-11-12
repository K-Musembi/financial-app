import React from "react";
import { Link } from "react-router-dom";

const NavBar = ({ isLoggedIn, onLogout }) => {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/team">Team</Link></li>
                {isLoggedIn ? (
                    <li><button onClick={onLogout}>Logout</button></li>
                ) : (
                    <li><Link to="/login">Login</Link></li>
                )}
            </ul>
        </nav>
    );
};

export default NavBar;
