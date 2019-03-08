from flask_restplus import Api
from .sensors import api as sensors
from .parameters import api as parameters
from .domains import api as domains
from .orgs import api as orgs
from .units import api as units
from flask import jsonify

authorizations = {
    'apikey' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'Authorization'
    }
}
api = Api(version='0.1',authorizations=authorizations, title='Sensor Ingest API',default='sensors', description='A Restful API for scheduling ingests of remote data sensors')

api.add_namespace(sensors, path='/api/sensors')
api.add_namespace(parameters, path='/api/parameters')
api.add_namespace(orgs, path='/api/orgs')
api.add_namespace(domains, path='/api/domains')
api.add_namespace(units, path='/api/units')


@api.errorhandler
def default_error_handler(error):
    return {'message': error.message, 'data' : error.payload}, error.status_code

