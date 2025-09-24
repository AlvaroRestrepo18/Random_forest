# Sistema de Diagnóstico Médico con IA - Random Forest
import streamlit as st
import subprocess
import sys
from pathlib import Path

# Configuración de la página
st.set_page_config(
    page_title="Sistema Random Forest",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E8B57;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .nav-button {
        width: 100%;
        margin: 0.5rem 0;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        font-size: 1.1rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .nav-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .info-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 5px solid #2E8B57;
    }
</style>
""", unsafe_allow_html=True)


# Contenido principal
st.markdown('<h1 class="main-header">🌳 Random Forest</h1>', unsafe_allow_html=True)

# Información sobre Random Forest
st.markdown("""
<div class="info-box">
<h3>🤖 ¿Qué es Random Forest?</h3>
Random Forest es un algoritmo de aprendizaje automático que agrupa múltiples árboles de decisión para realizar predicciones más precisas y robustas. Funciona creando muchos árboles independientes, cada uno entrenado en subconjuntos aleatorios de los datos y características, para luego combinar sus predicciones (por votación o promedio) y obtener un resultado final confiable.
</div>
""", unsafe_allow_html=True)

# Imagen
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://cdn.dida.do/bird-(9)-1733138076.png", width=400)

# Características del sistema
st.markdown("## 🚀 Características del Sistema")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🏥 Sistema de Diagnóstico
    - ✅ Evaluación de 10 síntomas médicos
    - ✅ Detección de emergencias críticas
    - ✅ Análisis de probabilidades detallado
    - ✅ Interfaz web moderna e intuitiva
    """)

with col2:
    st.markdown("""
    ### 🎯 Entrenamiento Personalizado
    - ✅ Configuración de número de árboles
    - ✅ Ajuste de parámetros del modelo
    - ✅ Visualizaciones de resultados
    - ✅ Métricas de evaluación completas
    """)

# Preguntas de estudio
st.markdown("## 📚 Preguntas de Estudio")
st.markdown("*Responde de forma clara y completa. Puedes utilizar ejemplos para enriquecer tus respuestas.*")

with st.expander("🤔 Ver preguntas sobre Random Forest"):
    st.markdown("""
    1. **¿Qué es el algoritmo Random Forest y para qué se utiliza?**
    
       **Respuesta:** Random Forest (Bosque Aleatorio) es un algoritmo de aprendizaje automático supervisado que se utiliza para problemas de clasificación y regresión. Funciona creando múltiples árboles de decisión durante el entrenamiento y combinando sus predicciones para obtener resultados más precisos y robustos.

    2. **Explica cómo funciona Random Forest durante la fase de entrenamiento.**
    
       **Respuesta:** Durante el entrenamiento:
       - Se crean múltiples subconjuntos de datos mediante **bootstrapping** (muestreo con reemplazo)
       - Para cada subconjunto, se entrena un árbol de decisión
       - En cada división del árbol, solo se considera un subconjunto aleatorio de características
       - Los árboles crecen sin poda hasta su máxima profundidad

    3. **¿Por qué Random Forest se considera un algoritmo de ensamble?**
    
       **Respuesta:** Se considera un algoritmo de ensamble porque combina las predicciones de múltiples modelos débiles (árboles de decisión individuales) para formar un modelo más fuerte y robusto. Esta técnica se conoce como **bagging** (Bootstrap Aggregating).

    4. **¿Cuál es la diferencia principal entre un árbol de decisión y un Random Forest?**
    
       **Respuesta:** La principal diferencia es que un árbol de decisión es un modelo único que puede sufrir de sobreajuste (overfitting), mientras que Random Forest combina múltiples árboles, reduciendo el sobreajuste y mejorando la generalización mediante el principio de "la sabiduría de las multitudes".

    5. **¿Qué ventajas ofrece Random Forest frente a otros modelos de aprendizaje supervisado?**
    
       **Respuesta:** Ventajas principales:
       - Menor sobreajuste que los árboles individuales
       - Alta precisión en muchos problemas
       - Maneja bien datos con missing values
       - No requiere normalización de características
       - Proporciona importancia de características
       - Funciona bien con datasets grandes

    6. **Menciona dos aplicaciones reales en las que se podría usar Random Forest.**
    
       **Respuesta:** 
       - **Diagnóstico médico**: Clasificación de enfermedades basada en síntomas y pruebas médicas
       - **Detección de fraude**: Identificación de transacciones fraudulentas en tarjetas de crédito

    7. **¿Qué significa el término "bootstrap" en el contexto de Random Forest?**
    
       **Respuesta:** Bootstrap se refiere a la técnica de muestreo con reemplazo donde se crean múltiples subconjuntos del dataset original, permitiendo que algunas instancias aparezcan múltiples veces en un mismo subconjunto mientras otras pueden no aparecer.
    """)

# Footer
st.markdown("---")
st.markdown("🔬 **Desarrollado con Streamlit y scikit-learn** | 🌳 **Random Forest ML System**")
