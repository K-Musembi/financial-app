import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { API_URL } from "../config";

const CreateBudget = () => {
    const [timePeriod, setTimePeriod] = useState("");
    const [amount, setAmount] = useState("");

    const navigate = useNavigate();

    const handleCreateBudget = async (event) => {
        event.preventDefault();

        const response = await fetch(`${API_URL}/createbudget`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ timePeriod, amount }),
            credentials: "include"
        });
        if (response.ok) {
            navigate("/budgetdashboard");
        } else {
            alert("Please try again.");
        }
    };

    return (
        <div className="createbudget-container">
            <h2>Create a new budget</h2>
            <form onSubmit={handleCreateBudget}>
                <label>
                    Choose time period
                    <select value={timePeriod} onChange={(event) => setTimePeriod(event.target.value)} required>
                        <option value="" disabled></option>
                        <option value="monthly">Monthly</option>
                        <option value="weekly">Weekly</option>
                    </select>
                </label>
                <label>
                    Amount
                    <input type="number" value={amount} onChange={(event) => setAmount(event.target.value)} required />
                </label>
            </form>
        </div>
    );
};

export default CreateBudget;
