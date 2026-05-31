// frontend/src/App.js - Trip Planner UI
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MapView from './components/MapView';
import SearchBar from './components/SearchBar';
import ItineraryCard from './components/ItineraryCard';
import './App.css';

function App() {
  const [source, setSource] = useState('');
  const [destination, setDestination] = useState('');
  const [routeResult, setRouteResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [locations, setLocations] = useState([]);
  const [showMap, setShowMap] = useState(true);
  const [currentTab, setCurrentTab] = useState('search');

  // GOOD (Only declared once)
  const API_BASE = process.env.REACT_APP_API_URL;

  useEffect(() => {
    const fetchLocations = async () => {
      try {
        const response = await axios.get(`${API_BASE}/api/locations`);
        const locs = response.data.locations || [];
        setLocations(locs);

        // Ensure default source/destination are valid selectable codes
        if (locs.length > 0) {
          const codes = locs.map(l => l.code);
          if (!codes.includes(source)) {
            setSource(codes[0]);
          }
          if (!codes.includes(destination)) {
            setDestination(codes.length > 1 ? codes[1] : codes[0]);
          }
        }
      } catch (err) {
        console.error('Error fetching locations:', err);
      }
    };

    fetchLocations();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const calculateRoute = async () => {
    if (!source || !destination) {
      setError('Please select both source and destination');
      return;
    }

    if (source === destination) {
      setError('Source and destination cannot be the same');
      return;
    }

    setLoading(true);
    setError(null);
    
    try {
      const response = await axios.post(`${API_BASE}/api/plan-trip`, {
        source: source,
        destination: destination,
        optimization: 'time'
      });
      
      if (response.data.status === 'success') {
        setRouteResult(response.data);
        setCurrentTab('results');
        setShowMap(true);
      } else {
        setError(response.data.message || 'Failed to plan trip');
      }
    } catch (err) {
      setError(`Error: ${err.response?.data?.message || err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>🚇 MetroMind - Trip Planner</h1>
        <p>Plan your journey in Islamabad-Rawalpindi</p>
      </header>

      <div className="app-container">
        {/* Tab Navigation */}
        <div className="tab-navigation">
          <button
            className={`tab-btn ${currentTab === 'search' ? 'active' : ''}`}
            onClick={() => setCurrentTab('search')}
          >
            🔍 Plan Trip
          </button>
          <button
            className={`tab-btn ${currentTab === 'results' ? 'active' : ''}`}
            onClick={() => currentTab === 'search' || setCurrentTab('results')}
            disabled={!routeResult}
          >
            📍 Results
          </button>
          {/* The booking feature has been disabled as it's not part of the core trip planner */}
        </div>

        {/* Search Tab */}
        {currentTab === 'search' && (
          <div className="search-section">
            <SearchBar
              source={source}
              destination={destination}
              onSourceChange={setSource}
              onDestinationChange={setDestination}
              onSearch={calculateRoute}
              stations={locations}
              loading={loading}
            />
            {error && <div className="error-message">⚠️ {error}</div>}
            <div className="map-wrapper-search">
              <MapView path={[]} />
            </div>
          </div>
        )}

        {/* Results Tab */}
        {currentTab === 'results' && routeResult && (
          <div className="results-section">
            <h2>
              Trip from <strong>{source.replace(/_/g, ' ')}</strong> to <strong>{destination.replace(/_/g, ' ')}</strong>
            </h2>
            
            {showMap && routeResult.packages.length > 0 && (
              <MapView path={routeResult.packages[0].path} />
            )}

            <div className="itineraries">
              {routeResult.packages.map((pkg, idx) => (
                <ItineraryCard
                  key={idx}
                  itineraryPackage={pkg}
                  isPrimary={idx === 0}
                  loading={loading}
                />
              ))}
            </div>
          </div>
        )}
      </div>

      <footer className="app-footer">
        <p>🚌 Real Islamabad-Rawalpindi Metro & Feeder Routes • Make your commute smart</p>
      </footer>
    </div>
  );
}

export default App;