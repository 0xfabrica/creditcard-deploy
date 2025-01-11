```markdown
# Credit Card Fraud Detection with Streamlit

Este proyecto implementa un sistema de detección de fraude en tarjetas de crédito utilizando aprendizaje automático. La aplicación está desarrollada con **Streamlit** para proporcionar una interfaz interactiva y fácil de usar.

🌐 **Prueba la aplicación aquí**: [Credit Card Fraud Detection App](https://creditcard-deploy.streamlit.app/)

---

## 🚀 Características

- **Interfaz interactiva**: Permite a los usuarios ingresar datos manualmente o cargar un archivo con múltiples registros.
- **Predicciones en tiempo real**: Utiliza un modelo de **XGBoost** para predecir si una transacción es fraudulenta.
- **Gestión de datos personalizada**:
  - Agregar múltiples registros manualmente.
  - Visualizar los datos ingresados en tiempo real.
  - Eliminar registros del conjunto de datos antes de realizar la predicción.

---

## 📂 Estructura del Proyecto

```
creditcard-deploy/
├── main.py                 # Archivo principal para ejecutar la app Streamlit
├── morosos_credit_card.py  # Módulo que incluye funciones para cargar el modelo y realizar predicciones
├── requirements.txt        # Lista de dependencias necesarias
└── README.md               # Documentación del proyecto
```

---

## 🛠️ Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/0xfabrica/creditcard-deploy.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd creditcard-deploy
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:

   ```bash
   streamlit run main.py
   ```

---

## 🧠 Modelo de Machine Learning

El modelo está basado en **XGBoost**, entrenado para detectar transacciones fraudulentas en tarjetas de crédito. Utiliza características como:

- Información demográfica del cliente (sexo, educación, estado civil, etc.).
- Historial de pagos y montos adeudados.
- Comportamiento financiero reciente.

---

## 📊 Uso de la Aplicación

1. **Abrir el formulario de entrada de datos**:
   - Haz clic en el botón "Mostrar Formulario de Datos".
   - Introduce los datos necesarios en los campos proporcionados.
   - Haz clic en "Agregar Datos" para incluirlos en el conjunto actual.

2. **Gestionar los datos**:
   - Visualiza la tabla con los registros ingresados.
   - Elimina filas específicas si es necesario.

3. **Realizar predicciones**:
   - Una vez configurados los datos, presiona "Predecir" para ver los resultados del modelo.

---

## 🌐 Despliegue

La aplicación está desplegada en **Streamlit Cloud**. Puedes probarla directamente desde este enlace:  
[Credit Card Fraud Detection App](https://creditcard-deploy.streamlit.app/)

---

## 🤝 Contribuciones

Si deseas contribuir, abre un *issue* o envía un *pull request*. ¡Toda ayuda es bienvenida!

---

## 📄 Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).  

---

## 👨‍💻 Autor

Desarrollado por [0xfabrica](https://github.com/0xfabrica).  
Si tienes alguna pregunta, no dudes en contactarme.
```

Copia y pega este contenido directamente en el archivo `README.md` de tu repositorio. 🚀
