import streamlit as st
import numpy as np
import pickle
import os


current_dir = os.path.dirname(__file__)

stack_path = os.path.join(current_dir, '..', 'models','final_model_stacking.pkl')

scaler_path = os.path.join(current_dir, '..', 'models','scaler.pkl')

with open(stack_path, "rb") as f:  # reemplaza con la ruta correcta
    stack = pickle.load(f)

with open(scaler_path, "rb") as f:  # reemplaza con la ruta correcta
    scaler = pickle.load(f)





st.set_page_config(page_title="Predicción LoL", layout="wide")


# ---------- TÍTULO ----------
st.title("Predicción de victoria – Minuto 10 (LoL)")

# ---------- EQUIPO USUARIO ----------
lado_usuario = st.radio(
    "¿En qué equipo estás?",
    ["Azul", "Rojo"],
    horizontal=True
)

# ---------- COLOR BOTÓN ----------
color_boton = "#1f77b4" if lado_usuario == "Azul" else "#d62728"

st.markdown(
    f"""
    <style>
    div.stButton > button {{
        background-color: {color_boton};
        color: white;
        font-size: 18px;
        font-weight: bold;
        height: 3em;
        border-radius: 8px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- PRIMERA SANGRE ----------
primera_sangre = st.radio(
    "Primera sangre",
    ["Azul", "Rojo"],
    horizontal=True
)

ps_azul = 1 if primera_sangre == "Azul" else 0
ps_rojo = 1 - ps_azul

# ---------- INPUTS ----------
col_azul, col_rojo = st.columns(2)

def inputs_equipo(nombre, key):
    st.subheader(nombre)
    return {
        "asesinatos": st.number_input("Asesinatos", min_value=0, value=0, key=f"{key}_asesinatos"),
        "asistencias": st.number_input("Asistencias", min_value=0, value=0, key=f"{key}_asistencias"),
        "nivel": st.number_input("Nivel medio", min_value=0, value=0, key=f"{key}_nivel"),
        "subditos": st.number_input("Súbditos", min_value=0, value=0, key=f"{key}_subditos"),
        "torretas": st.number_input("Torretas", min_value=0, value=0, key=f"{key}_torretas"),
        "dragones": st.number_input("Dragones", min_value=0, value=0, key=f"{key}_dragones"),
        "heraldos": st.number_input("Heraldos", min_value=0, value=0, key=f"{key}_heraldos"),
    }

with col_azul:
    azul = inputs_equipo("🔵 Equipo Azul", "azul")

with col_rojo:
    rojo = inputs_equipo("🔴 Equipo Rojo", "rojo")

# ---------- PREDICCIÓN ----------
if st.button("🔮 Predecir resultado"):

    X = np.array([[
        ps_azul - ps_rojo,
        azul["asesinatos"] - rojo["asesinatos"],
        azul["asistencias"] - rojo["asistencias"],
        azul["nivel"] - rojo["nivel"],
        azul["subditos"] - rojo["subditos"],
        azul["torretas"] - rojo["torretas"],
        azul["dragones"] - rojo["dragones"],
        azul["heraldos"] - rojo["heraldos"],
    ]])

    X_scaled = scaler.transform(X)

    prob_rojo = stack.predict_proba(X_scaled)[0, 1]
    prob_azul = 1 - prob_rojo

    prob_usuario = prob_azul if lado_usuario == "Azul" else prob_rojo

    # ---------- RESULTADO ----------
    st.markdown("---")
    st.subheader(f"Resultado para el equipo {lado_usuario}")

    st.metric(
        label="Probabilidad de victoria",
        value=f"{prob_usuario:.2%}"
    )

    if prob_usuario < 0.2:
        st.error("⚠️ Alta probabilidad de derrota")
    elif prob_usuario > 0.7:
        st.success("✅ Alta probabilidad de victoria")
    else:
        st.info("🔹 Probabilidad intermedia")


