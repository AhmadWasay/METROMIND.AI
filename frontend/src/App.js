// frontend/src/App.js - Trip Planner UI with Authentication & Booking
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MapView from './components/MapView';
import SearchBar from './components/SearchBar';
import ItineraryCard from './components/ItineraryCard';
import AuthModal from './components/AuthModal';
import OrderManager from './components/OrderManager';
import AdminDashboard from './components/AdminDashboard';
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
  const [userId, setUserId] = useState(localStorage.getItem('user_id'));
  const [showAuthModal, setShowAuthModal] = useState(false);
  const [currentPage, setCurrentPage] = useState('planner');

  // GOOD (Only declared once)
  const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:5000';

  // Check authentication on mount
  useEffect(() => {
    const storedUserId = localStorage.getItem('user_id');
    if (storedUserId) {
      setUserId(storedUserId);
    }
  }, []);

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

  const handleBookTrip = async (tripPlan, totalFare) => {
    if (!userId) {
      setShowAuthModal(true);
      return;
    }
    
    try {
      const response = await axios.post(
        `${API_BASE}/api/orders/create`,
        {
          source,
          destination,
          trip_plan: tripPlan,
          trip_date: new Date().toISOString().split('T')[0],
          total_fare: totalFare
        },
        { headers: { 'X-User-ID': userId } }
      );
      
      if (response.data.status === 'success') {
        alert('✅ Trip booked successfully! Check your email for confirmation.');
        setCurrentPage('orders');
      }
    } catch (err) {
      alert('Failed to book trip: ' + err.response?.data?.error);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('user_id');
    setUserId(null);
    setCurrentPage('planner');
  };

  const calculateRoute = async () => {
    if (!source || !destination) {
      alert('Please select source and destination');
      return;
    }
    
    setLoading(true);
    setError('');
    
    try {
      const response = await axios.post(`${API_BASE}/api/plan-trip`, {
        source,
        destination,
        optimization: 'time'
      });
      
      if (response.data && response.data.packages) {
        setRouteResult(response.data);
        setCurrentTab('results');
      } else {
        setError('No routes found. Try different locations.');
      }
    } catch (err) {
      setError('Error planning trip: ' + (err.response?.data?.error || err.message));
    } finally {
      setLoading(false);
    }
  };

  // Render Admin Panel
  if (currentPage === 'admin') {
    return <AdminDashboard />;
  }

  // Render Orders Page
  if (currentPage === 'orders' && userId) {
    return (
      <div className="app">
        <header className="app-header">
          <div className="header-content">
            <h1>🚇 MetroMind AI</h1>
            <div className="header-nav">
              <button 
                className="nav-btn"
                onClick={() => setCurrentPage('planner')}
              >
                🔍 Plan Trip
              </button>
              <button 
                className="nav-btn active"
                onClick={() => setCurrentPage('orders')}
              >
                📦 My Bookings
              </button>
              <button 
                className="nav-btn"
                onClick={() => setCurrentPage('admin')}
              >
                🎛️ Admin
              </button>
              <button 
                className="nav-btn logout"
                onClick={handleLogout}
              >
                🚪 Logout
              </button>
            </div>
          </div>
        </header>
        <OrderManager userId={userId} />
      </div>
    );
  }

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <h1>🚇 MetroMind AI - Intelligent Transit Planner</h1>
          <div className="header-nav">
            <button 
              className="nav-btn active"
              onClick={() => setCurrentPage('planner')}
            >
              🔍 Plan Trip
            </button>
            {userId ? (
              <>
                <button 
                  className="nav-btn"
                  onClick={() => setCurrentPage('orders')}
                >
                  📦 My Bookings
                </button>
                <button 
                  className="nav-btn"
                  onClick={() => setCurrentPage('admin')}
                >
                  🎛️ Admin
                </button>
                <button 
                  className="nav-btn logout"
                  onClick={handleLogout}
                >
                  🚪 Logout
                </button>
              </>
            ) : (
              <button 
                className="nav-btn login"
                onClick={() => setShowAuthModal(true)}
              >
                🔐 Login / Sign Up
              </button>
            )}
          </div>
        </div>
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
                  onBook={() => handleBookTrip(pkg, pkg.total_fare || 50)}
                  showBookButton={true}
                />
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Auth Modal */}
      {showAuthModal && (
        <AuthModal 
          onClose={() => setShowAuthModal(false)}
          onAuthSuccess={(newUserId) => {
            setUserId(newUserId);
            setShowAuthModal(false);
          }}
        />
      )}

      <footer className="app-footer">
        <p>🚌 MetroMind AI - Real Islamabad-Rawalpindi Metro & Feeder Routes • Make your commute smart</p>
      </footer>
    </div>
  );
}

export default App;