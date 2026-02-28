from flask_wtf import Form
from wtforms import StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere min=4 max=20')
    ])
    apellidos = StringField('apellidos' , [
        validators.DataRequired(message='El apellido es requerido')
    ])
    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
    telefono = StringField('telefono', [
        validators.DataRequired(message='El telefono es requerido')
    ])



class MaestroForm(Form):
    matricula = IntegerField('matricula')
    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido')
    ])
    apellidos = StringField('apellidos' , [
        validators.DataRequired(message='Los apellidos son requeridos')
    ])
    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
    especialidad = StringField('especialidad', [
        validators.DataRequired(message='La especialidad es requerida')
    ])

class CursoForm(Form):
    id = IntegerField('id')
    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre del curso es requerido'),
        validators.length(min=4, max=150, message='Requiere min=4 max=150')
    ])
    descripcion = StringField('descripcion', [
        validators.DataRequired(message='La descripción es requerida')
    ])
    maestro_id = IntegerField('maestro_id', [
        validators.DataRequired(message='La matrícula del maestro es requerida')
    ])