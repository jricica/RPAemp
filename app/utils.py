import pdfplumber
import pytesseract
from PIL import Image
import re

def leer_pdf(pdf_path):
    """
    Esta función extrae el texto de un archivo PDF, usando pdfplumber y Tesseract OCR en caso de necesitarlo.
    """
    texto = ""

    try:
        # Usamos pdfplumber para intentar extraer texto de PDFs complejos
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                texto += page.extract_text()

        # Si no se encuentra texto, usamos OCR
        if not texto.strip():
            print("Texto no encontrado, utilizando OCR...")
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    im = page.to_image()
                    texto += pytesseract.image_to_string(im.original)

    except Exception as e:
        print(f"Error al leer el PDF: {e}")

    print("Texto extraído del PDF:", texto)
    return texto


def extraer_info(texto):
    """
    Esta función extrae información relevante del texto de la factura, como el cliente, el total facturado, la fecha y hora de emisión.
    Utiliza expresiones regulares para encontrar los valores correspondientes en el texto.
    """
    total_facturado = None
    cliente = None
    fecha_emision = None
    nit = None

    # Buscar el cliente
    match_cliente = re.search(r"Nombre Receptor:\s*(.*)", texto)
    if match_cliente:
        cliente = match_cliente.group(1).strip()

    # Buscar el total facturado
    match_total = re.search(r"TOTALES:\s*[\d,\.]+\s*[\d,\.]+\s*([\d,\.]+)", texto)
    if match_total:
        total_facturado = match_total.group(1).strip()

    # Buscar la fecha de emisión
    match_fecha = re.search(r"Fecha y hora de emision:\s*([\d\-]+\s[\d:]+)", texto)
    if match_fecha:
        fecha_emision = match_fecha.group(1).strip()

    # Buscar el NIT
    match_nit = re.search(r"NIT Receptor:\s*(\d+)", texto)
    if match_nit:
        nit = match_nit.group(1).strip()

    # Si no se encuentran, asignamos valores por defecto
    if not total_facturado:
        total_facturado = "No disponible"
    
    if not cliente:
        cliente = "Desconocido"
    
    if not fecha_emision:
        fecha_emision = "No disponible"
    
    if not nit:
        nit = "No disponible"

    # Devuelve los datos extraídos
    return {
        "total_facturado": total_facturado,
        "cliente": cliente,
        "fecha_emision": fecha_emision,
        "nit": nit
    }
