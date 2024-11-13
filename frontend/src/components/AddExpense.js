import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { API_URL } from "../config";

const AddExpense = ({ budgetId }) => {
    const [category, setCategory] = useState("");
    const [amount, setAmount] = useState("");

    const navigate = useNavigate();

    const handleAddExpense = async (event) => {
        event.preventDefault();

        const budgetid = budgetId

        const response = await fetch(`${API_URL}/addexpense`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ category, amount, budgetid }),
            credentials: "include"
        });
        if (response.ok) {
            navigate("/budgetdashboard");
        } else {
            alert("Please try again.");
        }
    };

    return (
        <div className="expense-budget-container">
            <h2>Track your spending</h2>
            <form onSubmit={handleAddExpense}>
                <label>
                    Category
                    <select value={category} onChange={(event) => setCategory(event.target.value)} required>
                        <option value="" disabled>Choose from categories</option>
                        <option value="groceries">Groceries</option>
                        <option value="food">Food</option>
                        <option value="rent">Rent</option>
                        <option value="electricity_water">Electricity/Water</option>
                        <option value="airtime">Airtime</option>
                        <option value="fare">Fare</option>
                        <option value="entertainment">Entertainment</option>
                        <option value="debt_payment">Debt Payment</option>
                        <option value="fee_payment">Fee Payment</option>
                        <option value="internet_connection">Internet Connection</option>
                        <option value="laundry">Laundry</option>
                        <option value="miscalleneous">Miscalleneous</option>
                    </select>
                </label>
                <label>
                    Amount
                    <input type="number" value={amount} onChange={(event) => setAmount(event.target.value)} required />
                </label>
                <button type="submit">Send</button>
            </form>
        </div>
    );
};

export default AddExpense;
