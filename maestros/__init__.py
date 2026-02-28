from flask import Blueprint

maestros=Blueprint(
    'maestros',
    __name__,
    template_folder='templates',
    static_folder='static')

# Las rutas siempre van al final para evitar la importación circular
from . import routes