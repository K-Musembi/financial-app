import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';
import { API_URL } from "../config";

const SignUp = (onLogin) => {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    
    const navigate = useNavigate()

    const handleSignUp = async (event) => {
        event.preventDefault();
        
        const response = await fetch(`${API_URL}/signup`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, email, password }),
            credentials: "include"
        });
        if (response.ok) {
            alert("Successfully signed up!");
            setUsername("");
            setEmail("");
            setPassword("");
            onLogin();
            navigate("/dashboard");
        } else {
            alert("Please try again.");
        }
    };

    return (
        <div className="signup-container">
            <h2>Create Account</h2>
            <form onSubmit={handleSignUp}>
                <label>
                    Username
                    <input type="text" value={username} onChange={(event) => setUsername(event.target.value)} required />
                </label>
                <label>
                    Email
                    <input type="email" value={email} onChange={(event) => setEmail(event.target.value)} required />
                </label>
                <label>
                    Password
                    <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} required />
                </label>
                <button type="submit">Sign Up</button>
            </form> 
        </div>
    );
};

export default SignUp;
