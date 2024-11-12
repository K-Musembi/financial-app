import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { API_URL } from "../config";

const Login = (onLogin) => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const navigate = useNavigate()

    const handleLogin = async (event) => {
        event.preventDefault();

        const response = await fetch(`${API_URL}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });
        if (response.ok) {
            // const result = await response.json();
            onLogin();
            alert("Successful login!");
            navigate("/dashboard");
        } else {
            alert("Check your credentials and try again.");
        }
    };

    return (
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
                <label>
                    Email
                    <input type="text" value={email} onChange={(event) => setEmail(event.target.value)} required />
                </label>
                <label>
                    Password
                    <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} required />
                </label>
                <button type="submit">Submit</button>
                <p>
                    Not yet registered? <a href="/signup">Sign Up</a>
                </p>
            </form>
        </div>
    );
};

export default Login;
