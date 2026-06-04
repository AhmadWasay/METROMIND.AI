// frontend/src/App.js - Trip Planner UI with Authentication & Booking
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MapView from './components/MapView';
import SearchBar from './components/SearchBar';
import ItineraryCard from './components/ItineraryCard';
import AuthModal from './components/AuthModal';
import OrderManager from './components/OrderManager';
import AdminDashboard from './components/AdminDashboard';
import './styles/design-system.css';

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
  const [currentPage, setCurrentPage] = useState('landing');

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

  // Design System Custom Cursor & Interaction
  useEffect(() => {
    const cursor = document.getElementById('cursor');
    const cursorRing = document.getElementById('cursor-ring');
    let mouseX = 0, mouseY = 0;
    let ringX = 0, ringY = 0;

    const onMouseMove = (e) => {
      mouseX = e.clientX; mouseY = e.clientY;
      if (cursor) { cursor.style.left = `${mouseX}px`; cursor.style.top = `${mouseY}px`; }
    };

    const render = () => {
      ringX += (mouseX - ringX) * 0.12; ringY += (mouseY - ringY) * 0.12;
      if (cursorRing) { cursorRing.style.left = `${ringX}px`; cursorRing.style.top = `${ringY}px`; }
      requestAnimationFrame(render);
    };

    window.addEventListener('mousemove', onMouseMove);
    let rafId = requestAnimationFrame(render);

    const handleMouseOver = (e) => {
      if (e.target.tagName.toLowerCase() === 'a' || e.target.tagName.toLowerCase() === 'button' || e.target.closest('button') || e.target.closest('a')) {
        cursor?.classList.add('hover');
      } else { cursor?.classList.remove('hover'); }
    };
    window.addEventListener('mouseover', handleMouseOver);

    return () => {
      window.removeEventListener('mousemove', onMouseMove);
      window.removeEventListener('mouseover', handleMouseOver);
      cancelAnimationFrame(rafId);
    };
  }, []);

  const calculateRoute = async () => {
    if (!userId) {
      setShowAuthModal(true);
      return;
    }

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

  return (
    <div className="app-shell">
      {/* Custom Cursor UI */}
      <div id="cursor"></div>
      <div id="cursor-ring"></div>

      {/* Section 3.2: Ticker Banner */}
      <div className="ticker-banner">
        <div className="ticker-track">
          <span>🟢 Green Line running on schedule</span>
          <span>🔴 Red Line delay at Faizabad</span>
          <span>🔵 Blue Line normal service</span>
          <span>⚡ Pindi EVs fully charged</span>
          <span>🟢 Green Line running on schedule</span>
          <span>🔴 Red Line delay at Faizabad</span>
          <span>🔵 Blue Line normal service</span>
          <span>⚡ Pindi EVs fully charged</span>
        </div>
      </div>

      {/* Section 3.3: Navigation Bar */}
      <nav className="nav-pill-bar">
        <button className="nav-left" style={{ background: 'none', border: 'none', padding: 0, color: 'inherit', display: 'flex', alignItems: 'center', gap: '12px' }} onClick={() => setCurrentPage('landing')}>
          <div className="logo-mark"></div>
          <span className="wordmark">MetroMind</span>
        </button>
        <div className="nav-center">
          <button className={`nav-link ${currentPage === 'planner' ? 'active' : ''}`} onClick={() => setCurrentPage('planner')}>Plan Trip</button>
          {userId && (
            <>
              <button className={`nav-link ${currentPage === 'orders' ? 'active' : ''}`} onClick={() => setCurrentPage('orders')}>My Bookings</button>
              <button className={`nav-link ${currentPage === 'admin' ? 'active' : ''}`} onClick={() => setCurrentPage('admin')}>Admin</button>
            </>
          )}
        </div>
        <div className="nav-right">
          {userId ? (
            <button className="btn-pill ghost" onClick={handleLogout}>Log Out</button>
          ) : (
            <button className="btn-pill filled" onClick={() => setShowAuthModal(true)}>Log In →</button>
          )}
        </div>
      </nav>

      <main className="main-content">
        {currentPage === 'landing' && (
          <div className="landing-view">
            <section className="section" style={{ background: 'var(--color-ink)', padding: '160px 24px 120px' }}>
              <div className="section-inner" style={{ maxWidth: '1160px', margin: '0 auto', textAlign: 'center' }}>
                <div className="s-label" style={{ animation: 'fade-up 0.8s 0s both cubic-bezier(0.16,1,0.3,1)' }}>IIUI WEB ENGINEERING 2026</div>
                <h1 style={{ fontSize: 'clamp(48px, 8vw, 96px)', fontFamily: 'Syne, sans-serif', margin: '24px 0', lineHeight: 1.1, animation: 'fade-up 0.8s 0.1s both cubic-bezier(0.16,1,0.3,1)' }}>
                  Commute <span style={{ color: 'var(--color-accent)' }}>Smarter</span>,<br/>Not Harder.
                </h1>
                <p className="s-sub" style={{ maxWidth: '600px', margin: '0 auto 48px', fontSize: '19px', animation: 'fade-up 0.8s 0.2s both cubic-bezier(0.16,1,0.3,1)' }}>
                  MetroMind AI optimizes your transit paths across Islamabad & Rawalpindi. Find the fastest routes, book tickets, and track your journey in real-time.
                </p>
                <div style={{ display: 'flex', gap: '16px', justifyContent: 'center', animation: 'fade-up 0.8s 0.3s both cubic-bezier(0.16,1,0.3,1)' }}>
                  <button className="btn-primary" onClick={() => setCurrentPage('planner')}>Plan Your Trip →</button>
                  <button className="btn-ghost" onClick={() => document.getElementById('how-it-works').scrollIntoView({behavior: 'smooth'})}>How it Works</button>
                </div>
              </div>
            </section>

            <section id="how-it-works" className="section" style={{ background: 'var(--color-surface)', padding: '120px 24px' }}>
              <div className="section-inner" style={{ maxWidth: '1160px', margin: '0 auto' }}>
                <div className="s-label">HOW IT WORKS</div>
                <h2 className="s-h2">Seamless Transit Experience</h2>
                <p className="s-sub">Three simple steps to your destination.</p>
                
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '24px' }}>
                  <div className="card" style={{ animation: 'fade-up 0.8s 0.1s both' }}>
                    <div style={{ fontSize: '32px', marginBottom: '16px' }}>🔍</div>
                    <h3 style={{ fontSize: '22px', fontFamily: 'Syne, sans-serif', marginBottom: '12px', color: 'var(--color-white)' }}>1. Search</h3>
                    <p style={{ color: 'var(--color-muted)', fontSize: '14px', lineHeight: 1.6 }}>Enter your source and destination. Our AI graph engine calculates the fastest, cheapest, and most efficient routes.</p>
                  </div>
                  <div className="card" style={{ animation: 'fade-up 0.8s 0.2s both' }}>
                    <div style={{ fontSize: '32px', marginBottom: '16px' }}>🎫</div>
                    <h3 style={{ fontSize: '22px', fontFamily: 'Syne, sans-serif', marginBottom: '12px', color: 'var(--color-white)' }}>2. Book</h3>
                    <p style={{ color: 'var(--color-muted)', fontSize: '14px', lineHeight: 1.6 }}>Select your preferred itinerary and book your trip. We manage inventory to ensure you have a guaranteed spot.</p>
                  </div>
                  <div className="card" style={{ animation: 'fade-up 0.8s 0.3s both' }}>
                    <div style={{ fontSize: '32px', marginBottom: '16px' }}>📍</div>
                    <h3 style={{ fontSize: '22px', fontFamily: 'Syne, sans-serif', marginBottom: '12px', color: 'var(--color-white)' }}>3. Track</h3>
                    <p style={{ color: 'var(--color-muted)', fontSize: '14px', lineHeight: 1.6 }}>Follow your journey in real-time with our live tracking system and receive SMS or email status updates.</p>
                  </div>
                </div>
              </div>
            </section>
          </div>
        )}

        {currentPage === 'admin' && (
          <section className="section" style={{ paddingTop: '120px' }}>
            <div className="section-inner"><AdminDashboard /></div>
          </section>
        )}

        {currentPage === 'orders' && userId && (
          <section className="section" style={{ paddingTop: '120px' }}>
            <div className="section-inner">
              <OrderManager 
                userId={userId} 
                onReuseRoute={(src, dst) => {
                  setSource(src);
                  setDestination(dst);
                  setCurrentTab('search');
                  setCurrentPage('planner');
                }}
              />
            </div>
          </section>
        )}

        {/* Section 5.2: Trip Planner Page (Split Panel) */}
        {currentPage === 'planner' && (
          <section className="section-planner">
            <div className="section-inner">
              <div className="s-label">TRIP PLANNER</div>
              <h2 className="s-h2">Find Your Best Route</h2>
              <p className="s-sub">AI-optimized transit paths across Islamabad & Rawalpindi.</p>

              <div className="split-panel">
                <div className="left-panel">
                  <div className="tab-navigation">
                    <button className={`tab-btn ${currentTab === 'search' ? 'active' : ''}`} onClick={() => setCurrentTab('search')}>🔍 Plan Trip</button>
                    <button className={`tab-btn ${currentTab === 'results' ? 'active' : ''}`} onClick={() => currentTab === 'search' || setCurrentTab('results')} disabled={!routeResult}>📍 Results</button>
          </div>

                  {currentTab === 'search' && (
                    <div className="card">
                      <SearchBar source={source} destination={destination} onSourceChange={setSource} onDestinationChange={setDestination} onSearch={calculateRoute} stations={locations} loading={loading} />
                      {error && <div style={{ color: 'var(--color-red)', marginTop: '12px', fontSize: '14px' }}>⚠️ {error}</div>}
                    </div>
                  )}

                  {currentTab === 'results' && routeResult && (
                    <div className="itineraries">
                      {routeResult.packages.map((pkg, idx) => (
                        <ItineraryCard key={idx} itineraryPackage={pkg} isPrimary={idx === 0} loading={loading} onBook={() => handleBookTrip(pkg, pkg.estimated_cost || 50)} showBookButton={true} />
                      ))}
                    </div>
                  )}
                </div>
                
                <div className="right-panel">
                  {currentTab === 'search' ? (
                    <MapView path={[]} />
                  ) : (
                    <MapView path={routeResult?.packages[0]?.path || []} />
                  )}
                </div>
              </div>
            </div>
          </section>
        )}
      </main>

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