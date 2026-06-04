import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './OrderManager.css';

function OrderManager({ userId, onReuseRoute }) {
  const [orders, setOrders] = useState([]);
  const [activeTab, setActiveTab] = useState('all');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [selectedOrder, setSelectedOrder] = useState(null);
  const [showRatingModal, setShowRatingModal] = useState(false);
  const [ratingData, setRatingData] = useState({ rating: 5, review: '' });

  const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:5000';

  const fetchOrders = async (status = null) => {
    setLoading(true);
    try {
      let url = `${API_BASE}/api/orders/user/${userId}`;
      if (status) url += `?status=${status}`;
      
      const response = await axios.get(url, {
        headers: { 'X-User-ID': userId }
      });
      setOrders(response.data.orders || []);
    } catch (err) {
      setError('Failed to load orders');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleCancelOrder = async (orderId) => {
    if (window.confirm('Are you sure you want to cancel this booking? Seats will be released and you\'ll receive a confirmation email.')) {
      try {
        const reason = prompt('Cancellation reason (optional):') || 'User requested';
        
        await axios.post(
          `${API_BASE}/api/orders/${orderId}/cancel`,
          { reason },
          { headers: { 'X-User-ID': userId } }
        );
        
        alert('Order cancelled successfully');
        fetchOrders();
      } catch (err) {
        alert('Failed to cancel order: ' + err.response?.data?.error);
      }
    }
  };

  const handleStartTrip = async (orderId) => {
    try {
      await axios.post(
        `${API_BASE}/api/orders/${orderId}/start`,
        {},
        { headers: { 'X-User-ID': userId } }
      );
      
      alert('🚀 Trip started! Have a safe journey.');
      fetchOrders();
    } catch (err) {
      alert('Failed to start trip: ' + err.response?.data?.error);
    }
  };

  const handleRateOrder = async () => {
    try {
      await axios.post(
        `${API_BASE}/api/orders/${selectedOrder.order_id}/rate`,
        {
          rating: ratingData.rating,
          review: ratingData.review
        },
        { headers: { 'X-User-ID': userId } }
      );
      
      alert('Thank you for your feedback!');
      setShowRatingModal(false);
      setSelectedOrder(null);
      fetchOrders();
    } catch (err) {
      alert('Failed to submit rating: ' + err.response?.data?.error);
    }
  };

  const handleCheckStatus = async (orderId) => {
    try {
      const response = await axios.get(
        `${API_BASE}/api/orders/${orderId}/status`,
        { headers: { 'X-User-ID': userId } }
      );
      setSelectedOrder({ ...response.data, order_id: orderId });
    } catch (err) {
      alert('Failed to fetch status: ' + err.response?.data?.error);
    }
  };

  useEffect(() => {
    if (userId) {
      if (activeTab === 'all') fetchOrders();
      else fetchOrders(activeTab);
    }
  }, [userId, activeTab]);

  const filteredOrders = activeTab === 'all' ? orders : orders.filter(o => o.status === activeTab);

  return (
    <div className="order-manager">
      <div style={{ marginBottom: '48px' }}>
        <div className="s-label">MY BOOKINGS</div>
        <h2 className="s-h2">Manage Your Trips</h2>
        <p className="s-sub">View and manage your travel bookings</p>
      </div>

      {error && <div className="order-error">{error}</div>}

      <div className="tab-navigation" style={{ marginBottom: '32px', flexWrap: 'wrap' }}>
        <button 
          className={`tab-btn ${activeTab === 'all' ? 'active' : ''}`}
          onClick={() => setActiveTab('all')}
        >
          All ({orders.length})
        </button>
        <button 
          className={`tab-btn ${activeTab === 'pending' ? 'active' : ''}`}
          onClick={() => setActiveTab('pending')}
        >
          Pending
        </button>
        <button 
          className={`tab-btn ${activeTab === 'confirmed' ? 'active' : ''}`}
          onClick={() => setActiveTab('confirmed')}
        >
          Confirmed
        </button>
        <button 
          className={`tab-btn ${activeTab === 'in_transit' ? 'active' : ''}`}
          onClick={() => setActiveTab('in_transit')}
        >
          In Transit
        </button>
        <button 
          className={`tab-btn ${activeTab === 'completed' ? 'active' : ''}`}
          onClick={() => setActiveTab('completed')}
        >
          Completed
        </button>
        <button 
          className={`tab-btn ${activeTab === 'cancelled' ? 'active' : ''}`}
          onClick={() => setActiveTab('cancelled')}
        >
          Cancelled
        </button>
      </div>

      {loading ? (
        <div className="loading">Loading your bookings...</div>
      ) : filteredOrders.length === 0 ? (
        <div className="empty-orders">
          <p>No {activeTab !== 'all' ? activeTab + ' ' : ''}bookings yet</p>
          <p className="empty-subtitle">Start planning your next trip!</p>
        </div>
      ) : (
        <div className="orders-list">
          {filteredOrders.map((order) => (
            <div key={order.order_id} className="card" style={{ display: 'flex', flexDirection: 'column', gap: '16px', marginBottom: '16px' }}>
              <div className="order-card-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div className="order-info" style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <h3 style={{ fontSize: '20px', margin: 0, fontFamily: 'Syne, sans-serif' }}>{order.source} → {order.destination}</h3>
                  <p className="order-id" style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: '12px', color: 'var(--color-accent2)', margin: 0 }}>Order: {order.order_id.slice(0, 12)}...</p>
                </div>
                <div className="order-status">
                  <span className={`status-badge ${order.status}`}>
                    {order.status.toUpperCase()}
                  </span>
                </div>
              </div>

              <div className="order-details" style={{ display: 'flex', gap: '24px', color: 'var(--color-muted)', fontSize: '14px' }}>
                <div className="detail">
                  <span className="label">Trip Date:</span>
                  <span className="value">{order.trip_date}</span>
                </div>
                <div className="detail">
                  <span className="label">Total Fare:</span>
                  <span className="value">Rs. {order.total_fare}</span>
                </div>
                <div className="detail">
                  <span className="label">Booked:</span>
                  <span className="value">{new Date(order.booking_time).toLocaleDateString()}</span>
                </div>
              </div>

              {order.rating && (
                <div className="order-rating">
                  <span className="your-rating">Your Rating: ⭐ {order.rating}/5</span>
                  {order.review && <p className="review">{order.review}</p>}
                </div>
              )}

              <div className="order-actions">
                {(order.status === 'pending' || order.status === 'confirmed') && (
                  <button 
                    className="action-btn btn-primary"
                    onClick={() => handleStartTrip(order.order_id)}
                  >
                    🚀 Start Trip
                  </button>
                )}

                {order.status === 'pending' && (
                  <button 
                    className="action-btn btn-danger"
                    onClick={() => handleCancelOrder(order.order_id)}
                  >
                    ✕ Cancel Booking
                  </button>
                )}
                
                {order.status === 'in_transit' && (
                  <button 
                    className="action-btn btn-primary"
                    onClick={() => handleCheckStatus(order.order_id)}
                  >
                    📍 Track Live
                  </button>
                )}

                {order.status === 'completed' && !order.rating && (
                  <button 
                    className="action-btn btn-info"
                    onClick={() => {
                      setSelectedOrder(order);
                      setShowRatingModal(true);
                    }}
                  >
                    ⭐ Rate Trip
                  </button>
                )}

                {(order.status === 'completed' || order.status === 'cancelled') && (
                  <button 
                    className="action-btn btn-primary"
                    onClick={() => onReuseRoute && onReuseRoute(order.source, order.destination)}
                  >
                    🔄 Book Again
                  </button>
                )}

                <button 
                  className="action-btn btn-secondary"
                  onClick={() => handleCheckStatus(order.order_id)}
                >
                  📋 View Details
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Order Detail Modal */}
      {selectedOrder && !showRatingModal && (
        <div className="modal-overlay" onClick={() => setSelectedOrder(null)}>
          <div className="modal-panel" onClick={(e) => e.stopPropagation()}>
            <button className="btn-ghost" style={{ position: 'absolute', top: '16px', right: '16px', padding: '8px 12px' }} onClick={() => setSelectedOrder(null)}>✕</button>
            
            <h2 className="s-h2" style={{ fontSize: '28px' }}>Trip Details</h2>
            
            <div className="modal-section" style={{ marginBottom: '16px' }}>
              <h3>Journey Route</h3>
              <p><strong>From:</strong> {selectedOrder.source}</p>
              <p><strong>To:</strong> {selectedOrder.destination}</p>
            </div>

            <div className="modal-section" style={{ marginBottom: '16px' }}>
              <h3>Current Status</h3>
              <p><strong>Status:</strong> {selectedOrder.current_status || selectedOrder.status}</p>
              <p><strong>Progress:</strong> {selectedOrder.progress_percentage}%</p>
              <div className="progress-bar" style={{ height: '8px', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', marginTop: '8px', overflow: 'hidden' }}>
                <div className="progress-fill" style={{ height: '100%', background: 'var(--color-accent)', width: `${selectedOrder.progress_percentage}%`, transition: 'width 0.5s' }}></div>
              </div>
            </div>

            {selectedOrder.current_location && (
              <div className="modal-section" style={{ marginBottom: '16px' }}>
                <h3>Current Location</h3>
                <p><strong>Location:</strong> {selectedOrder.current_location.description}</p>
                <p><strong>Coordinates:</strong> {selectedOrder.current_location.lat}, {selectedOrder.current_location.lng}</p>
              </div>
            )}

            <div className="modal-section" style={{ marginBottom: '24px' }}>
              <h3>Estimated Arrival</h3>
              <p className="big-text" style={{ fontSize: '24px', fontFamily: 'Syne, sans-serif', color: 'var(--color-accent2)', margin: '8px 0' }}>{selectedOrder.estimated_arrival}</p>
              <p>Next Milestone: {selectedOrder.next_milestone || 'On Track'}</p>
            </div>

            <button className="btn-ghost" style={{ width: '100%' }} onClick={() => setSelectedOrder(null)}>
              Close
            </button>
          </div>
        </div>
      )}

      {/* Rating Modal */}
      {showRatingModal && selectedOrder && (
        <div className="modal-overlay" onClick={() => setShowRatingModal(false)}>
          <div className="modal-panel" onClick={(e) => e.stopPropagation()}>
            <button className="btn-ghost" style={{ position: 'absolute', top: '16px', right: '16px', padding: '8px 12px' }} onClick={() => setShowRatingModal(false)}>✕</button>
            
            <h2 className="s-h2" style={{ fontSize: '28px' }}>Rate Your Trip</h2>
            <p className="s-sub" style={{ marginBottom: '24px' }}>{selectedOrder.source} → {selectedOrder.destination}</p>

            <div className="rating-section">
              <label>How would you rate this trip?</label>
              <div className="star-rating" style={{ display: 'flex', gap: '8px', margin: '12px 0' }}>
                {[1, 2, 3, 4, 5].map(star => (
                  <button
                    key={star}
                    className={`btn-ghost ${star <= ratingData.rating ? 'active' : ''}`}
                    style={{ padding: '8px', borderColor: star <= ratingData.rating ? 'var(--color-accent)' : '' }}
                    onClick={() => setRatingData({ ...ratingData, rating: star })}
                  >
                    ⭐
                  </button>
                ))}
              </div>
              <p className="rating-value" style={{ fontSize: '14px', color: 'var(--color-muted)' }}>{ratingData.rating} out of 5 stars</p>
            </div>

            <div className="review-section" style={{ marginTop: '24px', marginBottom: '24px' }}>
              <label>Additional Review (Optional)</label>
              <textarea
                className="input-field"
                style={{ marginTop: '8px' }}
                value={ratingData.review}
                onChange={(e) => setRatingData({ ...ratingData, review: e.target.value })}
                placeholder="Share your experience..."
                rows="4"
              />
            </div>

            <div className="modal-actions" style={{ display: 'flex', gap: '12px' }}>
              <button className="btn-primary" onClick={handleRateOrder}>
                Submit Rating
              </button>
              <button className="btn-ghost" onClick={() => setShowRatingModal(false)}>
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default OrderManager;
