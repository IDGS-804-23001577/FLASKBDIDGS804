from flask import render_template, request, redirect, url_for
from . import cursos
from models import db, Curso
import forms

@cursos.route("/cursos", methods=['GET'])
def index():
    create_form = forms.CursoForm(request.form)
    lista_cursos = Curso.query.all()
    return render_template("cursos/listadoCursos.html", form=create_form, cursos=lista_cursos)


@cursos.route("/cursos_agregar", methods=['GET', 'POST'])
def agregar():
    create_form = forms.CursoForm(request.form)
    if request.method == 'POST':
        curso_nuevo = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data
        )
        db.session.add(curso_nuevo)
        db.session.commit()
        return redirect(url_for('cursos.index'))
    
    return render_template("cursos/agregar.html", form=create_form)


@cursos.route("/cursos_detalles", methods=['GET'])
def detalles():
    create_form = forms.CursoForm(request.form)
    id_curso = request.args.get('id')
    curso = db.session.query(Curso).filter(Curso.id == id_curso).first()
    
    return render_template('cursos/detalles.html', curso=curso, form=create_form)


@cursos.route("/cursos_modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.CursoForm(request.form)
    
    if request.method == 'GET':
        id_curso = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id_curso).first()
        create_form.id.data = curso.id
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro_id.data = curso.maestro_id

    if request.method == 'POST':
        id_curso = request.args.get('id')
        curso = db.session.query(Curso).filter(Curso.id == id_curso).first()
        curso.nombre = create_form.nombre.data
        curso.descripcion = create_form.descripcion.data
        curso.maestro_id = create_form.maestro_id.data
        db.session.commit()
        return redirect(url_for('cursos.index'))

    return render_template("cursos/modificar.html", form=create_form)


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