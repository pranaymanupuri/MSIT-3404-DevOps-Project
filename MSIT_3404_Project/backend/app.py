from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)

# Route 1: Home page
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>MSIT 3404 Backend API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 800px; margin: 0 auto; }
            h1 { color: #333; }
            .endpoint { background: #f5f5f5; padding: 10px; margin: 10px 0; border-radius: 5px; }
            code { background: #e0e0e0; padding: 2px 5px; border-radius: 3px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 MSIT 3404 Backend Service</h1>
            <p>Flask backend running successfully in Docker!</p>
            
            <h2>Available Endpoints:</h2>
            <div class="endpoint">
                <strong>GET /</strong> - This home page
            </div>
            <div class="endpoint">
                <strong>GET /health</strong> - Health check status
            </div>
            <div class="endpoint">
                <strong>GET /image</strong> - Serve sample image
            </div>
            <div class="endpoint">
                <strong>GET /api/data</strong> - Sample JSON API
            </div>
            
            <h2>Project Info:</h2>
            <p>This is part of the DevOps project demonstrating:</p>
            <ul>
                <li>Docker containerization</li>
                <li>Kubernetes deployment</li>
                <li>Multi-container applications</li>
                <li>DevOps CI/CD principles</li>
            </ul>
        </div>
    </body>
    </html>
    '''

# Route 2: Health check endpoint
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "msit3404-backend",
        "version": "1.0.0"
    })

# Route 3: Serve image
@app.route('/image')
def serve_image():
    try:
        return send_file('static/image.jpg', mimetype='image/jpeg')
    except FileNotFoundError:
        return "Image not found. Please add image.jpg to static folder.", 404

# Route 4: Sample JSON API
@app.route('/api/data')
def api_data():
    return jsonify({
        "project": "MSIT 3404 DevOps",
        "members": ["Student 1", "Student 2"],
        "tasks": ["Docker", "Kubernetes", "CI/CD"],
        "status": "in_progress"
    })

# Route 5: Simple hello
@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from Flask backend!"})

if __name__ == '__main__':
    # Run on all network interfaces (0.0.0.0) so it's accessible outside container
    app.run(debug=True, host='0.0.0.0', port=5000)