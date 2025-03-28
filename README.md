# Proyecto RPA para Facturación - Emprendentro

Este proyecto es una simulación de un sistema de Automatización de Procesos Robóticos (RPA) diseñado para la clase de **Emprendentro**. Utiliza el framework **Flask** para crear un servidor localhost que permite gestionar bots encargados de tareas relacionadas con la facturación y otros procesos administrativos.

## Objetivo

El objetivo principal es demostrar cómo los RPA pueden automatizar tareas repetitivas y optimizar procesos empresariales, utilizando un entorno simulado en un servidor local.

## Características

- **Servidor Flask**: Actúa como el backend para gestionar las solicitudes y coordinar los bots.
- **Bots de Facturación**: Automatizan la generación y envío de facturas.
- **Tareas Adicionales**: Los bots pueden realizar otras tareas administrativas como validación de datos o generación de reportes.
- **Simulación Local**: Todo el sistema funciona en un entorno localhost para fines educativos.

## Requisitos

- **Python 3.8+**
- **Flask**: Framework para el servidor web.
- **Dependencias adicionales**: Se encuentran en el archivo `requirements.txt`.

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/jricica/RPAemp.git
    cd RPAemp
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Ejecuta el servidor:
    ```bash
    python app.py
    ```

4. Accede al servidor en tu navegador:
    ```
    http://localhost:5000
    ```

## Estructura del Proyecto

```
RPAemp/
├── app.py               # Archivo principal del servidor Flask
├── bots/
│   ├── factura_bot.py   # Bot para generación de facturas
│   └── otros_bots.py    # Otros bots administrativos
├── templates/           # Archivos HTML para la interfaz
├── static/              # Archivos estáticos (CSS, JS, imágenes)
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación del proyecto
```

## Uso

1. Inicia el servidor Flask.
2. Accede a la interfaz web para interactuar con los bots.
3. Configura las tareas que deseas automatizar desde el panel de control.

## Contribuciones

Si deseas contribuir al proyecto, por favor realiza un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para cualquier consulta, puedes contactarme en [janricica@ufm.edu](mailto:janricica@ufm.edu).
