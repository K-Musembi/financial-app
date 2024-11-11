import React from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {
    const navigate = useNavigate();

    const handleGetStarted = () => {
        navigate("/login");
    }
    
    return (
        <div className="home-container">
            <h1>Welcome to PesaTrack</h1>
            <p>
                Empowering people to have better control of their money by enabling healthy financial habits.
            </p>
            <button onClick={handleGetStarted}>Get Started</button>
        </div>
    );
};

export default Home;
