Predicción de Partidas de League of Legends a 10 Minutos




Descripción

Este proyecto tiene como objetivo predecir el equipo ganador en partidas de League of Legends a los 10 minutos utilizando datos de partidas clasificatorias. Incluye procesos de adquisición y limpieza de datos, ingeniería de features, entrenamiento de múltiples modelos de Machine Learning y despliegue del modelo final a través de una aplicación web interactiva.

Estructura del proyecto
.
├── data
│   ├── raw/                 # Datos originales sin procesar
│   ├── processed/           # Datos procesados listos para modelos
│   ├── train/               # Datos de entrenamiento
│   └── test/                # Datos de prueba
├── notebooks/
│   ├── 01_Fuentes.ipynb          # Adquisición y unión de datos
│   ├── 02_LimpiezaEDA.ipynb      # Limpieza, transformaciones y EDA
│   └── 03_Entrenamiento_Evaluacion.ipynb  # Entrenamiento y evaluación de modelos
├── src/
│   ├── data_processing.py       # Procesamiento de datos desde raw a processed y creación de datasets train/test
│   ├── training.py              # Entrenamiento de modelos 
│   └── evaluation.py            # Evaluación de modelos y generación de métricas
├── models/
│   ├── <nombre>.pkl      # Modelos individuales entrenados
│   ├── final_model<nombre>.pkl          # Modelo final seleccionado
│   └── model_config.yaml        # Configuración de hiperparámetros del modelo final
├── app_streamlit/
│   ├── app.py                   # Aplicación web interactiva para predicciones
│   └── requirements.txt         # Dependencias para la aplicación web
├── docs/                         # Documentación adicional (presentaciones, memoria)
└── README.md                      # Este archivo

Dataset

Fuente: OpenDataBay – League of Legends Ranked Games 10min

Filas: 9879

Columnas originales: 40

Columnas procesadas:

equipo_ganador (0 = azul gana, 1 = rojo gana)

equipo_primera_sangre

Diferencias de métricas clave entre equipos:

asesinatos_dif, asistencias_dif, nivel_dif, minions_dif, torretas_dif, dragones_dif, heraldos_dif

Flujo de trabajo

Adquisición y preparación de datos:

Los notebooks 01_Fuentes.ipynb y 02_LimpiezaEDA.ipynb se encargan de unir las fuentes de datos, limpiar y transformar los datos, y generar las features necesarias.

Procesamiento de datos (src/data_processing.py):

Convierte los datos de data/raw a data/processed.

Genera nuevas columnas basadas en diferencias de métricas entre equipos.

Entrenamiento de modelos (src/training.py):

Entrena varios modelos supervisados y no supervisados.

Guarda modelos individuales en models/trained_model_n.pkl.

Crea train.csv y test.csv en data/train y data/test.

Evaluación de modelos (src/evaluation.py):

Evalúa los modelos utilizando métricas como Accuracy, F1-score y ROC-AUC.

Selecciona el modelo final (final_model.pkl) y genera model_config.yaml.

Despliegue (app_streamlit/app.py):

Permite hacer predicciones interactivas mediante una interfaz web.

Muestra la probabilidad de victoria para cada equipo y alertas según el umbral.

Instalación y requisitos

Clonar el repositorio:

git clone <https://github.com/davidlajas/min10-win-predict>
cd <min10-win-predict>


Instalar dependencias:

pip install -r app_streamlit/requirements.txt


Dependencias principales:

pandas
numpy
scikit-learn
xgboost
tensorflow
matplotlib
seaborn
pyyaml
streamlit


Ejecutar la aplicación web:

streamlit run app_streamlit/app.py

Uso de la aplicación

Selecciona tu equipo (azul o rojo) y la aplicación mostrará:

Probabilidad de victoria de tu equipo.

Estado de alerta basado en los umbrales:

< 0.2: alta probabilidad de perder ⚠️

0.7: alta probabilidad de ganar ✅

0.2 – 0.7: probabilidad intermedia 🔹

Licencia

MIT License – ver archivo LICENSE para más detalles.