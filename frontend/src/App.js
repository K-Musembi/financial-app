import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MainLayout from "./components/MainLayout";
import Home from './components/Home';
import CreateBudget from "./components/CreateBudget";
import AddExpense from "./components/AddExpense";
import SignUp from './components/SignUp';
import Login from './components/Login';
import Team from './components/Team';
import Logout from './components/Logout';
// import './App.css';
import Dashboard from "./components/Dashboard";
import BudgetDashboard from "./components/BudgetDashboard";

const App = () => {
    const [budgetId, setBudgetId] = useState(null);  // pass data from one component to another
    
    return (
        <Router>
            <div className="app-container">
                <Routes>
                    <Route path="/" element={<MainLayout><Home /></MainLayout>} />
                    <Route path="/dashboard" element={<MainLayout><Dashboard /></MainLayout>} />
                    <Route path="/budgetdashboard" element={<MainLayout><BudgetDashboard onId={setBudgetId} /></MainLayout>} />
                    <Route path="/signup" element={<MainLayout><SignUp /></MainLayout>} />
                    <Route path="/login" element={<MainLayout><Login /></MainLayout>} />
                    <Route path="/logout" element={<MainLayout><Logout /></MainLayout>} />
                    <Route path="/team" element={<MainLayout><Team /></MainLayout>} />
                    <Route path="/addexpense" element={<MainLayout><AddExpense budgetId={budgetId} /></MainLayout>} />
                    <Route path="/createbudget" element={<MainLayout><CreateBudget /></MainLayout>} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
