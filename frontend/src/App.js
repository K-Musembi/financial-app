import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MainLayout from "./components/MainLayout";
import Home from './components/Home';
import CreateBudget from "./components/CreateBudget";
import AddExpense from "./components/AddExpense";
import SignUp from './components/SignUp';
import Login from './components/Login';
import Team from './components/Team';
// import Logout from './components/Logout';
// import './App.css';
import Dashboard from "./components/Dashboard";
import BudgetDashboard from "./components/BudgetDashboard";

const App = () => {
    
    return (
        <Router>
            <div className="app-container">
                <Routes>
                    <Route path="/" element={<MainLayout><Home /></MainLayout>} />
                    <Route path="/dashboard" element={<MainLayout><Dashboard /></MainLayout>} />
                    <Route path="/budgetdashboard" element={<MainLayout><BudgetDashboard /></MainLayout>} />
                    <Route path="/signup" element={<MainLayout><SignUp /></MainLayout>} />
                    <Route path="/login" element={<MainLayout><Login /></MainLayout>} />
                    <Route path="/team" element={<MainLayout><Team /></MainLayout>} />
                    <Route path="/budgetdashboard/addexpense" element={<MainLayout><AddExpense /></MainLayout>} />
                    <Route path="/budgetdashboard/createbudget" element={<MainLayout><CreateBudget /></MainLayout>} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
