from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired, NumberRange, ValidationError
#test_1001

class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], choices=[('Not my choice', 'Not my choice')])
    #choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Petrol', 'Petrol'), ('No Fossil Fuel', 'No Fossil Fuel')])
                          
  submit = SubmitField('Submit')

class long_distance_busForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], choices=[('Not my choice', 'Not my choice')])
    #choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Petrol', 'Petrol'), ('No Fossil Fuel', 'No Fossil Fuel')])                       
  submit = SubmitField('Submit')

def validate_max_people(form, field):
    if field.data > 5:
        raise ValidationError('Maximum number of people allowed is 5.')
    
class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')])
  people = FloatField('People',[InputRequired(), NumberRange(min=0, max=5, message='Maximum number of people allowed is 5.')]) #max 5
  submit = SubmitField('Submit')  

class CarFormSUV(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')])
  people = FloatField('People',[InputRequired(), NumberRange(min=0, max=7, message='Maximum number of people allowed is 7.')])
  submit = SubmitField('Submit') 

class Long_haul_FlightForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Not my choice', 'Not my choice')])
  submit = SubmitField('Submit')

class Domestic_FlightForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Not my choice', 'Not my choice')])
  submit = SubmitField('Submit')

class tramForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Not my choice', 'Not my choice')])
  submit = SubmitField('Submit') 

class trainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Not my choice', 'Not my choice')])
  submit = SubmitField('Submit') 

class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Not my choice', 'Not my choice')])
  submit = SubmitField('Submit')  


class BicycleForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

