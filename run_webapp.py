#!/usr/bin/env python3
"""
Hindi Text Summarizer Web Application
Startup script for the Flask web interface
"""

import os
import sys
from pathlib import Path

# Add current directory to Python path
sys.path.append(str(Path(__file__).parent))

try:
    from app import app
    print("🚀 Starting Hindi Text Summarizer Web Application...")
    print("📱 Open your browser and go to: http://localhost:5001")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5001)
    
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    print("💡 Make sure you have installed all requirements:")
    print("   pip install -r requirements.txt")
    
except Exception as e:
    print(f"❌ Error starting the application: {e}") 