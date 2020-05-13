
# Importing HonoluluHI library made for this assignment
from HonoluluHI_Weather import HonoluluHI_WeatherDB
from HonoluluHI_Weather import month_offset

from flask import Flask, jsonify

# Flask set-up
app = Flask(__name__)

weather = HonoluluHI_WeatherDB()

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

# Returns the jsonified precipitation data for the last year in the database
@app.route("/api/v1.0/precipitation")
def get_precipitation_data():
     return jsonify(weather.get_prcp_data_last_yr("List of Dicts"))

# Returns jsonified data of all of the stations in the database
@app.route("/api/v1.0/stations")
def get_all_stations():
     #returns data of all stations
    return jsonify(weather.stations_data(list_of_dicts = True))

# Returns the jsonified data for the most active station for the last year of data
@app.route("/api/v1.0/tobs")
def get_station_tobs():
    #returns temperature for the most active station
    return jsonify( \
        weather.station_temp_data(station_name = "WAIHEE 837.5, HI US", list_of_dicts = True))

# Accepts the start date as input parameter from URL and returns min., max., avg. temperatures 
@app.route("/api/v1.0/<start>")
def get_temp_for_time_start(start):
     #returns data of all stations
    start = start.lstrip("<").rstrip(">")
    return jsonify(weather.calc_temps(start, "9999-01-01"))

# Accepts the start and end date as input parameter from URL and returns min., max., avg. temperatures     
@app.route("/api/v1.0/<start>/<end>")
def get_temp_for_time_start_end(start, end = ""):
     #returns data of all stations
    start = start.lstrip("<").rstrip(">")
    end = end.lstrip("<").rstrip(">")
    return jsonify(weather.calc_temps(start, end))
    #return weather.calc_temps(start, end)[0]
if __name__ == '__main__':
    app.run(debug=True)