# app/routes.py

from flask import Blueprint, render_template, request, jsonify
from app.utils import leer_pdf, extraer_info
import os
from datetime import datetime

# Definir el Blueprint
bp = Blueprint('main', __name__)

# Ruta para servir la página HTML
@bp.route('/')
def index():
    return render_template('index.html')

# Ruta para subir facturas y extraer datos
@bp.route('/subir_factura', methods=['POST'])
def subir_factura():
    if 'pdf' not in request.files:
        return jsonify({"error": "No se envió un archivo PDF"}), 400

    archivo = request.files['pdf']
    archivo_path = f'./uploads/{archivo.filename}'
    
    # Crear carpeta uploads si no existe
    if not os.path.exists('./uploads'):
        os.makedirs('./uploads')

    archivo.save(archivo_path)

    # Leer el contenido del PDF
    texto = leer_pdf(archivo_path)
    info = extraer_info(texto)

    # Verifica la información extraída
    print("Información extraída:", info)

    # Si no se encuentra la clave 'total_facturado', se usa un valor por defecto
    total_facturado = info.get('total_facturado', 'No disponible')
    cliente = info.get('cliente', 'Desconocido')

    print("Total facturado:", total_facturado)
    print("Cliente:", cliente)

    # Guardar la factura procesada en una lista
    factura_resumen = {
        'id': str(len(facturas_procesadas) + 1),
        'nombre': archivo.filename,
        'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'total_facturado': total_facturado,
        'cliente': cliente,
        'info': info
    }

    facturas_procesadas.append(factura_resumen)

    return jsonify({"success": True, "id_factura": factura_resumen['id']})

# Ruta para ver las facturas procesadas
@bp.route('/ver_facturas')
def ver_facturas():
    return render_template('ver_facturas.html', facturas=facturas_procesadas)

# Lista de facturas procesadas
facturas_procesadas = []
