import streamlit as st
import pandas as pd
from logic_formulas import *

# Configurar la página
st.set_page_config(
    page_title="Analizador de Lógica Proposicional",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para mejorar la visualización de LaTeX
st.markdown("""
<style>
.latex-formula {
    font-size: 18px;
    text-align: center;
    padding: 10px;
    background-color: #f0f2f6;
    
    border-radius: 5px;
    margin: 10px 0;
}
.truth-table {
    margin: 20px 0;
}
.step-explanation {
    background-color: #e8f4f8;
    padding: 10px;
    border-left: 4px solid #0e7b8a;
    margin: 10px 0;
    color: #0E1117;
}
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🧠 Analizador de Lógica Proposicional")
    st.markdown("*Herramienta para analizar fórmulas lógicas, generar tablas de verdad y obtener la Forma Normal Disyuntiva*")
    
    # Sidebar con opciones
    st.sidebar.header("⚙️ Opciones de Análisis")
    
    analysis_type = st.sidebar.radio(
        "Selecciona qué análisis realizar:",
        [
            "📊 Solo Tabla de Verdad Original",
            "🔄 Solo Forma Normal Disyuntiva",
            "🔍 Análisis Completo"
        ]
    )
    
    # Información sobre el formato LaTeX
    with st.sidebar.expander("ℹ️ Formato LaTeX"):
        st.markdown("""
        **Operadores soportados:**
        - `\\neg` : Negación (¬)
        - `\\land` : Conjunción (∧)
        - `\\lor` : Disyunción (∨)
        - `\\rightarrow` : Implicación (→)
        - `\\leftrightarrow` : Bicondicional (↔)
        
        **Ejemplo:**
        `((p \\rightarrow q) \\leftrightarrow (\\neg q \\lor r))`
        """)
    
    # Ejemplos predefinidos
    with st.sidebar.expander("📚 Ejemplos"):
        ejemplos = {
            "Ejemplo 1": "((p \\rightarrow q) \\leftrightarrow (\\neg q \\lor r))",
            "Ejemplo 2": "(p \\land q) \\rightarrow (r \\lor s)",
            "Ejemplo 3": "\\neg (p \\land q) \\leftrightarrow (\\neg p \\lor \\neg q)",
            "Ejemplo 4": "p \\rightarrow (q \\rightarrow r)",
            "Ejemplo 5": "(p \\lor q) \\land (\\neg p \\lor r)"
        }
        
        for nombre, formula in ejemplos.items():
            if st.button(nombre, key=f"btn_{nombre}"):
                st.session_state.formula_input = formula
    
    # Input principal
    st.header("📝 Entrada de Fórmula")
    
    # Campo de entrada con valor por defecto
    default_formula = getattr(st.session_state, 'formula_input', "((p \\rightarrow q) \\leftrightarrow (\\neg q \\lor r))")
    
    formula_input = st.text_area(
        "Ingrese la fórmula en formato LaTeX:",
        value=default_formula,
        height=100,
        help="Ejemplo: ((p \\rightarrow q) \\leftrightarrow (\\neg q \\lor r))"
    )
    
    if st.button("🚀 Analizar Fórmula", type="primary"):
        if formula_input.strip():
            try:
                # Procesar la fórmula
                formula_original = latex_string_to_formula(formula_input)
                
                # Mostrar fórmula original
                st.header("📋 Fórmula Original")
                latex_original = formula_original.to_latex()
                st.latex(latex_original)
                
                # Análisis según la opción seleccionada
                if analysis_type == "📊 Solo Tabla de Verdad Original":
                    mostrar_tabla_verdad_original(formula_original)
                
                elif analysis_type == "🔄 Solo Forma Normal Disyuntiva":
                    mostrar_fnd_solamente(formula_original)
                
                elif analysis_type == "🔍 Análisis Completo":
                    mostrar_analisis_completo(formula_original)
                    
            except Exception as e:
                st.error(f"❌ Error al procesar la fórmula: {str(e)}")
                st.info("Verifique que la sintaxis LaTeX sea correcta. Consulte la ayuda en la barra lateral.")
        else:
            st.warning("⚠️ Por favor, ingrese una fórmula válida.")

def mostrar_tabla_verdad_original(formula):
    """Muestra solo la tabla de verdad de la fórmula original"""
    st.header("📊 Tabla de Verdad")
    
    # Generar tabla de verdad
    tabla = tabla_verdad(formula)
    
    # Convertir a DataFrame para mejor visualización
    df = pd.DataFrame(tabla[1:], columns=tabla[0])
    
    # Mostrar tabla
    st.dataframe(df, use_container_width=True)
    
    # Mostrar en formato LaTeX
    with st.expander("📄 Ver en formato LaTeX"):
        latex_table = tabla_verdad_a_latex(tabla)
        st.code(latex_table, language="latex")

def mostrar_fnd_solamente(formula):
    """Muestra solo la transformación a FND"""
    st.header("🔄 Transformación a Forma Normal Disyuntiva")
    
    # Paso 1: Eliminar implicaciones
    sin_implicaciones = eliminate_implications(formula)
    st.subheader("Paso 1: Eliminar Implicaciones")
    st.markdown('<div class="step-explanation" >Convertimos → y ↔ usando equivalencias lógicas</div>', unsafe_allow_html=True)
    latex_paso1 = sin_implicaciones.to_latex()
    st.latex(latex_paso1)
    
    # Paso 2: Mover negaciones hacia adentro
    negaciones_internas = move_negations_inward(sin_implicaciones)
    st.subheader("Paso 2: Aplicar Leyes de De Morgan")
    st.markdown('<div class="step-explanation">Movemos las negaciones hacia las variables usando las leyes de De Morgan</div>', unsafe_allow_html=True)
    latex_paso2 = negaciones_internas.to_latex()
    st.latex(latex_paso2)
    
    # Paso 3: Distribuir disyunciones
    fnd_final = distribute_or_over_and(negaciones_internas)
    st.subheader("Paso 3: Distribuir Disyunciones")
    st.markdown('<div class="step-explanation">Aplicamos la propiedad distributiva para obtener la FND</div>', unsafe_allow_html=True)
    latex_fnd = fnd_final.to_latex()
    st.latex(latex_fnd)
    
    # Resultado final
    st.subheader("✅ Forma Normal Disyuntiva Final")
    formula_simplificada = simplify_formula(fnd_final)
    latex_final = formula_simplificada.to_latex()
    st.latex(latex_final)

def mostrar_analisis_completo(formula):
    """Muestra el análisis completo"""
    
    # Tabla de verdad original
    st.header("📊 Tabla de Verdad Original")
    tabla_orig = tabla_verdad(formula)
    df_orig = pd.DataFrame(tabla_orig[1:], columns=tabla_orig[0])
    st.dataframe(df_orig, use_container_width=True)

        # Mostrar en formato LaTeX
    with st.expander("📄 Ver en formato LaTeX"):
        latex_table = tabla_verdad_a_latex(tabla_orig)
        st.code(latex_table, language="latex")
    
    # Transformación a FND con pasos
    st.header("🔄 Transformación a Forma Normal Disyuntiva")

    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Pasos de Transformación")
        
        # Paso 1
        sin_implicaciones = eliminate_implications(formula)
        st.write("**1. Eliminar Implicaciones:**")
        latex_paso1 = sin_implicaciones.to_latex()
        st.latex(latex_paso1)
        
        # Paso 2
        negaciones_internas = move_negations_inward(sin_implicaciones)
        st.write("**2. Leyes de De Morgan:**")
        latex_paso2 = negaciones_internas.to_latex()
        st.latex(latex_paso2)
        
        # Paso 3
        fnd_final = distribute_or_over_and(negaciones_internas)
        st.write("**3. Distribución:**")
        latex_fnd = fnd_final.to_latex()
        st.latex(latex_paso1)
    
    with col2:
        st.subheader("Explicaciones")
        st.markdown("""
        **Paso 1:** Reemplazamos:
        - A → B por ¬A ∨ B
        - A ↔ B por (A → B) ∧ (B → A)
        
        **Paso 2:** Aplicamos:
        - ¬(A ∧ B) ≡ ¬A ∨ ¬B
        - ¬(A ∨ B) ≡ ¬A ∧ ¬B
        - ¬¬A ≡ A
        
        **Paso 3:** Distribuimos:
        - A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C)
        """)
    
    # FND final
    st.subheader("✅ Forma Normal Disyuntiva Final")
    formula_simplificada = simplify_formula(fnd_final)
    latex_final = formula_simplificada.to_latex()
    st.latex(latex_final)
    
    # Tabla de verdad de la FND
    st.header("📊 Tabla de Verdad de la FND")
    tabla_fnd = tabla_verdad(formula_simplificada)
    df_fnd = pd.DataFrame(tabla_fnd[1:], columns=tabla_fnd[0])
    st.dataframe(df_fnd, use_container_width=True)
    
        # Mostrar en formato LaTeX
    with st.expander("📄 Ver en formato LaTeX"):
        latex_fnd_table = tabla_verdad_a_latex(tabla_fnd)
        st.code(latex_fnd_table, language="latex")

    # Verificación de equivalencia
    st.header("✔️ Verificación de Equivalencia")
    
    # Comparar las columnas principales de ambas tablas
    col_original = df_orig.iloc[:, -1].tolist()  # Última columna (fórmula principal)
    col_fnd = df_fnd.iloc[:, -1].tolist()  # Última columna (FND)
    
    if col_original == col_fnd:
        st.success("✅ Las fórmulas son equivalentes: ambas tienen los mismos valores de verdad.")
    else:
        st.error("❌ Error: Las fórmulas no son equivalentes.")


if __name__ == "__main__":
    main()