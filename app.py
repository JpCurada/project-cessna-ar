from flask import Flask, render_template
from pathlib import Path

class ARApp:
    """Flask application for AR model visualization."""
    
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.setup_routes()
    
    def setup_routes(self) -> None:
        """Configure application routes."""
        @self.app.route('/')
        def index() -> str:
            return render_template('index.html')
    
    def run(self, debug: bool = True) -> None:
        """Run the Flask application."""
        self.app.run(debug=debug, host='0.0.0.0')

if __name__ == '__main__':
    ar_app = ARApp()
    ar_app.run()