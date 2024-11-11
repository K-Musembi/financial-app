import React from 'react';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
    const navigate = useNavigate();

    return (
        <div className="dashboard">
            <div className="panel">
                <h2>Income</h2>
                <p>Track your income streams</p>
                <button onClick={() => navigate('/incomedashboard')}>View Income</button>
            </div>

            <div className="panel">
                <h2>Budgets</h2>
                <p>Create budgets and track expenses</p>
                <button onClick={() => navigate('/budgetdashboard')}>View Budgets</button>
            </div>

            <div className="panel">
                <h2>Goals</h2>
                <p>Save and pursue your goals</p>
                <button onClick={() => navigate('/goaldashboard')}>View Goals</button>
            </div>
        </div>
    );
};

export default Dashboard;
