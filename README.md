# Proyecto-Matematicas-Discretas
## Analizador de Lógica Proposicional
Este proyecto trata de un programa desarrollado en Python que permite generar tablas de verdad y transformar una fórmula formula lógica bien formada dada a Forma Normal Disyuntiva (FND). Todo con entrada y salida en formato Latex

Su uso es simple, hay que introducir la fórmula lógica de la que se desea obtener la tabla de verdad, en lo posible asegurarse de que está bien formada y estructurada, luego de esto recibirá la tabla de verdad, acompañada con la fórmula lógica en su Forma Natural Disyuntiva.

## Características

- ✅ **Entrada en LaTeX**: Ingresa fórmulas usando notación LaTeX estándar
- 📊 **Tablas de Verdad**: Generación automática con pasos intermedios
- 🔄 **Transformación a FND**: Conversión paso a paso a Forma Normal Disyuntiva ademas muestra su respectiva tabla de verdad para verificar la Equivalencia con la formula original 
- 🎯 **Tres modos de análisis**: Solo tabla de verdad, solo FND, o análisis completo

## Operadores Soportados

| Operador | LaTeX | Descripción |
|----------|-------|-------------|
| ¬ | `\neg` | Negación |
| ∧ | `\land` | Conjunción (Y lógico) |
| ∨ | `\lor` | Disyunción (O lógico) |
| → | `\rightarrow` | Implicación |
| ↔ | `\leftrightarrow` | Bicondicional |


## Alternativas
### La más simple
- Está la posibilidad de usar el programa sin la interfaz gráfica con solo descargar o copiar el archivo Código_sin_interfaz.py y ejecutarlo en un interprete de python, este tiene inputs en terminal y de igual manera tiene las 3 opciones, tablas de verdad, transformación a FND o ambas.
### Con interfaz gráfica
- Con ayuda de una IA implementamos una interfaz web-gráfica al programa con las librerias pandas, streamlit, numpy y plotly, que permite una interacción más facil y amigable con el usuario, al código original no se le tuvo que cambiar nada, solo se añadió otro módulo con los imports y el código respectivo para la aplicación.
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
4. Completa la instalación.

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
cd Proyecto_final_def2.1
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

## Licencia

Este proyecto es de código abierto



