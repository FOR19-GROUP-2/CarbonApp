#from flask import render_template, Blueprint
#carbon_app = Blueprint('carbon_app', __name__)

#@carbon_app.route('/carbon_app')
#def carbon_app_home():
#    return render_template('carbon_app.html', title='carbon_app')
from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, FerryForm,trainForm, BicycleForm, WalkForm, CarFormSUV, Domestic_FlightForm, Long_haul_FlightForm, long_distance_busForm, tramForm

carbon_app=Blueprint('carbon_app',__name__)

#Emissions factor per transport in kg per passemger km
#Data from: http://efdb.apps.eea.europa.eu/?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22display_type%22%3A%22tabular%22%7D
#efco2={'Bus':{'Diesel':0.10231,'CNG':0.08,'Petrol':0.10231,'No Fossil Fuel':0},
 #   'Car':{'Petrol':0.18592,'Diesel':0.16453,'No Fossil Fuel':0},
  #  'Plane':{'Petrol':0.24298},
   # 'Ferry':{'Diesel':0.11131, 'CNG':0.1131, 'No Fossil Fuel':0},
    #'Motorbike':{'Petrol':0.09816,'No Fossil Fuel':0},
   # 'Scooter':{'No Fossil Fuel':0},
    #'Bicycle':{'No Fossil Fuel':0},
    #'Walk':{'No Fossil Fuel':0}}

efco2={'Car: Small':{'Petrol':0.1462,'Diesel':0.1197,'Electric':0.0414},
    'Car: SUV':{'Petrol':0.2088,'Diesel':0.1835,'Electric':0.0477},
    'Domestic Flight':{'Not my choice':0.246},
    'Long-haul Flight':{'Not my choice':0.1480},
    'Bus':{'Not my choice':0.097},
    'Long distance bus (Coach)':{'Not my choice':0.027},
    'Tram':{'Not my choice':0.029},
    'Train':{'Not my choice':0.035},
    'Ferry':{'Not my choice':0.019},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}

#if statement för att räkna co2 utsläpp fr alla classer

#if statement för att räkna om det finns ett annat transport sätt som är bättre
    #tar co2 från if statementen ovanför 
    #returnar bättre sätt att åka på 

#Carbon app, main page
@carbon_app.route('/carbon_app')
@login_required
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')

#New entry bus
@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = round(co2, 2)

        if float(kms) <= 15:
            saved = co2
            message = f"You could have saved {saved} by taking the bicycle or walking"
        else:
            saved = float(kms) - efco2['Tram'][fuel]
            saved2 = float(kms) * efco2['Train'][fuel]
            message = f"You could have saved {saved} by taking the tram and {saved2} by taking the train"
    
            
        #istellet för popup display bredvid graferna på samma sett så de är displayed


        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
        #return render_template('index.html', popup_script=popup_script)
    return render_template('carbon_app/new_entry_bus.html', title='new entry bus', form=form)

#New entry car small
@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        people = form.people.data
        transport = 'Car: Small'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = (float(kms) * efco2[transport][fuel]) / float(people)
        #ch4 = float(kms) * efch4[transport][fuel]
        #total = co2+ch4

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)
        #ch4 = float("{:.2f}".format(ch4))
        #total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, people=people, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_car.html', title='new entry car', form=form)    

#New entry car SUV
@carbon_app.route('/carbon_app/new_entry_carSUV', methods=['GET','POST'])
@login_required
def new_entry_carSUV():
    form = CarFormSUV()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        people = form.people.data
        transport = 'Car: SUV'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = (float(kms) * efco2[transport][fuel]) / float(people)
        #ch4 = float(kms) * efch4[transport][fuel]
        #total = co2+ch4

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)

        #ch4 = float("{:.2f}".format(ch4))
        #total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, people = people,author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_carSUV.html', title='new entry car SUV', form=form) 

#New entry Domestic Flight
@carbon_app.route('/carbon_app/new_entry_domestic_flight', methods=['GET','POST'])
@login_required
def new_entry_domestic_flight():
    form = Domestic_FlightForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Domestic Flight'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_domestic_flight.html', title='new entry domestic flight', form=form)

#New entry Long-haul Flight
@carbon_app.route('/carbon_app/new_entry_long_haul_flight', methods=['GET','POST'])
@login_required
def new_entry_long_haul_flight():
    form = Long_haul_FlightForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Long-haul Flight'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_long_haul_flight.html', title='new entry Long-haul Flight', form=form)

#New entry Long distance bus (Coach) 
@carbon_app.route('/carbon_app/new_entry_long_distance_bus', methods=['GET','POST'])
@login_required
def new_entry_long_distance_bus():
    form = long_distance_busForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Long distance bus (Coach)'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_long_distance_bus.html', title='new entry long distance bus (Coach)', form=form)

#New entry Tram 
@carbon_app.route('/carbon_app/new_entry_tram', methods=['GET','POST'])
@login_required
def new_entry_tram():
    form = tramForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Tram'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_tram.html', title='new entry tram', form=form)

#New entry Train 
@carbon_app.route('/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    form = trainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_train.html', title='new entry train', form=form)

#New entry Ferry 
@carbon_app.route('/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_ferry.html', title='new entry ferry', form=form)


#New entry Bicycle
@carbon_app.route('/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bicycle.html', title='new entry bicycle', form=form)

#New entry Walk
@carbon_app.route('/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_walk.html', title='new entry walk', form=form)

#Your data
@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    #Table
    
    entries = Transport.query.filter_by(author=current_user). \
        filter(Transport.date> (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()

    return render_template('carbon_app/your_data.html', title='your_data', entries=entries)


    

#Delete emission
@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))
    
  
