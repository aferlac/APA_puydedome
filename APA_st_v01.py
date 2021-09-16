#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import json
from pandas import json_normalize
import unicodedata


# In[2]:


# Liens de téléchargement des données
# data2019 et data2020 : allocataires APA puy de dome de 2019 et 2020
data2019_url = (
    "https://app.puy-de-dome.fr/open-data/public/files/app-open-data/Allocataires_APA_par_commune_(spatial_points)_1460_2020-09-03.csv")

data2020_url = (
    "https://app.puy-de-dome.fr/open-data/public/files/app-open-data/Allocataires_APA_par_commune_(spatial_points)_1492_2021-03-18.csv")

# datageo : coordonnées des communes du puy de dome
datageo_url = (
    'https://github.com/gregoiredavid/france-geojson/raw/master/departements/63-puy-de-dome/communes-63-puy-de-dome.geojson')
geo=pd.read_json(datageo_url)

df2020 = pd.read_csv(data2020_url, sep=';', encoding = "ISO-8859-1")

df2019 = pd.read_csv(data2019_url, sep=';', encoding = "ISO-8859-1")


# In[3]:


# Notebook de nettoyage des données

col_suppr = ['DATE_DEBUT', 'DATE_FIN', 'ID_HISTORIQUE']
STR = ['CODE_COMMUNE', 'CODE_CANTON']
NBRE = ['TOTAL', 'TOTAL_FEM', 'TOTAL_HOM', 'TOTAL_M75A', 'TOTAL_7584A', 'TOTAL_P85A', 'TOTAL_DOM', 'TOTAL_ETA']

def nettoie(A):
    A.columns = A.loc[0]
    A.drop(0,axis=0,inplace=True)
    A.drop(col_suppr, axis=1, inplace=True)
    A.fillna(0, inplace=True)
    A[STR] = A[STR].astype('str')
    A[NBRE] = A[NBRE].astype('int')
    return A

nettoie(df2020)
nettoie(df2019)

def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

dfgeo = json_normalize(geo['features'])
dfgeo.drop('type', axis=1, inplace=True)
dfgeo.drop('geometry.type', axis=1, inplace=True)
dfgeo=dfgeo.rename(columns={"geometry.coordinates": "coordinates",
                      "properties.code": "CODE_COMMUNE",
                      "properties.nom": "LIBL_COMMUNE"})
dfgeo['LIBL_COMMUNE']=dfgeo['LIBL_COMMUNE'].str.upper()
long,lat=[],[]
for commune in range(len(dfgeo)):
    A,B, nbcom=0,0,len(dfgeo['coordinates'][commune][0])
    for point in range(nbcom):
        A+= (dfgeo['coordinates'][commune][0][point][0] if commune!=244 else dfgeo['coordinates'][commune][0][0][point][0])
        B+= (dfgeo['coordinates'][commune][0][point][1] if commune!=244 else dfgeo['coordinates'][commune][0][0][point][1])
    long.append(A/nbcom)
    lat.append(B/nbcom)

dfgeo['LONG']=long
dfgeo['LAT']=lat

for commune in range(len(dfgeo['LIBL_COMMUNE'])):
    dfgeo['LIBL_COMMUNE'][commune] = remove_accents(dfgeo['LIBL_COMMUNE'][commune])


# In[ ]:





# In[5]:


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
folium.Marker(location=[dfgeo['LAT'][dfgeo['LIBL_COMMUNE']==commune], dfgeo['LONG'][dfgeo['LIBL_COMMUNE']==commune]],
             popup= commune).add_to(map)
folium_static(map) # Affichage de la carte dans Streamlit


# In[ ]:




