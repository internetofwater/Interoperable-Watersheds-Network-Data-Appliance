from flask_restplus import abort
from . import domains , sensors, organizations, session


class GenericModelService(object):
    
    
    def __init__(self, model, name):
        self.model = model
        self.name = name


    def query(self, **kwargs):
        return self.model.query.filter_by(kwargs)

    @property
    def objects(self):
        return self.model.query.all()
    
    def get(self, id):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))
        return obj
    
    def create(self, data):
        obj = self.model(**data)
        session.add(obj)
        session.commit()
        return obj
    
    def update(self, id, data):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))

        for key, value in data.items():
            setattr(obj,key,value)
        session.commit()
        return obj
    
    def delete(self, id):
        obj = self.model.query.get(id)
        if not obj:
            abort(404, '{0} Entity {1} Not Found'.format(self.name,id))
        session.delete(obj)
        session.commit()
        

sensors_service = GenericModelService(sensors.Sensors,'Sensor')
sensor_parameters_service = GenericModelService(sensors.SensorParameters, 'Sensor Parameter')
parameter_service = GenericModelService(domains.Parameters, 'Parameter')
units_service = GenericModelService(domains.Units, 'Unit')
medium_service = GenericModelService(domains.MediumTypes, 'Medium Type')
quality_check_operand_service = GenericModelService(domains.QualityCheckOperands, 'Quality Check Operand')
quality_check_action_service = GenericModelService(domains.QualityCheckActions, 'Quality Check Action')
data_qualifier_service = GenericModelService(domains.DataQualifiers, 'Data Qualifier')
organizations_service = GenericModelService(organizations.Organizations, 'Organization')