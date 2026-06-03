import React, { useState } from 'react';
import axios from 'axios';
import './AuthModal.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const AuthModal = ({ onClose, onAuthSuccess }) => {
    const [view, setView] = useState('login'); // 'login', 'signup', 'otp', 'forgot_password_email', 'reset_password'
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [fullName, setFullName] = useState('');
    const [phone, setPhone] = useState('');
    const [otp, setOtp] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [error, setError] = useState('');
    const [message, setMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSignup = async (e) => {
        e.preventDefault();
        setError('');
        setMessage('');
        setIsLoading(true);
        try {
            const response = await axios.post(`${API_URL}/api/auth/signup`, {
                email, password, full_name: fullName, phone
            });
            setMessage(response.data.message || "An OTP has been sent to your email.");
            setView('otp');
        } catch (err) {
            setError(err.response?.data?.message || err.response?.data?.error || 'Signup failed. Please try again.');
        } finally {
            setIsLoading(false);
        }
    };

    const handleLogin = async (e) => {
        e.preventDefault();
        setError('');
        setMessage('');
        setIsLoading(true);
        try {
            const response = await axios.post(`${API_URL}/api/auth/login`, { email, password });
            if (response.data.status === 'success') {
                onAuthSuccess(response.data.user_id);
            } else {
                setError(response.data.message || 'Login failed.');
            }
        } catch (err) {
            setError(err.response?.data?.message || err.response?.data?.error || 'Login failed. Please check your credentials.');
        } finally {
            setIsLoading(false);
        }
    };

    const handleVerifyOtp = async (e) => {
        e.preventDefault();
        setError('');
        setMessage('');
        setIsLoading(true);
        try {
            const response = await axios.post(`${API_URL}/api/auth/signup/verify`, { email, otp });
            setMessage(response.data.message || "Verification successful! You can now log in.");
            setOtp('');
            setView('login');
        } catch (err) {
            setError(err.response?.data?.message || err.response?.data?.error || 'OTP verification failed.');
        } finally {
            setIsLoading(false);
        }
    };

    const handleForgotPasswordInitiate = async (e) => {
        e.preventDefault();
        setError('');
        setMessage('');
        setIsLoading(true);
        try {
            const response = await axios.post(`${API_URL}/api/auth/password-reset/initiate`, { email });
            setMessage(response.data.message);
            setView('reset_password');
        } catch (err) {
            setError(err.response?.data?.message || err.response?.data?.error || 'Failed to initiate password reset.');
        } finally {
            setIsLoading(false);
        }
    };

    const handleResetPassword = async (e) => {
        e.preventDefault();
        if (newPassword !== confirmPassword) {
            setError("Passwords do not match.");
            return;
        }
        setError('');
        setMessage('');
        setIsLoading(true);
        try {
            const response = await axios.post(`${API_URL}/api/auth/password-reset/complete`, { 
                email, 
                otp, 
                new_password: newPassword 
            });
            if (response.data.status === 'success') {
                setMessage(response.data.message || "Password reset successfully. Please log in.");
                setView('login');
                // Clear password fields
                setOtp('');
                setNewPassword('');
                setConfirmPassword('');
            } else {
                setError(response.data.message || 'Password reset failed.');
            }
        } catch (err) {
            setError(err.response?.data?.message || err.response?.data?.error || 'Password reset failed.');
        } finally {
            setIsLoading(false);
        }
    };

    const renderLogin = () => (
        <form onSubmit={handleLogin}>
            <h2>Login</h2>
            <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
            <div className="forgot-password-link">
                <span onClick={() => setView('forgot_password_email')}>
                    Forgot Password?
                </span>
            </div>
            <button type="submit" disabled={isLoading}>{isLoading ? 'Logging in...' : 'Login'}</button>
            <p>Don't have an account? <span onClick={() => setView('signup')}>Sign Up</span></p>
        </form>
    );

    const renderSignup = () => (
        <form onSubmit={handleSignup}>
            <h2>Sign Up</h2>
            <input type="text" placeholder="Full Name" value={fullName} onChange={(e) => setFullName(e.target.value)} required />
            <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
            <input type="tel" placeholder="Phone Number (Optional)" value={phone} onChange={(e) => setPhone(e.target.value)} />
            <button type="submit" disabled={isLoading}>{isLoading ? 'Signing up...' : 'Sign Up'}</button>
            <p>Already have an account? <span onClick={() => setView('login')}>Login</span></p>
        </form>
    );

    const renderOtp = () => (
        <form onSubmit={handleVerifyOtp}>
            <h2>Verify Your Account</h2>
            <p>An OTP has been sent to {email}. Please enter it below.</p>
            <input
                type="text"
                placeholder="Enter 6-digit OTP"
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
                required
                maxLength="6"
            />
            <button type="submit" disabled={isLoading}>{isLoading ? 'Verifying...' : 'Verify'}</button>
            <p>Entered the wrong email? <span onClick={() => setView('signup')}>Go Back</span></p>
        </form>
    );

    const renderForgotPasswordEmail = () => (
        <form onSubmit={handleForgotPasswordInitiate}>
            <h2>Forgot Password</h2>
            <p>Enter your email to receive a login code.</p>
            <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            <button type="submit" disabled={isLoading}>{isLoading ? 'Sending...' : 'Send Code'}</button>
            <p>Remember your password? <span onClick={() => setView('login')}>Login</span></p>
        </form>
    );

    const renderResetPassword = () => (
        <form onSubmit={handleResetPassword}>
            <h2>Reset Your Password</h2>
            <p>An OTP has been sent to {email}.</p>
            <input
                type="text"
                placeholder="Enter 6-digit OTP"
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
                required
                maxLength="6"
            />
            <input 
                type="password" 
                placeholder="New Password" 
                value={newPassword} 
                onChange={(e) => setNewPassword(e.target.value)} 
                required 
            />
            <input 
                type="password" 
                placeholder="Confirm New Password" 
                value={confirmPassword} 
                onChange={(e) => setConfirmPassword(e.target.value)} 
                required 
            />
            <button type="submit" disabled={isLoading}>{isLoading ? 'Resetting...' : 'Reset Password'}</button>
            <p>Didn't get a code? <span onClick={() => setView('forgot_password_email')}>Go Back</span></p>
        </form>
    );

    return (
        <div className="modal-backdrop" onClick={onClose}>
            <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                <button className="close-button" onClick={onClose}>&times;</button>
                {error && <p className="error-message">{error}</p>}
                {message && <p className="info-message">{message}</p>}
                {view === 'login' && renderLogin()}
                {view === 'signup' && renderSignup()}
                {view === 'otp' && renderOtp()}
                {view === 'forgot_password_email' && renderForgotPasswordEmail()}
                {view === 'reset_password' && renderResetPassword()}
            </div>
        </div>
    );
};

export default AuthModal;
