from flask import render_template, request, redirect, url_for, flash
from . import maestros
from models import db, Maestros
import forms

@maestros.route("/maestros", methods=['GET'])
def index():
    create_form = forms.MaestroForm(request.form)
    lista_maestros = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=lista_maestros)


@maestros.route("/maestros_agregar", methods=['GET', 'POST'])
def agregar():
    create_form = forms.MaestroForm(request.form)
    
    
    if create_form.validate_on_submit():
        maestro_nuevo = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            especialidad=create_form.especialidad.data
        )
        db.session.add(maestro_nuevo)
        db.session.commit()
        return redirect(url_for('maestros.index'))
    
    
    return render_template("maestros/agregar.html", form=create_form)


@maestros.route("/maestros_detalles", methods=['GET'])
def detalles():
    create_form = forms.MaestroForm(request.form)
    matricula = request.args.get('id')
    maestro = Maestros.query.get(matricula)
    
    return render_template('maestros/detalles.html', maestro=maestro, form=create_form)


@maestros.route("/maestros_modificar", methods=['GET', 'POST'])
def modificar():
    matricula = request.args.get('id')
    maestro = Maestros.query.get(matricula)
    
    
    create_form = forms.MaestroForm(request.form, obj=maestro)
    
    
    if create_form.validate_on_submit():
        maestro.nombre = create_form.nombre.data
        maestro.apellidos = create_form.apellidos.data
        maestro.email = create_form.email.data
        maestro.especialidad = create_form.especialidad.data
        
        db.session.commit()
        return redirect(url_for('maestros.index'))

    return render_template("maestros/modificar.html", form=create_form)


@maestros.route("/maestros_eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.MaestroForm(request.form)
    
    if request.method == 'GET':
        matricula = request.args.get('id')
        maestro = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        create_form.matricula.data = maestro.matricula
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.email.data = maestro.email
        create_form.especialidad.data = maestro.especialidad

    if request.method == 'POST':
        matricula = create_form.matricula.data
        maestro = Maestros.query.get(matricula)
        
       
        if maestro.cursos:
            flash("No se puede eliminar: El maestro tiene cursos asignados.")
            return redirect(url_for('maestros.index'))

        db.session.delete(maestro)
        db.session.commit()
        return redirect(url_for('maestros.index'))

    return render_template("maestros/eliminar.html", form=create_form)
