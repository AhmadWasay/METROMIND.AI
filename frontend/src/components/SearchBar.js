// frontend/src/components/SearchBar.js - Location search and selection
import React, { useState, useEffect } from 'react';
import '../styles/SearchBar.css';

function SearchBar({
  source,
  destination,
  onSourceChange,
  onDestinationChange,
  onSearch,
  stations,
  loading
}) {
  const [sourceSearch, setSourceSearch] = useState('');
  const [destSearch, setDestSearch] = useState('');
  const [sourceOpen, setSourceOpen] = useState(false);
  const [destOpen, setDestOpen] = useState(false);

  useEffect(() => {
    const sourceStation = stations.find(s => s.code === source);
    setSourceSearch(sourceStation ? sourceStation.name : '');
  }, [source, stations]);

  useEffect(() => {
    const destStation = stations.find(s => s.code === destination);
    setDestSearch(destStation ? destStation.name : '');
  }, [destination, stations]);



  const filterLocations = (search, allLocations) => {
    if (!search) return allLocations;
    const searchLower = search.toLowerCase();
    return allLocations.filter(loc =>
      loc.name.toLowerCase().includes(searchLower) ||
      (loc.area && loc.area.toLowerCase().includes(searchLower)) ||
      (loc.line && loc.line.toLowerCase().includes(searchLower))
    );
  };

  const filteredSource = filterLocations(sourceSearch, stations);
  const filteredDest = filterLocations(destSearch, stations);

  return (
    <div className="search-bar-container">
      <div className="search-inputs">
        <div className="input-group">
          <label>📍 From</label>
          <div className="select-wrapper">
            <input
              type="text"
              placeholder="Search starting location..."
              value={sourceSearch}
              onChange={(e) => setSourceSearch(e.target.value)}
              onFocus={() => setSourceOpen(true)}
              onBlur={() => setTimeout(() => setSourceOpen(false), 200)}
              className="search-input"
            />
            <button className="map-select-btn" title="Select location from dropdown" disabled>
              🗺️
            </button>
            {sourceOpen && filteredSource.length > 0 && (
              <div className="dropdown-list">
                {filteredSource.map(loc => (
                  <div
                    key={loc.code}
                    className="dropdown-item"
                    onClick={() => {
                      onSourceChange(loc.code);
                      setSourceOpen(false);
                    }}
                  >
                    <span className="location-type">
                      {loc.type === 'metro' ? '🚆' : '🚌'}
                    </span>
                    <div className="location-info">
                      <div className="location-name">{loc.name}</div>
                      <div className="location-detail">
                        {loc.line || loc.area}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
            {/* The <select> dropdown is functionally replaced by the searchable input above. */}
          </div>
        </div>

        <div className="swap-button">
          <button
            onClick={() => {
              const currentSource = source;
              onSourceChange(destination);
              onDestinationChange(currentSource);
            }}
            title="Swap locations"
          >
            ⇅
          </button>
        </div>

        <div className="input-group">
          <label>📍 To</label>
          <div className="select-wrapper">
            <input
              type="text"
              placeholder="Search destination..."
              value={destSearch}
              onChange={(e) => setDestSearch(e.target.value)}
              onFocus={() => setDestOpen(true)}
              onBlur={() => setTimeout(() => setDestOpen(false), 200)}
              className="search-input"
            />
            <button className="map-select-btn" title="Select location from dropdown" disabled>
              🗺️
            </button>
            {destOpen && filteredDest.length > 0 && (
              <div className="dropdown-list">
                {filteredDest.map(loc => (
                  <div
                    key={loc.code}
                    className="dropdown-item"
                    onClick={() => {
                      onDestinationChange(loc.code);
                      setDestOpen(false);
                    }}
                  >
                    <span className="location-type">
                      {loc.type === 'metro' ? '🚆' : '🚌'}
                    </span>
                    <div className="location-info">
                      <div className="location-name">{loc.name}</div>
                      <div className="location-detail">
                        {loc.line || loc.area}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
            {/* The <select> dropdown is functionally replaced by the searchable input above. */}
          </div>
        </div>
      </div>

      <button
        className="search-button"
        onClick={onSearch}
        disabled={loading}
      >
        {loading ? '⏳ Planning...' : '🔍 Plan Trip'}
      </button>
    </div>
  );
}

export default SearchBar;
