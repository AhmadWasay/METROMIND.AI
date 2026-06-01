import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './OrderManager.css';

function OrderManager({ userId }) {
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
      <div className="order-header">
        <h2>📦 My Trip Bookings</h2>
        <p className="order-subtitle">View and manage your travel bookings</p>
      </div>

      {error && <div className="order-error">{error}</div>}

      <div className="order-tabs">
        <button 
          className={`order-tab ${activeTab === 'all' ? 'active' : ''}`}
          onClick={() => setActiveTab('all')}
        >
          All ({orders.length})
        </button>
        <button 
          className={`order-tab ${activeTab === 'pending' ? 'active' : ''}`}
          onClick={() => setActiveTab('pending')}
        >
          Pending
        </button>
        <button 
          className={`order-tab ${activeTab === 'confirmed' ? 'active' : ''}`}
          onClick={() => setActiveTab('confirmed')}
        >
          Confirmed
        </button>
        <button 
          className={`order-tab ${activeTab === 'in_transit' ? 'active' : ''}`}
          onClick={() => setActiveTab('in_transit')}
        >
          In Transit
        </button>
        <button 
          className={`order-tab ${activeTab === 'completed' ? 'active' : ''}`}
          onClick={() => setActiveTab('completed')}
        >
          Completed
        </button>
        <button 
          className={`order-tab ${activeTab === 'cancelled' ? 'active' : ''}`}
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
            <div key={order.order_id} className={`order-card status-${order.status}`}>
              <div className="order-card-header">
                <div className="order-info">
                  <h3>{order.source} → {order.destination}</h3>
                  <p className="order-id">Order: {order.order_id.slice(0, 12)}...</p>
                </div>
                <div className="order-status">
                  <span className={`status-badge status-${order.status}`}>
                    {order.status.toUpperCase()}
                  </span>
                </div>
              </div>

              <div className="order-details">
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
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <button className="close-btn" onClick={() => setSelectedOrder(null)}>×</button>
            
            <h2>Trip Details</h2>
            
            <div className="modal-section">
              <h3>Journey Route</h3>
              <p><strong>From:</strong> {selectedOrder.source}</p>
              <p><strong>To:</strong> {selectedOrder.destination}</p>
            </div>

            <div className="modal-section">
              <h3>Current Status</h3>
              <p><strong>Status:</strong> {selectedOrder.current_status || selectedOrder.status}</p>
              <p><strong>Progress:</strong> {selectedOrder.progress_percentage}%</p>
              <div className="progress-bar">
                <div className="progress-fill" style={{ width: `${selectedOrder.progress_percentage}%` }}></div>
              </div>
            </div>

            {selectedOrder.current_location && (
              <div className="modal-section">
                <h3>Current Location</h3>
                <p><strong>Location:</strong> {selectedOrder.current_location.description}</p>
                <p><strong>Coordinates:</strong> {selectedOrder.current_location.lat}, {selectedOrder.current_location.lng}</p>
              </div>
            )}

            <div className="modal-section">
              <h3>Estimated Arrival</h3>
              <p className="big-text">{selectedOrder.estimated_arrival}</p>
              <p>Next Milestone: {selectedOrder.next_milestone || 'On Track'}</p>
            </div>

            <button className="modal-close-btn" onClick={() => setSelectedOrder(null)}>
              Close
            </button>
          </div>
        </div>
      )}

      {/* Rating Modal */}
      {showRatingModal && selectedOrder && (
        <div className="modal-overlay" onClick={() => setShowRatingModal(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <button className="close-btn" onClick={() => setShowRatingModal(false)}>×</button>
            
            <h2>Rate Your Trip</h2>
            <p className="rating-subtitle">{selectedOrder.source} → {selectedOrder.destination}</p>

            <div className="rating-section">
              <label>How would you rate this trip?</label>
              <div className="star-rating">
                {[1, 2, 3, 4, 5].map(star => (
                  <button
                    key={star}
                    className={`star-btn ${star <= ratingData.rating ? 'active' : ''}`}
                    onClick={() => setRatingData({ ...ratingData, rating: star })}
                  >
                    ⭐
                  </button>
                ))}
              </div>
              <p className="rating-value">{ratingData.rating} out of 5 stars</p>
            </div>

            <div className="review-section">
              <label>Additional Review (Optional)</label>
              <textarea
                value={ratingData.review}
                onChange={(e) => setRatingData({ ...ratingData, review: e.target.value })}
                placeholder="Share your experience..."
                rows="4"
              />
            </div>

            <div className="modal-actions">
              <button className="btn-primary" onClick={handleRateOrder}>
                Submit Rating
              </button>
              <button className="btn-secondary" onClick={() => setShowRatingModal(false)}>
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
