from flask import render_template, redirect, request, session, url_for
from dojos_ninjas_app import app
from dojos_ninjas_app.models.ninja import Ninja
from dojos_ninjas_app.models.dojo import Dojo

@app.route('/ninjas')
def ninja():
    dojo = Dojo.get_all()
    return render_template('ninja_index.html',dojos=dojo)

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')