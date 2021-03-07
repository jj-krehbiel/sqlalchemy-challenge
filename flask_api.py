from flask import Flask, jsonify

# Flask setup
app = Flask(__name__)

#Flask routes
@app.route("/")
def home():
    return(
        f"Welcome to my Hawaii Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

#Define the precipation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func, inspect
    from sqlalchemy import desc

    # create engine to hawaii.sqlite
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    inspector = inspect(engine)
    inspector.get_table_names()

    # reflect an existing database into a new model
    Base = automap_base()

    # reflect the tables
    Base.prepare(engine, reflect=True)

    # View all of the classes that automap found
    Base.classes.keys()

    # Save references to each table
    Measurement = Base.classes.measurement
    Station = Base.classes.station

    # Create our session (link) from Python to the DB
    session = Session(engine)


    # Perform a query to retrieve the date and precipitation scores
    date_prcp = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > '2016-08-23').\
    order_by(Measurement.date).all()

    #Make date_prcp a dictionary
    prcp_dict = {result[0]:result[1] for result in date_prcp}


    return jsonify(prcp_dict)

# Define the stations route
@app.route("/api/v1.0/stations")
def stations():
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func, inspect
    from sqlalchemy import desc

    # create engine to hawaii.sqlite
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    inspector = inspect(engine)
    inspector.get_table_names()

    # reflect an existing database into a new model
    Base = automap_base()

    # reflect the tables
    Base.prepare(engine, reflect=True)

    # View all of the classes that automap found
    Base.classes.keys()

    # Save references to each table
    Measurement = Base.classes.measurement
    Station = Base.classes.station

    # Create our session (link) from Python to the DB
    session = Session(engine)

    #get a list of all stations from Station
    station_list = session.query(Station.station).all()
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func, inspect
    from sqlalchemy import desc

    # create engine to hawaii.sqlite
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    inspector = inspect(engine)
    inspector.get_table_names()

    # reflect an existing database into a new model
    Base = automap_base()

    # reflect the tables
    Base.prepare(engine, reflect=True)

    # View all of the classes that automap found
    Base.classes.keys()

    # Save references to each table
    Measurement = Base.classes.measurement
    Station = Base.classes.station

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Perform a query to retrieve the date and precipitation scores for most active station
    temp_data = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date > '2016-08-18').\
    filter(Measurement.station =='USC00519281').\
    all()

    tobs_dict = {result[0]:result[1] for result in temp_data}

    return jsonify(tobs_dict)
  


@app.route("/api/v1.0/<start>/<end>")
def date_range(start, end):
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func, inspect
    from sqlalchemy import desc

    # create engine to hawaii.sqlite
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    inspector = inspect(engine)
    inspector.get_table_names()

    # reflect an existing database into a new model
    Base = automap_base()

    # reflect the tables
    Base.prepare(engine, reflect=True)

    # View all of the classes that automap found
    Base.classes.keys()

    # Save references to each table
    Measurement = Base.classes.measurement
    Station = Base.classes.station

    # Create our session (link) from Python to the DB
    session = Session(engine)

    mintemp = session.query(func.min(Measurement.tobs)).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()

    maxtemp = session.query(func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()

    avgtemp = session.query(func.avg(Measurement.tobs)).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()

    return(
        f"The minimum temperature for this date range is {mintemp}<br/>"
        f"The maximum temperature for this date range is {maxtemp}<br/>"
        f"The average temperature for this date range is {avgtemp}<br/>"
    )

@app.route("/api/v1.0/<start>")
def start_date(start):
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func, inspect
    from sqlalchemy import desc

    # create engine to hawaii.sqlite
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    inspector = inspect(engine)
    inspector.get_table_names()

    # reflect an existing database into a new model
    Base = automap_base()

    # reflect the tables
    Base.prepare(engine, reflect=True)

    # View all of the classes that automap found
    Base.classes.keys()

    # Save references to each table
    Measurement = Base.classes.measurement
    Station = Base.classes.station

    # Create our session (link) from Python to the DB
    session = Session(engine)

    mintemp = session.query(func.min(Measurement.tobs)).\
    filter(Measurement.date >= start).all()

    maxtemp = session.query(func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).all()

    avgtemp = session.query(func.avg(Measurement.tobs)).\
    filter(Measurement.date >= start).all()

    return(
        f"The minimum temperature for this date range is {mintemp}<br/>"
        f"The maximum temperature for this date range is {maxtemp}<br/>"
        f"The average temperature for this date range is {avgtemp}<br/>"
    )

if __name__ == "__main__":
    app.run(debug=True)