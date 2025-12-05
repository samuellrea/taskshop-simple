# TaskShop - Tienda de Productos Digitales

## Visión General
TaskShop es una aplicación de e-commerce simple para vender productos digitales (plantillas, cursos, recargas) desarrollada en Python. Incluye interfaz gráfica con Tkinter y versión de consola.

## Requisitos
- Python 3.12.10 o superior
- Tkinter (viene con Python en Windows)

## Instalación y Configuración del Entorno Virtual

### 1. Crear entorno virtual
```bash
# En Windows
python -m venv .venv

# En Linux/Mac
python3 -m venv .venv

2. Activar entorno virtual
bash
# Windows (CMD/PowerShell)
.venv\Scripts\activate

# Windows (Git Bash)
source .venv/Scripts/activate

# Linux/Mac
source .venv/bin/activate

3. Verificar que el entorno está activo
bash

4. Instalar dependencias (si las hubiera)
bash
# En este proyecto no hay dependencias externas
# Tkinter viene incluido con Python

5. Desactivar entorno virtual
bash
deactivate


Ejecución
bash

Modo Demo Automático
python -m src.taskshop
Interfaz Gráfica (Tkinter)
python src/taskshop/simple_gui.py
Interfaz de Consola
python src/taskshop/cli_app.py


Pruebas Unitarias

### Ejecutar tests (método recomendado):
```bash
# Usar el script de tests
python run_tests.py

# O usar pytest si está instalado
pytest tests/ -v


Estructura del Proyecto
text
taskshop/
├── src/
│   └── taskshop/
│       ├── __init__.py
│       ├── models.py           # Modelos de datos
│       ├── simple_gui.py       # Interfaz gráfica Tkinter
│       ├── cli_app.py          # Interfaz de consola
│       └── __main__.py         # Punto de entrada principal
├── tests/
│   └── test_basic.py          # Tests unitarios
├── .venv/                     # Entorno virtual (NO subir a Git)
├── pyproject.toml             # Configuración del proyecto
├── .gitignore                 # Archivos a ignorar en Git
├── README.md                  # Este archivo
└── LICENSE                    # Licencia MIT

Notas Técnicas
Uso del Entorno Virtual
Recomendado: Activar siempre el entorno virtual antes de trabajar

Git: El directorio .venv/ está en .gitignore 

Replicar entorno: Otros desarrolladores deben crear su propio .venv

Solución de Problemas
Si tienes problemas con Tkinter:

bash
# Verificar instalación de Python
python --version

# Probar Tkinter
python -c "import tkinter; print('Tkinter funciona')"

Roadmap Breve
Versión básica con interfaz gráfica y consola
Mejoras en la interfaz gráfica
Sistema de persistencia con archivos
Más tests automatizados
Documentación ampliada

Autores
Iker Hernández

Juan Luis Sanz

Pablo Gila

Rodrigo Povedano

Samuel Larrea

Licencia
MIT License - ver archivo LICENSE

**ARCHIVO ADICIONAL: `requirements.txt`** (opcional obviamente profe)

TaskShop - Dependencias:

Python 3.12.10
No hay dependencias externas
Tkinter viene incluido con Python
Para desarrollo (opcional):
pytest>=7.0
black>=23.0
ruff>=0.1.0

Ejecución Rápida 

Archivo Todo en Uno:
python todo_en_uno.py

## CI/CD con GitHub Actions

El proyecto incluye un workflow de GitHub Actions que:
-  Ejecuta tests automáticamente en cada push
-  Verifica formato con Black
-  Verifica estilo con Ruff
-  Valida la estructura del proyecto

##Configuración

Archivo `.env.example` con variables de configuración.
**Importante:** No subas el archivo `.env` real al repositorio.

## 🔧 Hooks Pre-commit

Instalar hooks:
```bash
python install_hooks.py