from flask import render_template
from CarbonApp import app  ## dette er nok FEIL

@app.route('/about_us')
def about_us():
    team_members = [
        {"name": "Thomas Andre Vindenes", "role": "Developer", "bio": "Bio."},
        {"name": "Elsa", "role": "Developer", "bio": "Bio."},
        {"name": "Julen Gago", "role": "Developer", "bio": "Bio."},
        {"name": "Emelie Nyström", "role": "Developer", "bio": "Bio."},
        {"name": "Sondre Bøygard", "role": "Developer", "bio": "Bio."},
        {"name": "Fredrik Sælemyr", "role": "Developer", "bio": "Bio."},
        {"name": "Alexander Kjellevold", "role": "Developer", "bio": "Bio."}
    ]
    return render_template('about_us.html', title='About Us', team_members=team_members)
