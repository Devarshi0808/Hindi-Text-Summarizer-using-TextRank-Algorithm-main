from flask import Flask, render_template, request, jsonify
import os
import sys
from pathlib import Path

# Add the current directory to Python path to import the summarizer
sys.path.append(str(Path(__file__).parent))
from summarizer_fixed import summarize_hindi_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text.strip():
            return jsonify({
                'success': False,
                'error': 'Please enter some Hindi text to summarize.'
            })
        
        # Generate summary
        summary = summarize_hindi_text(text, summary_ratio=0.3)
        
        # Calculate statistics
        original_length = len(text.split())
        summary_length = len(summary.split())
        compression_ratio = (1 - summary_length / original_length) * 100 if original_length > 0 else 0
        
        return jsonify({
            'success': True,
            'summary': summary,
            'original_length': original_length,
            'summary_length': summary_length,
            'compression_ratio': round(compression_ratio, 1)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        })

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file uploaded'})
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'})
        
        if file:
            # Read file content
            content = file.read().decode('utf-8')
            
            # Generate summary
            summary = summarize_hindi_text(content, summary_ratio=0.3)
            
            # Calculate statistics
            original_length = len(content.split())
            summary_length = len(summary.split())
            compression_ratio = (1 - summary_length / original_length) * 100 if original_length > 0 else 0
            
            return jsonify({
                'success': True,
                'summary': summary,
                'original_length': original_length,
                'summary_length': summary_length,
                'compression_ratio': round(compression_ratio, 1),
                'filename': file.filename
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 