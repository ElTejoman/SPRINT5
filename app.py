import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV en un DataFrame
#car_data = pd.read_csv('C:/Users/User/Desktop/Learning_Python/Learning_Python/Sprint 5/SPRINT5/vehicles_us.csv')

#Utilizaré ruta relativa porque Streamlit si lee la direccion completa de la base de datos, pero Render al parecer no.
car_data = pd.read_csv('vehicles_us.csv')


# Encabezado de la aplicación
st.header('Panel de Control de Anuncios de Venta de Coches')

# Casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # Si la casilla de verificación está seleccionada
    # Mensaje
    st.write('Construyendo un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Construir el histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el histograma
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter: # Si la casilla de verificación está seleccionada
    # Mensaje
    st.write('Construyendo un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Construir el gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
