#Cargar librerias
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import joblib as jb

#Crear el main
def main ():
  st.set_page_config(
  page_title="Predicción de deserción de clientes")
  
  st.title("Aplicación de predicción usando Naive Bayes")
  
  with st.container( border=True):
    st.subheader("Modelo Machine Learning para predecir la deserción de clientes")
    st.write("Realizado por Andres David Vesga y Moisés Santiago Colmenares")

  styletexto = "<style>h2 {text-align: center;}</style>"
  st.sidebar.markdown(styletexto, unsafe_allow_html=True)
  st.sidebar.header('Seleccione los datos de entrada')
  
  #Crear la sidebar para seleccionar los datos
  def seleccionar(modeloL):
    
    st.sidebar.subheader('Selector de Modelo')
    modeloS=st.sidebar.selectbox("Modelo",modeloL)

    st.sidebar.subheader('Seleccione la COMP')
    COMPS=st.sidebar.slider("Seleccion", 4000, 18000, 8000, 100)
    
    st.sidebar.subheader('Selector del PROM')
    PROMS=st.sidebar.slider("Seleccion", 0.7, 9.0, 5.0, 0.5)
    
    st.sidebar.subheader('Selector de COMINT')
    COMINTS=st.sidebar.slider("Seleccione", 1500, 58000, 12000, 100)
    
    st.sidebar.subheader('Selector de COMPPRES') 
    COMPPRESS=st.sidebar.slider('Seleccione', 17000, 90000, 25000, 100)
    
    st.sidebar.subheader('Selector de RATE')
    RATES=st.sidebar.slider("Seleccione", 0.5, 4.2, 2.0, 0.1)

    st.sidebar.subheader('Selector de DIASSINQ')
    DIASSINQS=st.sidebar.slider("Seleccione", 270, 1800, 500, 10)
    
    st.sidebar.subheader('Selector de TASARET')
    TASARETS=st.sidebar.slider("Seleccione", 0.3, 1.9, 0.8, .5)
    
    st.sidebar.subheader('Selector de NUMQ')
    NUMQS=st.sidebar.slider("Seleccione", 3.0, 10.0, 4.0, 0.5)
    
    st.sidebar.subheader('Selector de RETRE entre 3 y 30')
    
    RETRES=st.sidebar.number_input("Ingrese el valor de RETRE", value=3.3, placeholder="Digite el numero...")
    
    return modeloS,COMPS, PROMS, COMINTS ,COMPPRESS, RATES, DIASSINQS,TASARETS, NUMQS, RETRES
  
  #Presentar resultados
  with st.container(border=True):
    st.title("Predicción de Churn")
    st.write(""" Pronóstico cortesía del modelo:""")
    st.write(modelo)
    st.write("Se han seleccionado los siguientes parámetros:")

    lista=[[COMP, PROM, COMINT ,COMPPRES, RATE, DIASSINQ,TASARET, NUMQ, RETRE]]
    X_predecir=pd.DataFrame(lista,columns=['COMP', 'PROM', 'COMINT', 'COMPPRES', 'RATE', 'DIASSINQ','TASARET', 'NUMQ', 'RETRE'])
    st.dataframe(X_predecir)
  
  modelo,COMP, PROM, COMINT ,COMPPRES, RATE, DIASSINQ,TASARET, NUMQ, RETRE=seleccionar(modeloA)
  
  #Definir las predicciones
  if modelo=='Naive Bayes':
    y_predict=modeloNB.predict(X_predecir)
    probabilidad=modeloNB.predict_proba(X_predecir)
  
  #Resultado final
  styleprediccion= '<p style="font-family:sans-serif; font-size: 42px;">La predicción es</p>'
  st.markdown(styleprediccion, unsafe_allow_html=True)
  prediccion='Resultado: '+ str(y_predict[0])+ " en conclusion :"+churn[y_predict[0]]
  st.header(prediccion)
    
  col1, col2= st.columns(2)
  col1.metric(label="Probalidad de NO :", value="{0:.2%}".format(probabilidad[0][0]),delta=" ")
  col2.metric(label="Probalidad de SI:", value="{0:.2%}".format(probabilidad[0][1]),delta=" ")

#Cargar modelos
def load_models():
  modeloNB=jb.load('modeloNB.bin')
  return modeloNB

modeloNB = load_models()

modeloA=['Naive Bayes']

churn = {1 : 'Cliente se retirará', 0 : 'Cliente No se Retirará' }

if __name__ == '__main__':
    main()