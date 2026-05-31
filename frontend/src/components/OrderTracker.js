// frontend/src/components/OrderTracker.js
import React, { useEffect, useState } from 'react';
import '../styles/OrderTracker.css';

function OrderTracker({ order, onCancel, loading }) {
  const [trackingStatus, setTrackingStatus] = useState('Awaiting Transport');
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    // Simulate real-time tracking
    const interval = setInterval(() => {
      setProgress(prev => Math.min(prev + Math.random() * 20, 100));
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  const getStatusEmoji = (status) => {
    const statusMap = {
      'Awaiting Transport': '⏳',
      'Boarded First Bus': '🚌',
      'Transferring at Hub': '🚶',
      'On Final Leg': '🚇',
      'Destination Reached': '✅'
    };
    return statusMap[status] || '📍';
  };

  const statuses = [
    'Awaiting Transport',
    'Boarded First Bus',
    'Transferring at Hub',
    'On Final Leg',
    'Destination Reached'
  ];

  return (
    <div className="order-tracker-container">
      <div className="order-header">
        <h2>📦 Order Confirmation</h2>
        <div className="order-id">Order ID: <strong>{order.order_id}</strong></div>
      </div>

      <div className="order-details">
        <div className="detail-item">
          <span className="label">Booked At:</span>
          <span className="value">{new Date(order.booked_at).toLocaleTimeString()}</span>
        </div>
        <div className="detail-item">
          <span className="label">Expires At:</span>
          <span className="value">{new Date(order.expires_at).toLocaleTimeString()}</span>
        </div>
        <div className="detail-item">
          <span className="label">Passengers:</span>
          <span className="value">{order.passengers}</span>
        </div>
        <div className="detail-item">
          <span className="label">Payment Status:</span>
          <span className={`value status-${order.payment_status}`}>
            {order.payment_status.toUpperCase()}
          </span>
        </div>
      </div>

      <div className="tracking-section">
        <h3>🗺️ Live Trip Status</h3>
        
        <div className="status-timeline">
          {statuses.map((status, idx) => (
            <div key={idx} className={`timeline-step ${idx <= Math.floor(progress / 20) ? 'completed' : ''}`}>
              <div className="step-circle">{getStatusEmoji(status)}</div>
              <div className="step-label">{status}</div>
            </div>
          ))}
        </div>

        <div className="progress-bar">
          <div className="progress-fill" style={{ width: `${progress}%` }}></div>
        </div>
        <p className="progress-text">Trip progress: {Math.floor(progress)}%</p>
      </div>

      <div className="current-status">
        <h3>📍 Current Location</h3>
        <div className="location-info">
          <p><strong>Next Stop:</strong> PIMS Medical Complex</p>
          <p><strong>Estimated Arrival:</strong> 08:35 AM (+3 mins)</p>
          <p><strong>Driver:</strong> Muhammad Ali | Rating: ⭐⭐⭐⭐⭐</p>
        </div>
      </div>

      <div className="rider-contact">
        <h3>👤 Rider Information</h3>
        <div className="rider-card">
          <div className="rider-avatar">👨</div>
          <div className="rider-details">
            <p><strong>Bus Driver</strong></p>
            <p>License: PK-1234567</p>
            <button className="contact-btn">📞 Call Driver</button>
          </div>
        </div>
      </div>

      <div className="action-buttons">
        <button className="btn-secondary">💬 Message Support</button>
        <button 
          className="btn-danger"
          onClick={onCancel}
          disabled={loading}
        >
          {loading ? '⏳ Cancelling...' : '❌ Cancel Order'}
        </button>
      </div>

      <div className="post-trip-info">
        <p>💡 After your trip, you'll be able to rate your experience and help improve our AI.</p>
      </div>
    </div>
  );
}

export default OrderTracker;