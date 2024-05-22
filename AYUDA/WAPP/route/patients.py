from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import Patient, db
from forms import PatientForm

patients = Blueprint('patients', __name__)

@patients.route('/patients')
@login_required
def list_patients():
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

@patients.route('/patients/create', methods=['GET', 'POST'])
@login_required
def create_patient():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patient(
            name=form.name.data,
            lastname=form.lastname.data,
            ci=form.ci.data,
            birth_date=form.birth_date.data
        )
        db.session.add(patient)
        db.session.commit()
        flash('Patient created successfully!', 'success')
        return redirect(url_for('patients.list_patients'))
    return render_template('patient_form.html', form=form)

@patients.route('/patients/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_patient(id):
    patient = Patient.query.get_or_404(id)
    form = PatientForm()
    if form.validate_on_submit():
        patient.name = form.name.data
        patient.lastname = form.lastname.data
        patient.ci = form.ci.data
        patient.birth_date = form.birth_date.data
        db.session.commit()
        flash('Patient updated successfully!', 'success')
        return redirect(url_for('patients.list_patients'))
    elif request.method == 'GET':
        form.name.data = patient.name
        form.lastname.data = patient.lastname
        form.ci.data = patient.ci
        form.birth_date.data = patient.birth_date
    return render_template('patient_form.html', form=form)

@patients.route('/patients/<int:id>/delete', methods=['POST'])
@login_required
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    flash('Patient deleted successfully!', 'success')
    return redirect(url_for('patients.list_patients'))
