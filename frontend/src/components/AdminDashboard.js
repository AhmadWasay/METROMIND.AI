import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AdminDashboard.css';

function AdminDashboard() {
  const [adminToken, setAdminToken] = useState(localStorage.getItem('admin_token') || '');
  const [isAuthenticated, setIsAuthenticated] = useState(!!adminToken);
  const [activeTab, setActiveTab] = useState('overview');
  const [dashboardData, setDashboardData] = useState(null);
  const [orders, setOrders] = useState([]);
  const [users, setUsers] = useState([]);
  const [notifications, setNotifications] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:5000';

  const handleAdminLogin = (e) => {
    e.preventDefault();
    const token = prompt('Enter Admin Token:');
    if (token) {
      localStorage.setItem('admin_token', token);
      setAdminToken(token);
      setIsAuthenticated(true);
      fetchDashboard();
    }
  };

  const fetchDashboard = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_BASE}/api/admin/dashboard`, {
        headers: { 'X-Admin-Token': adminToken }
      });
      setDashboardData(response.data);
    } catch (err) {
      setError('Failed to fetch dashboard data');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const fetchAllOrders = async (status = null) => {
    setLoading(true);
    try {
      let url = `${API_BASE}/api/admin/orders`;
      if (status) url += `?status=${status}`;
      
      const response = await axios.get(url, {
        headers: { 'X-Admin-Token': adminToken }
      });
      setOrders(response.data.orders);
    } catch (err) {
      setError('Failed to fetch orders');
    } finally {
      setLoading(false);
    }
  };

  const fetchAllUsers = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_BASE}/api/admin/users`, {
        headers: { 'X-Admin-Token': adminToken }
      });
      setUsers(response.data.users);
    } catch (err) {
      setError('Failed to fetch users');
    } finally {
      setLoading(false);
    }
  };

  const fetchPendingNotifications = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_BASE}/api/admin/notifications`, {
        headers: { 'X-Admin-Token': adminToken }
      });
      setNotifications(response.data.pending_notifications);
    } catch (err) {
      setError('Failed to fetch notifications');
    } finally {
      setLoading(false);
    }
  };

  const updateOrderStatus = async (orderId, newStatus) => {
    try {
      const message = prompt(`Enter status update message for order ${orderId}:`);
      if (message !== null) {
        await axios.put(`${API_BASE}/api/orders/${orderId}/update-status`, 
          { status: newStatus, message },
          { headers: { 'X-Admin-Token': adminToken } }
        );
        alert('Order status updated!');
        fetchAllOrders();
      }
    } catch (err) {
      alert('Failed to update order status');
    }
  };

  const sendBroadcastAlert = async () => {
    try {
      const userIds = users.filter(u => u.is_premium).map(u => u.user_id);
      const message = prompt('Enter alert message for premium users:');
      
      if (message !== null && userIds.length > 0) {
        await axios.post(`${API_BASE}/api/admin/send-alerts`,
          { user_ids: userIds, message, type: 'alert' },
          { headers: { 'X-Admin-Token': adminToken } }
        );
        alert(`Alert sent to ${userIds.length} premium users!`);
      }
    } catch (err) {
      alert('Failed to send alerts');
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('admin_token');
    setAdminToken('');
    setIsAuthenticated(false);
  };

  useEffect(() => {
    if (isAuthenticated && activeTab === 'overview') {
      fetchDashboard();
    }
  }, [isAuthenticated, activeTab]);

  if (!isAuthenticated) {
    return (
      <div className="admin-login">
        <div className="login-container">
          <h1>MetroMind Admin Portal</h1>
          <button onClick={handleAdminLogin} className="login-btn">
            Admin Login
          </button>
          <p className="hint">Contact administrator for access token</p>
        </div>
      </div>
    );
  }

  return (
    <div className="admin-dashboard">
      <div className="admin-header">
        <h1>🎛️ MetroMind Admin Dashboard</h1>
        <button onClick={handleLogout} className="logout-btn">Logout</button>
      </div>

      <div className="admin-tabs">
        <button 
          className={`tab-btn ${activeTab === 'overview' ? 'active' : ''}`}
          onClick={() => setActiveTab('overview')}
        >
          📊 Overview
        </button>
        <button 
          className={`tab-btn ${activeTab === 'orders' ? 'active' : ''}`}
          onClick={() => { setActiveTab('orders'); fetchAllOrders(); }}
        >
          📦 Orders
        </button>
        <button 
          className={`tab-btn ${activeTab === 'users' ? 'active' : ''}`}
          onClick={() => { setActiveTab('users'); fetchAllUsers(); }}
        >
          👥 Users
        </button>
        <button 
          className={`tab-btn ${activeTab === 'notifications' ? 'active' : ''}`}
          onClick={() => { setActiveTab('notifications'); fetchPendingNotifications(); }}
        >
          🔔 Notifications
        </button>
      </div>

      {error && <div className="error-message">{error}</div>}

      {/* OVERVIEW TAB */}
      {activeTab === 'overview' && dashboardData && (
        <div className="tab-content">
          <h2>Dashboard Overview</h2>
          
          <div className="stats-grid">
            <div className="stat-card">
              <h3>Total Orders</h3>
              <p className="stat-number">{dashboardData.statistics.total_orders}</p>
              <div className="status-breakdown">
                {Object.entries(dashboardData.statistics.orders_by_status).map(([status, count]) => (
                  <span key={status} className={`badge badge-${status}`}>
                    {status}: {count}
                  </span>
                ))}
              </div>
            </div>

            <div className="stat-card">
              <h3>Total Revenue</h3>
              <p className="stat-number">Rs. {dashboardData.statistics.total_revenue.toFixed(2)}</p>
              <p className="stat-subtitle">From completed bookings</p>
            </div>

            <div className="stat-card">
              <h3>Average Rating</h3>
              <p className="stat-number">⭐ {dashboardData.statistics.average_rating.toFixed(1)}</p>
              <p className="stat-subtitle">Out of 5 stars</p>
            </div>

            <div className="stat-card">
              <h3>Users</h3>
              <p className="stat-number">{dashboardData.statistics.total_users}</p>
              <p className="stat-subtitle">
                Premium: {dashboardData.statistics.premium_users}
              </p>
            </div>
          </div>

          <div className="top-routes">
            <h3>Top Routes</h3>
            <table>
              <thead>
                <tr>
                  <th>Source</th>
                  <th>Destination</th>
                  <th>Bookings</th>
                </tr>
              </thead>
              <tbody>
                {dashboardData.top_routes.map((route, idx) => (
                  <tr key={idx}>
                    <td>{route.source}</td>
                    <td>{route.destination}</td>
                    <td className="text-center">{route.bookings}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <button onClick={sendBroadcastAlert} className="broadcast-btn">
            📢 Send Alert to Premium Users
          </button>
        </div>
      )}

      {/* ORDERS TAB */}
      {activeTab === 'orders' && (
        <div className="tab-content">
          <h2>All Orders</h2>
          
          <div className="filter-buttons">
            <button onClick={() => fetchAllOrders()} className="filter-btn active">All</button>
            <button onClick={() => fetchAllOrders('pending')} className="filter-btn">Pending</button>
            <button onClick={() => fetchAllOrders('confirmed')} className="filter-btn">Confirmed</button>
            <button onClick={() => fetchAllOrders('in_transit')} className="filter-btn">In Transit</button>
            <button onClick={() => fetchAllOrders('completed')} className="filter-btn">Completed</button>
            <button onClick={() => fetchAllOrders('cancelled')} className="filter-btn">Cancelled</button>
          </div>

          {loading ? <p>Loading...</p> : (
            <table className="orders-table">
              <thead>
                <tr>
                  <th>Order ID</th>
                  <th>User</th>
                  <th>Route</th>
                  <th>Fare</th>
                  <th>Status</th>
                  <th>Date</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {orders.map((order) => (
                  <tr key={order.order_id}>
                    <td><code>{order.order_id}</code></td>
                    <td>{order.user_id}</td>
                    <td>{order.source} → {order.destination}</td>
                    <td>Rs. {order.total_fare}</td>
                    <td><span className={`badge badge-${order.status}`}>{order.status}</span></td>
                    <td>{new Date(order.booking_time).toLocaleDateString()}</td>
                    <td>
                      <select 
                        onChange={(e) => updateOrderStatus(order.order_id, e.target.value)}
                        className="status-select"
                      >
                        <option value="">Update...</option>
                        <option value="pending">Pending</option>
                        <option value="confirmed">Confirmed</option>
                        <option value="in_transit">In Transit</option>
                        <option value="completed">Completed</option>
                        <option value="cancelled">Cancelled</option>
                      </select>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      )}

      {/* USERS TAB */}
      {activeTab === 'users' && (
        <div className="tab-content">
          <h2>All Users ({users.length})</h2>
          
          {loading ? <p>Loading...</p> : (
            <table className="users-table">
              <thead>
                <tr>
                  <th>User ID</th>
                  <th>Email</th>
                  <th>Name</th>
                  <th>Phone</th>
                  <th>Status</th>
                  <th>Joined</th>
                  <th>Last Login</th>
                </tr>
              </thead>
              <tbody>
                {users.map((user) => (
                  <tr key={user.user_id}>
                    <td><code>{user.user_id}</code></td>
                    <td>{user.email}</td>
                    <td>{user.full_name}</td>
                    <td>{user.phone || '-'}</td>
                    <td>
                      <span className={`badge ${user.is_premium ? 'badge-premium' : 'badge-regular'}`}>
                        {user.is_premium ? '⭐ Premium' : 'Regular'}
                      </span>
                    </td>
                    <td>{new Date(user.created_at).toLocaleDateString()}</td>
                    <td>{user.last_login ? new Date(user.last_login).toLocaleDateString() : 'Never'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      )}

      {/* NOTIFICATIONS TAB */}
      {activeTab === 'notifications' && (
        <div className="tab-content">
          <h2>Pending Notifications ({notifications.length})</h2>
          
          {loading ? <p>Loading...</p> : notifications.length === 0 ? (
            <p className="empty-message">No pending notifications</p>
          ) : (
            <div className="notifications-list">
              {notifications.map((notif) => (
                <div key={notif.notification_id} className="notification-card">
                  <h4>{notif.notification_type}</h4>
                  <p><strong>Order:</strong> {notif.order_id}</p>
                  <p><strong>Channel:</strong> {notif.channel}</p>
                  <p><strong>Message:</strong> {notif.message}</p>
                  <p><strong>Status:</strong> {notif.status}</p>
                  <p className="timestamp">{new Date(notif.created_at).toLocaleString()}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default AdminDashboard;
