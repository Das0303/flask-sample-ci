from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Define the root route
@app.route('/')
def hello_world():
    """Returns a simple 'Hello, World!' message."""
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the application (for local testing)
    app.run(debug=True)
