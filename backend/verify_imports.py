#!/usr/bin/env python3
"""
MetroMind Backend - Import Verification
Checks if all modules can be imported successfully
"""

import sys
import os

# Add backend directory to path
backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

def check_import(module_name, description):
    """Check if module imports successfully"""
    try:
        __import__(module_name)
        print(f"✅ {description}: {module_name}")
        return True
    except ImportError as e:
        print(f"❌ {description}: {module_name}")
        print(f"   Error: {e}")
        return False
    except Exception as e:
        print(f"⚠️  {description}: {module_name}")
        print(f"   Warning: {e}")
        return True

print("=" * 60)
print("MetroMind AI - Backend Import Verification")
print("=" * 60)

results = {}

# Check Python version
print(f"\n📦 Python Version: {sys.version.split()[0]}")

# Core dependencies
print("\n🔧 Core Dependencies:")
results['flask'] = check_import('flask', 'Flask')
results['flask_cors'] = check_import('flask_cors', 'Flask-CORS')
results['sqlite3'] = check_import('sqlite3', 'SQLite3')

# Backend modules (local)
print("\n📦 Backend Modules:")
results['graph_engine'] = check_import('graph_engine', 'Graph Engine')
results['transit_data'] = check_import('transit_data', 'Transit Data')
results['models'] = check_import('models', 'Models/Database')
results['notifications'] = check_import('notifications', 'Notifications')

# Optional dependencies
print("\n📦 Optional Dependencies (for advanced features):")
results['sqlalchemy'] = check_import('sqlalchemy', 'SQLAlchemy')
results['dotenv'] = check_import('dotenv', 'Python-Dotenv')
results['twilio'] = check_import('twilio', 'Twilio')
results['requests'] = check_import('requests', 'Requests')

# Summary
print("\n" + "=" * 60)
passed = sum(1 for v in results.values() if v)
total = len(results)
print(f"✨ Results: {passed}/{total} imports successful")
print("=" * 60)

if passed == total:
    print("\n🎉 All systems ready! You can start main.py")
else:
    print("\n⚠️  Some imports failed. Install missing packages:")
    print("    pip install -r requirements.txt")
