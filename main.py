import streamlit as st
import pandas as pd
import morosos_credit_card
import re

# Título de la aplicación
st.title("Predicción de Morosidad con IA")

st.markdown("""
Esta aplicación utiliza un modelo de Machine Learning para predecir si un cliente caerá en morosidad. 
Introduce los datos en los campos proporcionados y haz clic en "Realizar Predicción" para obtener el resultado.
""")

# Sidebar: Captura de datos del cliente
st.sidebar.header("Introduce los datos del cliente")

# Función para extraer el número entre paréntesis en las opciones
def extract_number(text):
    match = re.search(r'\((\d+)\)', text)
    if match:
        return int(match.group(1))
    return 0  # Valor predeterminado en caso de que no haya coincidencia

def user_input_features():
    sex = st.sidebar.selectbox("Sexo", options=["Masculino (1)", "Femenino (2)"], index=1, key="sexo")
    education = st.sidebar.selectbox("Educación", options=["Graduate School (1)", "University (2)", "High School (3)", "Others (4)"], index=1, key="educacion")
    marriage = st.sidebar.selectbox("Estado Civil", options=["Casado (1)", "Soltero (2)", "Otros (3)"], index=0, key="estado_civil")
    age = st.sidebar.slider("Edad", min_value=18, max_value=100, value=30, step=1, key="edad")
    pay_0 = st.sidebar.slider("Estado de Pago (Septiembre)", min_value=-1, max_value=9, value=0, key="pay_0")
    pay_2 = st.sidebar.slider("Estado de Pago (Agosto)", min_value=-1, max_value=9, value=0, key="pay_2")
    pay_3 = st.sidebar.slider("Estado de Pago (Julio)", min_value=-1, max_value=9, value=0, key="pay_3")
    pay_4 = st.sidebar.slider("Estado de Pago (Junio)", min_value=-1, max_value=9, value=0, key="pay_4")
    pay_5 = st.sidebar.slider("Estado de Pago (Mayo)", min_value=-1, max_value=9, value=0, key="pay_5")
    pay_6 = st.sidebar.slider("Estado de Pago (Abril)", min_value=-1, max_value=9, value=0, key="pay_6")

    # Crear un DataFrame con los datos del usuario
    data = {
        "SEX": extract_number(sex),
        "EDUCATION": extract_number(education),
        "MARRIAGE": extract_number(marriage),
        "AGE": age,
        "PAY_0": pay_0,
        "PAY_2": pay_2,
        "PAY_3": pay_3,
        "PAY_4": pay_4,
        "PAY_5": pay_5,
        "PAY_6": pay_6
    }
    return pd.DataFrame(data, index=[0])

# Crear un DataFrame vacío para almacenar las entradas
if 'input_data' not in st.session_state:
    st.session_state.input_data = pd.DataFrame(columns=["SEX", "EDUCATION", "MARRIAGE", "AGE", "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6"])

# Estado del formulario en session_state
if 'form_visible' not in st.session_state:
    st.session_state.form_visible = False

# Botón para mostrar el formulario de datos
if st.sidebar.button("Mostrar Formulario de Datos", key="show_form"):
    st.session_state.form_visible = not st.session_state.form_visible

# Mostrar el formulario de datos solo si 'form_visible' es True
if st.session_state.form_visible:
    input_df = user_input_features()
    st.session_state.input_data_temp = input_df

# Botón para agregar los datos al DataFrame
if st.sidebar.button("Agregar Datos", key="add_data"):
    if 'input_data_temp' in st.session_state:
        st.session_state.input_data = pd.concat([st.session_state.input_data, st.session_state.input_data_temp], ignore_index=True)
        st.session_state.input_data_temp = None  # Limpiar los datos temporales después de agregarlos

# Mostrar los datos ingresados
st.subheader("Datos Ingresados")
st.write(st.session_state.input_data)

# Opción para borrar una fila
row_to_delete = st.selectbox("Selecciona la fila para borrar:", range(len(st.session_state.input_data)))
if st.button("Borrar Fila Seleccionada", key="delete_row"):
    if len(st.session_state.input_data) > 0:
        st.session_state.input_data = st.session_state.input_data.drop(row_to_delete).reset_index(drop=True)

# Realizar la predicción al hacer clic en el botón
if st.button("Realizar Predicción", key="predict"):
    if len(st.session_state.input_data) > 0:
        # Asegurarse de que los datos son numéricos
        st.session_state.input_data = st.session_state.input_data.apply(pd.to_numeric, errors='coerce')
        
        # Ahora puedes pasar el DataFrame al modelo
        prediccion = morosos_credit_card.predecir(st.session_state.input_data)

        # Mostrar el resultado
        st.subheader("Resultado de la Predicción")
        if prediccion[0] == 1:
            st.error("El cliente tiene alta probabilidad de ser moroso.")
        else:
            st.success("El cliente probablemente no será moroso.")
    else:
        st.warning("Por favor, agrega algunos datos antes de realizar la predicción.")
