from flask import render_template, request, redirect, url_for, flash
from . import cursos
from models import db, Curso, Alumnos, Maestros
import forms

@cursos.route("/cursos", methods=['GET'])
def index():
    create_form = forms.CursoForm(request.form)
    lista_cursos = Curso.query.all()
    return render_template("cursos/listadoCursos.html", form=create_form, cursos=lista_cursos)

@cursos.route("/cursos_agregar", methods=['GET', 'POST'])
def agregar():
    create_form = forms.CursoForm(request.form)
    
   
    if create_form.validate_on_submit():
        curso_nuevo = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=request.form.get('maestro_id') 
        )
        db.session.add(curso_nuevo)
        db.session.commit()
        return redirect(url_for('cursos.index'))
    
    
    maestros = Maestros.query.all()
    return render_template("cursos/agregar.html", form=create_form, maestros=maestros)

@cursos.route("/cursos_detalles", methods=['GET', 'POST'])
def detalles():
    create_form = forms.CursoForm(request.form)
    id_curso = request.args.get('id')
    curso = Curso.query.get(id_curso)
    
    if request.method == 'POST':
        alumno_id = request.form.get('alumno_id')
        if alumno_id:
            alumno = Alumnos.query.get(alumno_id)
            if alumno not in curso.alumnos:
                curso.alumnos.append(alumno)
                db.session.commit()
        return redirect(url_for('cursos.detalles', id=id_curso))
    
    todos_los_alumnos = Alumnos.query.all()
    return render_template('cursos/detalles.html', curso=curso, form=create_form, alumnos=todos_los_alumnos)

@cursos.route("/cursos_modificar", methods=['GET', 'POST'])
def modificar():
    id_curso = request.args.get('id')
    curso = Curso.query.get(id_curso)
    
    
    create_form = forms.CursoForm(request.form, obj=curso)
    
    
    if create_form.validate_on_submit():
        curso.nombre = create_form.nombre.data
        curso.descripcion = create_form.descripcion.data
        curso.maestro_id = request.form.get('maestro_id') 
        db.session.commit()
        return redirect(url_for('cursos.index'))

    
    maestros = Maestros.query.all()
    return render_template("cursos/modificar.html", form=create_form, maestros=maestros, curso=curso)

@cursos.route("/cursos_eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.CursoForm(request.form)
    
    if request.method == 'GET':
        id_curso = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id_curso).first()
        create_form.id.data = curso.id
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro_id.data = curso.maestro_id

    if request.method == 'POST':
        id_curso = create_form.id.data
        curso = Curso.query.get(id_curso)
        db.session.delete(curso)
        db.session.commit()
        return redirect(url_for('cursos.index'))

    return render_template("cursos/eliminar.html", form=create_form)


@cursos.route("/inscripciones_agregar", methods=['GET', 'POST'])
def inscribir():
    
    form = forms.InscripcionForm(request.form)
    
    if form.validate_on_submit():
        alumno_id = form.alumno_id.data
        curso_id = form.curso_id.data
        
        alumno = Alumnos.query.get(alumno_id)
        curso = Curso.query.get(curso_id)
        
        if alumno and curso:
            
            if alumno in curso.alumnos:
                flash(f"El alumno {alumno.nombre} ya se encuentra inscrito en {curso.nombre}.", "warning")
            else:
                
                curso.alumnos.append(alumno)
                db.session.commit()
                flash(f"¡Inscripción exitosa de {alumno.nombre} en {curso.nombre}!", "success")
                
            
            return redirect(url_for('cursos.index'))

    
    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()
    return render_template("inscripciones/agregar.html", alumnos=alumnos, cursos=cursos, form=form)