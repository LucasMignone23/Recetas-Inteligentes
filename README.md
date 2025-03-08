# Recetas Inteligentes

## Descripción

Recetas Inteligentes es una aplicación web que permite a los usuarios ingresar ingredientes y obtener recetas sugeridas por IA. Utiliza la API de Google Gemini para generar recetas en función de los ingredientes ingresados.

## Características

* Ingreso de ingredientes
* Generación de recetas con IA
* Interfaz intuitiva con Streamlit
* Integración con la API de Google Gemini

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/recetas-inteligentes.git
   cd recetas-inteligentes
   ```
2. Crea un entorno virtual e instale las dependencias:
   ```bash
   python -m venv env
   source env/bin/activate  # En macOS y Linux
   env\Scripts\activate  # En Windows
   pip install -r requirements.txt
   ```
3. Configura tu clave de API de Google Gemini creando un archivo `.env` en la raíz del proyecto:
   ```env
   GOOGLE_API_KEY=tu_api_key
   ```

## Uso

Ejecuta la aplicación con:

```bash
streamlit run app.py
```

Esto abrirá la aplicación en tu navegador.
