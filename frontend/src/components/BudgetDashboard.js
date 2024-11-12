import React, { useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import { API_URL } from "../config";

const BudgetDashboard = () => {
    const [budgets, setBudgets] = useState([]);
    const navigate = useNavigate()

    // useEffect defines action to occur when page is loaded
    useEffect(() => {
        const fetchBudgets = async () => {
            const response = await fetch(`${API_URL}/budgetdashboard`);

            if (response.ok) {
                const data = await response.json();
                // data is a an object; one of it's properties should be budgets
                setBudgets(data.budgets || []);
            } else {
                alert("Budgets could not be fetched");
            }
        }
        fetchBudgets();
    }, []);
    
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
