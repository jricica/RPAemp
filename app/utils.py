import re
import pdfplumber
import pytesseract

def leer_pdf(pdf_path):
    texto = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                texto += page.extract_text() or ""

        if not texto.strip():
            print("Texto no encontrado, utilizando OCR...")
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    im = page.to_image()
                    texto += pytesseract.image_to_string(im.original)

    except Exception as e:
        print(f"Error al leer el PDF: {e}")

    return texto


def extraer_info(texto):
    total_facturado = "No disponible"
    cliente = "Desconocido"
    fecha_emision = "No disponible"
    nit = "No disponible"
    autorizacion = "No disponible"

    # Cliente (más robusto)
    match_cliente = re.search(r"Nombre Receptor:\s*(.+?)\s+Fecha y hora", texto)
    if match_cliente:
        cliente = match_cliente.group(1).strip()

    # Total (varios formatos posibles)
    match_total = re.search(r"TOTALES:\s*[\d,\.]+\s*([\d,\.]+)", texto)
    if not match_total:
        match_total = re.search(r"Total \(Q\)\s+[\d,\.]+\s+[\d,\.]+\s+([\d,\.]+)", texto)
    if match_total:
        total_facturado = match_total.group(1).strip()

    # Fecha y hora de emisión
    match_fecha = re.search(r"Fecha y hora de emision:\s*([\d]{1,2}-[a-z]{3}-[\d]{4} [\d:]{5,8})", texto, re.IGNORECASE)
    if match_fecha:
        fecha_emision = match_fecha.group(1).strip()

    # NIT receptor
    match_nit = re.search(r"NIT Receptor:\s*([0-9A-Z\-]+)", texto)
    if match_nit:
        nit = match_nit.group(1).strip()

    # Número de autorización (busca UUID o línea donde se mezcle con NIT)
    match_autorizacion = re.search(r"NÚMERO DE AUTORIZACIÓN:\s*\n?[^:]*\s*Nit Emisor:\s*[^\s]+\s+([A-F0-9\-]{20,})", texto, re.IGNORECASE)
    if not match_autorizacion:
        match_autorizacion = re.search(r"[A-F0-9]{8}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{12}", texto, re.IGNORECASE)
    if match_autorizacion:
        autorizacion = match_autorizacion.group(1).strip()

    return {
        "cliente": cliente,
        "total_facturado": total_facturado,
        "fecha_emision": fecha_emision,
        "nit": nit,
        "autorizacion": autorizacion
    }
