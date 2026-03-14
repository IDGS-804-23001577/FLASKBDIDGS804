from flask import render_template, request, redirect, url_for, flash
from . import inscripciones
from models import db, Curso, Alumnos
import forms


@inscripciones.route("/consultas", methods=['GET'])
def index():
    
    todos_cursos = Curso.query.all()
    todos_alumnos = Alumnos.query.all()
    
    curso_seleccionado = None
    alumno_seleccionado = None

    
    curso_id = request.args.get('curso_id')
    alumno_id = request.args.get('alumno_id')

    if curso_id:
        curso_seleccionado = Curso.query.get(curso_id)
    elif alumno_id:
        alumno_seleccionado = Alumnos.query.get(alumno_id)

    return render_template("inscripciones/consultar.html", 
                           todos_cursos=todos_cursos, 
                           todos_alumnos=todos_alumnos,
                           curso_seleccionado=curso_seleccionado, 
                           alumno_seleccionado=alumno_seleccionado)

