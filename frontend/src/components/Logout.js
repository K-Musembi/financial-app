import React from 'react';
import { useNavigate } from 'react-router-dom';
import { API_URL } from '../config';

const Logout = () => {
    const navigate = useNavigate()

    const handleLogout = async () => {
        const response = await fetch(`${API_URL}/logout`, {
            method: 'POST',
            credentials: 'include'
        });
        
        if (response.ok) {
            navigate("/");
        } else {
            alert("Logout failed!");
        }
    };

    return (
        <button className='logout-button' onClick={handleLogout}>
            Logout
        </button>
    );
};

export default Logout;
