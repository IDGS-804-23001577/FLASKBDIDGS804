from types import MethodType

from models import Maestros
from flask import Flask, render_template, request, redirect, url_for, flash, g
from . import maestros
import forms
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g



@maestros.route("/maestros", methods=['GET','POST'])
@maestros.route("/index")
def index():
    create_form=forms.UserForm(request.form)
    maestros=Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=maestros)


@maestros.route("/perfil/<nombre>")
def perfil(nombre):
    return f"perfil de {nombre}"

