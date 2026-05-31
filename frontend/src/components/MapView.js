// frontend/src/components/MapView.js - Simplified Journey Route Visualization
import React from 'react';
import '../styles/MapView.css';

function MapView({ path }) {
  return (
    <div className="map-view-container">
      <div className="route-visualization">
        <h3 className="route-title">📍 Your Journey Route</h3>
        
        {path && path.length > 0 ? (
          <div className="route-steps">
            {path.map((station, index) => (
              <div key={index} className="route-step">
                {/* Step number and indicator */}
                <div className="step-indicator">
                  <div className="step-circle">
                    {index === 0 ? '🟢' : index === path.length - 1 ? '🔴' : '●'}
                  </div>
                </div>

                {/* Station info */}
                <div className="step-content">
                  <div className="step-station-name">{station}</div>
                  {index < path.length - 1 && (
                    <div className="step-connection">
                      ↓ Next Stop
                    </div>
                  )}
                </div>

                {/* Connection line */}
                {index < path.length - 1 && (
                  <div className="step-connector"></div>
                )}
              </div>
            ))}
          </div>
        ) : (
          <div className="no-route">
            <p>📍 Plan a trip to see your route</p>
          </div>
        )}

        {/* Static Map Background (Simple) */}
        <div className="simple-map-background">
          <div className="map-info">
            <p>🗺️ Islamabad-Rawalpindi Transit Network</p>
            <p className="map-hint">Trip details shown above</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default MapView;