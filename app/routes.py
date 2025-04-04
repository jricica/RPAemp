from flask import Blueprint, render_template, request, redirect, url_for
from app.utils import leer_pdf, extraer_info
import os

bp = Blueprint('main', __name__)

# Lista de facturas procesadas (simulación de base de datos)
facturas_procesadas = []

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/subir_factura', methods=['POST'])
def subir_factura():
    if 'pdf' not in request.files:
        return "Error: No se envió un archivo PDF", 400

    archivo = request.files['pdf']
    archivo_path = f'./uploads/{archivo.filename}'
    archivo.save(archivo_path)

    # Leer y extraer info del PDF
    texto = leer_pdf(archivo_path)
    info = extraer_info(texto)

    # Guardar en lista
    factura = {
        "id": len(facturas_procesadas) + 1,
        "nombre": archivo.filename,
        "fecha": info["fecha_emision"],
        "total_facturado": info["total_facturado"],
        "cliente": info["cliente"]
    }
    facturas_procesadas.append(factura)

    # Redirigir a la vista de facturas
    return redirect(url_for("main.ver_facturas"))

@bp.route('/ver_facturas')
def ver_facturas():
    return render_template('ver_facturas.html', facturas=facturas_procesadas)
