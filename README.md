# CV

Generador del CV en PDF a partir de un script Python con [ReportLab](https://www.reportlab.com/).

## Requisitos

- Python 3
- ReportLab (`reportlab==4.5.1`)

## Generar el PDF

1. Crea y activa el entorno virtual (si no existe ya):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install reportlab
   ```

2. Ejecuta el script:

   ```bash
   venv/bin/python generate_cv.py
   ```

3. El PDF se genera en `cv_javier_polo_updated.pdf`, en la raíz del proyecto.

> Nota: `foto.png` debe estar presente en la raíz del proyecto, ya que el script la usa como foto de perfil.
