# Proyecto-Matematicas-Discretas
Este proyecto trata de un programa desarrollado en Python que realiza la tabla de verdad de una formula lógica bien formada dada. Además convierte la formula en su Forma Normal Disyuntiva (FND). Todo con entrada y salida en formato Latex

La instalación del programa es solo el ".py" y su ejecución. Asegurarse de tener las librerías correctamente instaladas

Su uso es simple, hay que introducir la fórmula lógica de la que se desea obtener la tabla de verdad, en lo posible asegurarse de que está bien formada y estructurada, luego de esto recibirá la tabla de verdad, acompañada con la fórmula lógica en su Forma Natural Disyuntiva.


## 📌 Requerimientos

## 🐧 Método para Linux/Mac

# Analizador de Lógica Proposicional

Una herramienta web interactiva para el análisis de fórmulas de lógica proposicional que permite generar tablas de verdad y transformar fórmulas a Forma Normal Disyuntiva (FND).

## Características

- ✅ **Entrada en LaTeX**: Ingresa fórmulas usando notación LaTeX estándar
- 📊 **Tablas de Verdad**: Generación automática con pasos intermedios
- 🔄 **Transformación a FND**: Conversión paso a paso a Forma Normal Disyuntiva
- 🎯 **Tres modos de análisis**: Solo tabla de verdad, solo FND, o análisis completo
- 📱 **Interfaz responsiva**: Funciona en desktop y móvil
- 📥 **Exportación**: Descarga resultados en LaTeX, CSV o PNG

## Operadores Soportados

| Operador | LaTeX | Descripción |
|----------|-------|-------------|
| ¬ | `\neg` | Negación |
| ∧ | `\land` | Conjunción (Y lógico) |
| ∨ | `\lor` | Disyunción (O lógico) |
| → | `\rightarrow` | Implicación |
| ↔ | `\leftrightarrow` | Bicondicional |

## Instalación

### 1. Verificar la instalación de Python

Abre tu terminal o línea de comandos y ejecuta:

```bash
python --version
```

Si ves un mensaje como `Python 3.x.x`, ya tienes Python instalado. **Si aparece un error o "not found", continúa con el paso 2.**

### 2. Instalar Python (si no está instalado)

#### Windows:
1. Ve a [python.org/downloads](https://python.org/downloads/)
2. Descarga la versión más reciente de Python (3.11 o superior)
3. **IMPORTANTE**: Durante la instalación, marca la casilla "Add Python to PATH"
4. Completa la instalación

#### macOS:
```bash
# Usando Homebrew (recomendado)
brew install python

# O descarga desde python.org
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 3. Verificar la instalación de pip

```bash
pip --version
```

Si no funciona, intenta:
```bash
python -m pip --version
```

### 4. Instalar las dependencias

```bash
pip install streamlit pandas numpy plotly
```

Si tienes problemas de permisos en Windows, usa:
```bash
pip install --user streamlit pandas numpy plotly
```

### 5. Descargar el proyecto

#### Opción A: Clonar con Git
```bash
git clone [URL_DEL_REPOSITORIO]
cd analizador-logica-proposicional
```

#### Opción B: Descargar ZIP
1. Descarga el archivo ZIP del repositorio
2. Extrae los archivos
3. Navega a la carpeta del proyecto

### 6. Ejecutar la aplicación

```bash
streamlit run logic_app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`.

## Uso Básico

### Ejemplo de Fórmula
```latex
((p \rightarrow q) \leftrightarrow (\neg q \lor r))
```

### Pasos para usar:
1. Selecciona el tipo de análisis en la barra lateral
2. Ingresa tu fórmula en formato LaTeX
3. Haz clic en "🚀 Analizar Fórmula"
4. Explora los resultados y exporta si es necesario

## Ejemplos de Fórmulas

| Descripción | Fórmula LaTeX |
|-------------|---------------|
| Modus Ponens | `(p \land (p \rightarrow q)) \rightarrow q` |
| Ley de De Morgan | `\neg (p \land q) \leftrightarrow (\neg p \lor \neg q)` |
| Distributividad | `p \land (q \lor r) \leftrightarrow ((p \land q) \lor (p \land r))` |
| Contraposición | `(p \rightarrow q) \leftrightarrow (\neg q \rightarrow \neg p)` |

## Estructura del Proyecto

```
.
├── logic_app.py           # Aplicación principal de Streamlit
├── logic_formulas.py      # Clases y funciones de lógica proposicional
├── .streamlit/
│   └── config.toml       # Configuración de Streamlit
└── README.md             # Este archivo
```

## Solución de Problemas

### Error: 'python' no se reconoce
- **Windows**: Reinstala Python marcando "Add Python to PATH"
- **macOS/Linux**: Usa `python3` en lugar de `python`

### Error: 'pip' no se reconoce
```bash
python -m pip install streamlit pandas numpy plotly
```

### Error: Puerto en uso
```bash
streamlit run logic_app.py --server.port 8502
```

### Problemas con caracteres especiales
Asegúrate de que tu terminal soporte UTF-8 o usa un editor de texto con codificación UTF-8.

## Alternativas de Instalación

### Opción 1: Anaconda (Recomendado para principiantes)
1. Descarga [Anaconda](https://anaconda.com/download)
2. Instala Anaconda
3. Abre "Anaconda Prompt"
4. Ejecuta: `conda install streamlit pandas numpy plotly`
5. Ejecuta: `streamlit run logic_app.py`

### Opción 2: Entorno Virtual (Recomendado para desarrolladores)
```bash
# Crear entorno virtual
python -m venv logic_env

# Activar entorno (Windows)
logic_env\Scripts\activate

# Activar entorno (macOS/Linux)
source logic_env/bin/activate

# Instalar dependencias
pip install streamlit pandas numpy plotly

# Ejecutar aplicación
streamlit run logic_app.py
```

### Opción 3: requirements.txt
Si tienes un archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Contribuir

Las contribuciones son bienvenidas. Por favor:
1. Haz fork del repositorio
2. Crea una rama para tu feature
3. Haz commit de tus cambios
4. Push a la rama
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Si tienes preguntas o encuentras problemas, por favor abre un issue en el repositorio.


