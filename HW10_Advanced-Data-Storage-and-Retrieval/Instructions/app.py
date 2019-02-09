import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base, and_
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    # base = "http://127.0.0.1:5000/api/v1.0/"
    # """List all available api routes."""
    # return (
    #     f"Available Routes:<br/>"
    #     f"<a href={base}precipitation>All Precipitation Data</a><br>"
    #     f"<a href={base}stations>List of Stations</a><br>"
    #     f"<a href={base}tobs>All Temperature Data</a><br>"
    #     f"<hr>"
    #     f"Retrieve Temperature From Date Range"
    #     f"<form action='range' method='get'>\
    #         Start Date:<br>\
    #         <input type='text' name='Start'><br>\
    #         End Date (optional):<br>\
    #         <input type='text' name='End'>\
    #         <input type='submit' value='Submit'>\
    #     </form>"        
    #     f"/api/v1.0/&lt;start&gt;<br>"
    #     f"/api/v1.0/&lt;start&gt;&lt;end&gt;<br>"

    # )
    return render_template('home.html')


@app.route("/api/v1.0/precipitation")
def precepitation():
    """Convert the query results to a Dictionary using date as the key and prcp as the value"""
    #Query all dates

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    annual_prcp = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= query_date).\
        order_by(Measurement.date).all()

    prcp_values = []
    
    for observation in annual_prcp:
        prcp_dict = {}
        prcp_dict[observation.date]=observation.prcp
        prcp_values.append(prcp_dict)
    session.close()
    return jsonify(prcp_values)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))
    session.close()
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def temperature():
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    annual_temp = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= query_date).\
        order_by(Measurement.date).all()
        
    temp_values = []
    for observation in annual_temp:
        temp_dict = {}
        temp_dict [observation.date] = observation.tobs
        temp_values.append(temp_dict )
    session.close()
    return jsonify(temp_values)

@app.route("/api/v1.0/<start>")
def temp_start(start):
    start = dt.datetime.strptime(start, '%Y-%m-%d')
    annual_temp = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= start).\
        order_by(Measurement.date).all()
        
    temp_values = []
    for observation in annual_temp:
        temp_dict = {}
        temp_dict [observation.date] = observation.tobs
        temp_values.append(temp_dict )
    session.close()
    return jsonify(temp_values)

@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start, end):
    start = dt.datetime.strptime(start, '%Y-%m-%d')
    end = dt.datetime.strptime(end, '%Y-%m-%d')
    annual_temp = session.query(Measurement.date, Measurement.tobs).\
        filter(and_(Measurement.date >= start, Measurement.date <= end)).\
        order_by(Measurement.date).all()
        
    temp_values = []
    for observation in annual_temp:
        temp_dict = {}
        temp_dict [observation.date] = observation.tobs
        temp_values.append(temp_dict )
    session.close()
    return jsonify(temp_values)


# @app.route("/range?Start=<start>&End=<end>")
# def range(start, end):
#     start = dt.datetime.strptime(start, '%Y-%m-%d')
#     end = dt.datetime.strptime(end, '%Y-%m-%d')
#     annual_temp = session.query(Measurement.date, Measurement.tobs).\
#         filter(and_(Measurement.date >= start, Measurement.date <= end)).\
#         order_by(Measurement.date).all()
        
#     temp_values = []
#     for observation in annual_temp:
#         temp_dict = {}
#         temp_dict [observation.date] = observation.tobs
#         temp_values.append(temp_dict )
#     session.close()
#     return jsonify(temp_values)


if __name__ == '__main__':
    app.run(debug=True)
