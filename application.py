
from flask import Flask

# Flask set-up
app = Flask(__name__)

#Flask routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"<ol>"
        f"<li>api/v1.0/precipitation</li>"
        f"<br/>"
        f"<li>api/v1.0/stations</li>"
        f"<br/>"
        f"<li>api/v1.0/tobs</li>"
        f"<br/>"
        f"<li>api/v1.0/<start></li>"
        f"<br/>"
        f"<li>api/v1.0/<start>/<end></li>"
        f"</ol>"
    )

if __name__ == '__main__':
    app.run(debug=True)