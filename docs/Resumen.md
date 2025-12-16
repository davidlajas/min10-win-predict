🧠 Explicación del modelo de predicción
1. Objetivo del modelo

El objetivo del modelo es predecir la probabilidad de victoria de un equipo en el minuto 10 de partida en League of Legends, utilizando estadísticas clave del juego temprano.

El modelo no predice el resultado final de forma determinista, sino una probabilidad, lo que permite:

Interpretar el estado de la partida

Tomar decisiones informadas

Integrarse fácilmente en productos de análisis o predicción en tiempo real

2. Variables utilizadas

El modelo trabaja con diferencias entre equipos (Azul − Rojo), ya que lo relevante no es el valor absoluto, sino quién va por delante.

Variables de entrada:

Primera sangre: impacto temprano en oro y presión

Diferencia de asesinatos

Diferencia de asistencias

Diferencia de nivel

Diferencia de súbditos

Diferencia de torretas

Diferencia de dragones

Diferencia de heraldos

👉 Este enfoque hace que el modelo sea:

Más robusto

Menos dependiente del parche

Más generalizable entre partidas

3. Preprocesado de datos

Antes de la predicción:

Se calculan las diferencias entre equipos

Se aplica un escalado estándar (StandardScaler)

El escalado es necesario porque:

Las variables tienen rangos muy distintos

El stacking combina modelos sensibles a la escala

Mejora la estabilidad del entrenamiento y la predicción

4. Tipo de modelo: Stacking

El modelo principal es un Stacking Classifier, una técnica de ensemble learning.

🔹 ¿Qué es el stacking?

El stacking combina varios modelos base y utiliza un modelo final (meta-modelo) que aprende:

“Cuándo confiar más en cada modelo base”

5. Modelos base

El stacking incluye varios modelos con comportamientos distintos, por ejemplo:

Regresión logística → interpretabilidad y estabilidad

Random Forest → captura relaciones no lineales

Gradient Boosting  → alto rendimiento predictivo

Cada modelo base:

Hace su propia predicción

Aporta una visión diferente del estado de la partida

6. Meta-modelo

El meta-modelo (regresión logística) recibe como entrada:

Las probabilidades generadas por los modelos base

Su función es:

Aprender cómo combinar esas probabilidades

Corregir errores individuales

Mejorar la generalización

👉 Esto reduce:

Overfitting

Dependencia de un único algoritmo

7. ¿Por qué se eligió stacking?
✅ Ventajas clave

Combina fortalezas de varios modelos

Reduce el riesgo de decisiones erróneas

Mejora la precisión global

Ofrece predicciones más estables

❌ Alternativas descartadas

Un solo modelo → menos robusto

Deep Learning → excesivo para este volumen de datos

Árbol único → menor capacidad predictiva

8. Interpretación de la salida

El modelo devuelve:

Probabilidad de victoria del equipo


Ejemplo:

0.82 → alta probabilidad de victoria

0.45 → partida equilibrada

0.15 → alta probabilidad de derrota

Estos valores se agrupan en tres estados:

🟢 Alta probabilidad de victoria

🔵 Probabilidad intermedia

🔴 Alta probabilidad de derrota

9. Aplicación en el producto

En la aplicación Streamlit:

El usuario introduce datos de ambos equipos

El sistema calcula diferencias y escala

El modelo predice la probabilidad

Se muestra el resultado desde la perspectiva del usuario

Esto permite:

Uso intuitivo

Análisis en tiempo real

Escalabilidad a otros minutos de la partida

10. Conclusión

El modelo combina:

Buen rendimiento predictivo

Interpretabilidad

Aplicabilidad real

El uso de stacking permite aprovechar múltiples enfoques de aprendizaje automático para ofrecer una predicción robusta, estable y útil, alineada tanto con objetivos técnicos como de negocio.