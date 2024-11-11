import React from "react";
import { useNavigate } from 'react-router-dom';

const BudgetDashboard = ({ budgets }) => {
    const navigate = useNavigate()
    
    return (
        <div className="budget-container">
            {budgets && budgets.length > 0 ? (
                budgets.map((budget, index) => (
                    <div key={index} className="budget-panel">
                        <h2>{budget.period}</h2>
                        <p>Amount: {budget.amount}</p>
                        <p>Total Expenditure: {budget.total_expenditure}</p>
                        <button onClick={() => navigate('/addexpense')}>Add expenses</button>
                    </div>
                ))
            ) : (
                <div>
                    <p>No current budgets.</p>
                </div>
            )}
            <button onClick={() => navigate('/createbudget')}>Create new budget</button>
        </div>
    );
};

export default BudgetDashboard;
