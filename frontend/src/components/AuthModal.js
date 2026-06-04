import React, { useState } from 'react';
import axios from 'axios';

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
        <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <h2 className="s-h2" style={{ fontSize: '28px', marginBottom: '8px' }}>Login</h2>
            <input className="input-field" type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            <input className="input-field" type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
            
            <div style={{ textAlign: 'right' }}>
                <button type="button" style={{ background: 'none', border: 'none', color: 'var(--color-muted)', fontSize: '13px', padding: 0, cursor: 'pointer' }} onClick={() => setView('forgot_password_email')}>
                    Forgot Password?
                </button>
            </div>
            
            <button className="btn-primary" type="submit" disabled={isLoading} style={{ marginTop: '8px' }}>{isLoading ? 'Logging in...' : 'Login'}</button>
            
            <div style={{ marginTop: '24px', textAlign: 'center' }}>
                <span style={{ color: 'var(--color-muted)', fontSize: '14px' }}>Don't have an account? </span>
                <button type="button" className="btn-ghost" style={{ padding: '4px 12px', fontSize: '14px', border: 'none', color: 'var(--color-accent)' }} onClick={() => setView('signup')}>Sign up</button>
            </div>
        </form>
    );

    const renderSignup = () => (
        <form onSubmit={handleSignup} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <h2 className="s-h2" style={{ fontSize: '28px', marginBottom: '8px' }}>Sign Up</h2>
            <input className="input-field" type="text" placeholder="Full Name" value={fullName} onChange={(e) => setFullName(e.target.value)} required />
            <input className="input-field" type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            <input className="input-field" type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
            <input className="input-field" type="tel" placeholder="Phone Number (Optional)" value={phone} onChange={(e) => setPhone(e.target.value)} />
            
            <button className="btn-primary" type="submit" disabled={isLoading} style={{ marginTop: '8px' }}>{isLoading ? 'Signing up...' : 'Sign Up'}</button>
            
            <div style={{ marginTop: '24px', textAlign: 'center' }}>
                <span style={{ color: 'var(--color-muted)', fontSize: '14px' }}>Already have an account? </span>
                <button type="button" className="btn-ghost" style={{ padding: '4px 12px', fontSize: '14px', border: 'none', color: 'var(--color-accent)' }} onClick={() => setView('login')}>Login</button>
            </div>
        </form>
    );

    const renderOtp = () => (
        <form onSubmit={handleVerifyOtp} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <h2 className="s-h2" style={{ fontSize: '28px', marginBottom: '8px' }}>Verify Account</h2>
            <p className="s-sub" style={{ marginBottom: '16px', fontSize: '14px' }}>An OTP has been sent to {email}.</p>
            <input
                className="input-field"
                type="text"
                placeholder="Enter 6-digit OTP"
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
                required
                maxLength="6"
                style={{ letterSpacing: '4px', textAlign: 'center', fontSize: '20px', fontFamily: 'JetBrains Mono, monospace' }}
            />
            <button className="btn-primary" type="submit" disabled={isLoading} style={{ marginTop: '8px' }}>{isLoading ? 'Verifying...' : 'Verify'}</button>
            
            <div style={{ marginTop: '24px', textAlign: 'center' }}>
                <span style={{ color: 'var(--color-muted)', fontSize: '14px' }}>Wrong email? </span>
                <button type="button" className="btn-ghost" style={{ padding: '4px 12px', fontSize: '14px', border: 'none', color: 'var(--color-accent)' }} onClick={() => setView('signup')}>Go Back</button>
            </div>
        </form>
    );

    const renderForgotPasswordEmail = () => (
        <form onSubmit={handleForgotPasswordInitiate} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <h2 className="s-h2" style={{ fontSize: '28px', marginBottom: '8px' }}>Forgot Password</h2>
            <p className="s-sub" style={{ marginBottom: '16px', fontSize: '14px' }}>Enter your email to receive a login code.</p>
            <input className="input-field" type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            
            <button className="btn-primary" type="submit" disabled={isLoading} style={{ marginTop: '8px' }}>{isLoading ? 'Sending...' : 'Send Code'}</button>
            
            <div style={{ marginTop: '24px', textAlign: 'center' }}>
                <span style={{ color: 'var(--color-muted)', fontSize: '14px' }}>Remember your password? </span>
                <button type="button" className="btn-ghost" style={{ padding: '4px 12px', fontSize: '14px', border: 'none', color: 'var(--color-accent)' }} onClick={() => setView('login')}>Login</button>
            </div>
        </form>
    );

    const renderResetPassword = () => (
        <form onSubmit={handleResetPassword} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <h2 className="s-h2" style={{ fontSize: '28px', marginBottom: '8px' }}>Reset Password</h2>
            <p className="s-sub" style={{ marginBottom: '16px', fontSize: '14px' }}>An OTP has been sent to {email}.</p>
            <input
                className="input-field"
                type="text"
                placeholder="Enter 6-digit OTP"
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
                required
                maxLength="6"
                style={{ letterSpacing: '4px', textAlign: 'center', fontSize: '20px', fontFamily: 'JetBrains Mono, monospace' }}
            />
            <input 
                className="input-field"
                type="password" 
                placeholder="New Password" 
                value={newPassword} 
                onChange={(e) => setNewPassword(e.target.value)} 
                required 
            />
            <input 
                className="input-field"
                type="password" 
                placeholder="Confirm New Password" 
                value={confirmPassword} 
                onChange={(e) => setConfirmPassword(e.target.value)} 
                required 
            />
            
            <button className="btn-primary" type="submit" disabled={isLoading} style={{ marginTop: '8px' }}>{isLoading ? 'Resetting...' : 'Reset Password'}</button>
            
            <div style={{ marginTop: '24px', textAlign: 'center' }}>
                <span style={{ color: 'var(--color-muted)', fontSize: '14px' }}>Didn't get a code? </span>
                <button type="button" className="btn-ghost" style={{ padding: '4px 12px', fontSize: '14px', border: 'none', color: 'var(--color-accent)' }} onClick={() => setView('forgot_password_email')}>Go Back</button>
            </div>
        </form>
    );

    return (
        <div className="modal-overlay" onClick={onClose}>
            <div className="modal-panel" onClick={(e) => e.stopPropagation()} style={{ maxWidth: '420px', padding: '36px' }}>
                <button className="btn-ghost" style={{ position: 'absolute', top: '16px', right: '16px', padding: '8px 12px' }} onClick={onClose}>✕</button>
                {error && <div style={{ color: 'var(--color-red)', marginBottom: '16px', fontSize: '14px', textAlign: 'center' }}>{error}</div>}
                {message && <div style={{ color: 'var(--color-accent2)', marginBottom: '16px', fontSize: '14px', textAlign: 'center' }}>{message}</div>}
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
