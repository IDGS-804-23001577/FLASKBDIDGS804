from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, validators

class UserForm(FlaskForm):
    id = IntegerField('ID', [
        validators.Optional()
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El nombre es obligatorio'),
        validators.Length(min=4, max=20, message='El nombre debe tener entre 4 y 20 letras')
    ])
    apellidos = StringField('Apellidos' , [
        validators.DataRequired(message='Los apellidos son obligatorios')
    ])
    email = EmailField('Correo Electrónico', [
        validators.DataRequired(message='El correo electrónico es obligatorio'),
        validators.Email(message='Ingrese una direccion de correo valida')
    ])
    telefono = StringField('Teléfono', [
        validators.DataRequired(message='El número de teléfono es obligatorio'),
        validators.Length(min=10, max=10, message='El teléfono debe tener exactamente 10 dígitos')
    ])




class MaestroForm(FlaskForm):
    matricula = IntegerField('Matrícula', [
        validators.Optional()
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El nombre es obligatorio')
    ])
    apellidos = StringField('Apellidos' , [
        validators.DataRequired(message='Los apellidos son obligatorios')
    ])
    email = EmailField('Correo Electrónico', [
        validators.DataRequired(message='El correo electrónico es obligatorio'),
        validators.Email(message='Ingrese un correo válido')
    ])
    especialidad = StringField('Especialidad', [
        validators.DataRequired(message='La especialidad es necesaria')
    ])





class CursoForm(FlaskForm):
    id = IntegerField('ID')
    nombre = StringField('Nombre del Curso', [
        validators.DataRequired(message='El nombre del curso es obligatorio'),
        validators.Length(min=4, max=150, message='El nombre debe tener entre 4 y 150 caracteres')
    ])
    descripcion = StringField('Descripción', [
        validators.DataRequired(message='La descripción del curso es obligatoria')
    ])
    maestro_id = IntegerField('ID del Maestro', [
        validators.DataRequired(message='Debe asignar un maestro al curso')
    ])







class InscripcionForm(FlaskForm):
    alumno_id = IntegerField('ID del Alumno', [
        validators.DataRequired(message='Debe seleccionar un alumno de la lista')
    ])
    curso_id = IntegerField('ID del Curso', [
        validators.DataRequired(message='Debe seleccionar un curso de la lista')
    ])