// frontend/src/components/ItineraryCard.js - Display trip details with walking distances
import React, { useState } from 'react';
import '../styles/ItineraryCard.css';

function ItineraryCard({ itineraryPackage, isPrimary, loading }) {
  const [showDetails, setShowDetails] = useState(isPrimary);

  return (
    <div className={`itinerary-card ${isPrimary ? 'primary' : 'alternative'}`}>
      <div className="card-header">
        <h3>{isPrimary ? '⭐ RECOMMENDED' : '📍 ALTERNATIVE'} - {itineraryPackage.name}</h3>
        {isPrimary && <span className="badge">Best Value</span>}
      </div>

      <div className="card-content">
        {/* Main Info Cards */}
        <div className="main-info">
          <div className="info-box">
            <span className="label">⏱️ Total Time</span>
            <span className="value">{itineraryPackage.estimated_time_minutes} mins</span>
          </div>

          <div className="info-box">
            <span className="label">💰 Cost</span>
            <span className="value">PKR {itineraryPackage.estimated_cost || 20}</span>
          </div>

          <div className="info-box">
            <span className="label">🚶 Walking</span>
            <span className="value">{itineraryPackage.walking_distance_km || 0} km</span>
          </div>

          <div className="info-box">
            <span className="label">🔄 Transfers</span>
            <span className="value">{itineraryPackage.transfers || 0}</span>
          </div>
        </div>

        {/* Time Breakdown */}
        {showDetails && itineraryPackage.transit_time_mins !== undefined && (
          <div className="time-breakdown">
            <strong>⏱️ Time Breakdown:</strong>
            <div className="breakdown-items">
              <div className="breakdown-item">
                <span>🚌 Transit Time:</span>
                <span className="value">{itineraryPackage.transit_time_mins} mins</span>
              </div>
              <div className="breakdown-item">
                <span>🚶 Walking Time:</span>
                <span className="value">{itineraryPackage.walking_time_mins} mins</span>
              </div>
            </div>
          </div>
        )}

        {/* Journey Segments */}
        {showDetails && itineraryPackage.journey_segments && itineraryPackage.journey_segments.length > 0 && (
          <div className="journey-segments">
            <strong>📍 Full Journey:</strong>
            <div className="segments-list">
              {itineraryPackage.journey_segments.map((segment, idx) => (
                <div key={idx} className={`segment segment-${segment.type}`}>
                  <div className="segment-header">
                    <span className="segment-type-badge">{segment.type.toUpperCase()}</span>
                    <span className="segment-description">{segment.description}</span>
                  </div>
                  <div className="segment-details">
                    <span className="from-to">
                      {segment.from} → {segment.to}
                    </span>
                    <div className="segment-info">
                      <span className="time">⏱️ {segment.time_mins} mins</span>
                      {segment.distance_km > 0 && (
                        <span className="distance">📏 {segment.distance_km} km</span>
                      )}
                      {segment.walking_time_mins > 0 && (
                        <span className="walking">🚶 {segment.walking_time_mins} mins walk</span>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Lines Used */}
        {showDetails && itineraryPackage.lines_used && itineraryPackage.lines_used.length > 0 && (
          <div className="lines-used">
            <strong>🚆 Lines/Routes:</strong>
            <div className="line-badges">
              {itineraryPackage.lines_used.map((line, idx) => (
                <span key={idx} className="line-badge">{line}</span>
              ))}
            </div>
          </div>
        )}

        {/* Availability */}
        {showDetails && itineraryPackage.inventory_status && (
          <div className="availability-info">
            <strong>🪑 Seat Availability:</strong>
            <span className={`availability-${itineraryPackage.inventory_status.status.toLowerCase()}`}>
              {itineraryPackage.inventory_status.available} seats available
            </span>
          </div>
        )}

        {/* Description */}
        {showDetails && itineraryPackage.description && (
          <p className="description">{itineraryPackage.description}</p>
        )}

        <button 
          className="toggle-details-btn"
          onClick={() => setShowDetails(!showDetails)}
        >
          {showDetails ? '▼ Hide Details' : '▶ Show Details'}
        </button>
      </div>

      {/* The booking feature has been disabled to focus on the trip planning functionality. */}

    </div>
  );
}

export default ItineraryCard;
