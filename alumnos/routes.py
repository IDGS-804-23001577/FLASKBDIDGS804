from flask import Blueprint, render_template, request, redirect, url_for
import forms
from models import db, Alumnos

alumnos = Blueprint('alumnos', __name__)

@alumnos.route("/alumnos", methods=['GET', 'POST'])
def tabla():
    create_form = forms.UserForm(request.form)
    alumno = Alumnos.query.all()
    return render_template("alumnos/alumnos_tabla.html", form=create_form, alumno=alumno)

@alumnos.route("/agregar_alumno", methods=['GET', 'POST'])
def agregar_alumno():
    create_form = forms.UserForm(request.form)
    if create_form.validate_on_submit():
        alum = Alumnos(nombre=create_form.nombre.data,
                     apellidos=create_form.apellidos.data, 
                     email=create_form.email.data,
                     telefono=create_form.telefono.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.tabla')) 
    return render_template("alumnos/Alumnos.html", form=create_form)

@alumnos.route("/detalles", methods=['GET'])
def detalles():
    id = request.args.get('id')
    alum1 = Alumnos.query.get(id)
    return render_template('alumnos/detalles.html', nombre=alum1.nombre, apellidos=alum1.apellidos, email=alum1.email, telefono=alum1.telefono, id=id)

@alumnos.route("/modificar", methods=['GET', 'POST'])
def modificar():
    id_arg = request.args.get('id')
    alum1 = Alumnos.query.get(id_arg)
    create_form = forms.UserForm(request.form, obj=alum1)

    if create_form.validate_on_submit():
        alum1.nombre = create_form.nombre.data
        alum1.apellidos = create_form.apellidos.data
        alum1.email = create_form.email.data
        alum1.telefono = create_form.telefono.data
        db.session.commit()
        return redirect(url_for('alumnos.tabla')) 
        
    return render_template("alumnos/modificar.html", form=create_form)

@alumnos.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email
        create_form.telefono.data=alum1.telefono

    if request.method=='POST':
        id=create_form.id.data
        alum=Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('alumnos.tabla')) 
        
    return render_template("alumnos/eliminar.html", form=create_form)