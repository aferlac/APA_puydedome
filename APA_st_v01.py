#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static


# In[55]:


# Liens de téléchargement des données
# data2019 et data2020 : allocataires APA puy de dome de 2019 et 2020
dfgeo=pd.read_csv('./APA_geo.csv')
for i in range(len(dfgeo)):
    dfgeo['geo'][i]=eval(dfgeo['geo'][i])

df2020 = pd.read_csv('./APA_2020.csv')

df2019 = pd.read_csv('./APA_2019.csv')


# In[57]:


# Titre de la page Streamlit
st.set_page_config(page_title=' APA - Puy de Dôme ', page_icon=None, layout='wide', initial_sidebar_state='auto')
st.title(' Répartition des allocataires APA du Puy de Dôme ')

# Bouton de choix d'une commune dans la barre latérale
st.sidebar.header("Choisissez une commune")
commune = st.sidebar.selectbox(label='',options=df2020['LIBL_COMMUNE'].sort_values())

# Affichage du nombre d'allocataires pour la commune 
col1, col2, col3, col4 = st.columns(4)
col1.header('Année 2020')
col2.metric("Nombre d'allocataires",
            str(df2020['TOTAL'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if str(df2020['TOTAL'][df2020['LIBL_COMMUNE']==commune].tolist()[0])!= '0' else "*",
            str(df2020['TOTAL'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))

# Affichage du nombre d'allocataires par sexe pour la commune 
col1, col2, col3, col4 = st.columns(4)
col1.subheader("Par sexe")
col2.metric("Hommes",
            str(df2020['TOTAL_HOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if str(df2020['TOTAL_HOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_HOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_HOM'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))
col3.metric("Femmes",
            str(df2020['TOTAL_FEM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if str(df2020['TOTAL_FEM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_FEM'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_FEM'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))

# Affichage du nombre d'allocataires par age pour la commune 
col1, col2, col3, col4 = st.columns(4)
col1.subheader("Par age")
col2.metric("Moins de 75 ans",
            str(df2020['TOTAL_M75A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if str(df2020['TOTAL_M75A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_M75A'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_M75A'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))
col3.metric("De 75 à 84 ans",
            str(df2020['TOTAL_7584A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if str(df2020['TOTAL_7584A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_7584A'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_7584A'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))
col4.metric("Plus de 84 ans",
            str(df2020['TOTAL_P85A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if str(df2020['TOTAL_P85A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_P85A'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_P85A'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))

# Affichage du nombre d'allocataires par type d'habitation pour la commune 
col1, col2, col3, col4 = st.columns(4)
col1.subheader("Par type d'habitation")
col2.metric("A domicile",
            str(df2020['TOTAL_DOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if str(df2020['TOTAL_DOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_DOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_DOM'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))
col3.metric("En établissement",
            str(df2020['TOTAL_ETA'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if str(df2020['TOTAL_ETA'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_ETA'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_ETA'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))

st.text("Les variations sous les indices correspondent à l'évolution entre 2019 et 2020")
st.text("* : Donnée non disponible, valeur entre 0 et 5 ")

# création de la carte OpenStreetMap du puy de dome indiquant la position de la commune sélectionnée
map = folium.Map([45.77, 3.15], zoom_start=9)
folium.vector_layers.Polygon(locations=dfgeo[(dfgeo['LIBL_COMMUNE']==commune)]['geo'],
                             fill_color='blue',
                             popup=commune).add_to(map)

folium_static(map) # Affichage de la carte dans Streamlit


# In[ ]:




