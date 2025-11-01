from flask import Flask

from cliente import cliente_bp


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(cliente_bp)
    return app


app = create_app()

if __name__ == "__main__":
    # Keep the development server bound to localhost only.
    app.run(host="127.0.0.1", port=5003, debug=True)
