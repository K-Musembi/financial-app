import React from "react";

const Team = () => {

    return (
        <div className="team-container">
            <h2>Meet the developer.</h2>
            <div className="card">
                <div className="team-photo">
                    <img
                        src=""
                        alt="Dev"
                        className="photo"
                    />
                    <p className="name">Kevin Musembi</p>
                </div>
                <div className="team-info">
                    <h3>About me</h3>
                    <p><strong>Bio:</strong> Software engineer with a passion for creating apps that have societal impact</p>
                    <p><strong>Email:</strong> kevinmusembi.m@gmail.com</p>
                    <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/kevin-musembi/" target="_blank" rel="noopener noreferrer">Profile</a></p>
                </div>
            </div>
        </div>
    );
};

export default Team;
