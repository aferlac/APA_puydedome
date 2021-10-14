#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import numpy as np
import folium
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_folium import folium_static


# Liens de téléchargement des données
# data2019 et data2020 : allocataires APA puy de dome de 2019 et 2020
dfgeocommune=pd.read_csv('./commune_geo.csv')
for i in range(len(dfgeocommune)):
    dfgeocommune['geo'][i]=eval(dfgeocommune['geo'][i])

dfgeodepartement=pd.read_csv('./departement_geo.csv')
dfgeodepartement['geo'][0]=eval(dfgeodepartement['geo'][0])

df2020 = pd.read_csv('./APA_2020.csv')

df2019 = pd.read_csv('./APA_2019.csv')

df2018 = pd.read_csv('./APA_2018.csv')

df2017 = pd.read_csv('./APA_2017.csv')

df2016 = pd.read_csv('./APA_2016.csv')

df2015 = pd.read_csv('./APA_2015.csv')

df2014 = pd.read_csv('./APA_2014.csv')

dfAPA63 = pd.concat([df2020, df2019, df2018, df2017, df2016, df2015, df2014])


# Titre de la page Streamlit
st.set_page_config(page_title=' APA - Puy de Dôme ', page_icon=None, layout='wide', initial_sidebar_state='auto')
st.title('Allocataires APA dans le Puy de Dôme')

st.header('**Répartition des allocataires en 2020**')
col1, col2, col3 = st.columns([1.5,1,2.5])
commune = col1.selectbox(label='Choisissez une commune', options=df2020['LIBL_COMMUNE'].sort_values().unique())
indice_commune=dfgeocommune.index[dfgeocommune['CODE_COMMUNE']==df2020[df2020['LIBL_COMMUNE']==commune]['CODE_COMMUNE'].tolist()[0]].tolist()[0]
# Affichage du nombre d'allocataires pour la commune 
if commune == 'CLERMONT-FERRAND':
    col2.metric("Nombre d'allocataires dans la commune",
            str(df2020['TOTAL'][df2020['LIBL_COMMUNE']==commune].sum()),
            str(df2020['TOTAL'][df2020['LIBL_COMMUNE']==commune].sum() -
                df2019['TOTAL'][df2019['LIBL_COMMUNE']==commune].sum()))
else :
    col2.metric("Nombre d'allocataires dans la commune",
            str(df2020['TOTAL'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if 
                str(df2020['TOTAL'][df2020['LIBL_COMMUNE']==commune].tolist()[0])!= '0' else "*",
            str(df2020['TOTAL'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))
    
# Affichage du nombre d'allocataires par sexe pour la commune 
col1, col2, col3, col4 = st.columns([1,1,1,3])
col1.subheader("Par sexe")
if commune == 'CLERMONT-FERRAND':
    col1.metric("Hommes",
            str(df2020['TOTAL_HOM'][df2020['LIBL_COMMUNE']==commune].sum()),
            str(df2020['TOTAL_HOM'][df2020['LIBL_COMMUNE']==commune].sum() -
                df2019['TOTAL_HOM'][df2019['LIBL_COMMUNE']==commune].sum()))
    col1.metric("Femmes",
            str(df2020['TOTAL_FEM'][df2020['LIBL_COMMUNE']==commune].sum()),
            str(df2020['TOTAL_FEM'][df2020['LIBL_COMMUNE']==commune].sum() -
                df2019['TOTAL_FEM'][df2019['LIBL_COMMUNE']==commune].sum()))  
else :
    col1.metric("Hommes",
            str(df2020['TOTAL_HOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if 
                str(df2020['TOTAL_HOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_HOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_HOM'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))
    col1.metric("Femmes",
            str(df2020['TOTAL_FEM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if 
                str(df2020['TOTAL_FEM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_FEM'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_FEM'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))

col2.subheader("Par age")
if commune == 'CLERMONT-FERRAND':
    col2.metric("Moins de 75 ans",
            str(df2020['TOTAL_M75A'][df2020['LIBL_COMMUNE']==commune].sum()),
            str(df2020['TOTAL_M75A'][df2020['LIBL_COMMUNE']==commune].sum() -
                df2019['TOTAL_M75A'][df2019['LIBL_COMMUNE']==commune].sum()))
    col2.metric("De 75 à 84 ans",
            str(df2020['TOTAL_7584A'][df2020['LIBL_COMMUNE']==commune].sum()),
            str(df2020['TOTAL_7584A'][df2020['LIBL_COMMUNE']==commune].sum() -
                df2019['TOTAL_7584A'][df2019['LIBL_COMMUNE']==commune].sum()))
    col2.metric("Plus de 84 ans",
            str(df2020['TOTAL_P85A'][df2020['LIBL_COMMUNE']==commune].sum()),
            str(df2020['TOTAL_P85A'][df2020['LIBL_COMMUNE']==commune].sum() -
                df2019['TOTAL_P85A'][df2019['LIBL_COMMUNE']==commune].sum()))
else :
    col2.metric("Moins de 75 ans",
            str(df2020['TOTAL_M75A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if 
                str(df2020['TOTAL_M75A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_M75A'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_M75A'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))
    col2.metric("De 75 à 84 ans",
            str(df2020['TOTAL_7584A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if 
                str(df2020['TOTAL_7584A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_7584A'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_7584A'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))
    col2.metric("Plus de 84 ans",
            str(df2020['TOTAL_P85A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if 
                str(df2020['TOTAL_P85A'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_P85A'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_P85A'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))
    
col3.subheader("Par type d'habitation")
if commune == 'CLERMONT-FERRAND':
    col3.metric("A domicile",
            str(df2020['TOTAL_DOM'][df2020['LIBL_COMMUNE']==commune].sum()),
            str(df2020['TOTAL_DOM'][df2020['LIBL_COMMUNE']==commune].sum() -
                df2019['TOTAL_DOM'][df2019['LIBL_COMMUNE']==commune].sum()))
    col3.metric("En établissement",
            str(df2020['TOTAL_ETA'][df2020['LIBL_COMMUNE']==commune].sum()),
            str(df2020['TOTAL_ETA'][df2020['LIBL_COMMUNE']==commune].sum() -
                df2019['TOTAL_ETA'][df2019['LIBL_COMMUNE']==commune].sum()))
else :
    col3.metric("A domicile",
            str(df2020['TOTAL_DOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if 
                str(df2020['TOTAL_DOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_DOM'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_DOM'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))
    col3.metric("En établissement",
            str(df2020['TOTAL_ETA'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) if 
                str(df2020['TOTAL_ETA'][df2020['LIBL_COMMUNE']==commune].tolist()[0]) !='0' else "*",
            str(df2020['TOTAL_ETA'][df2020['LIBL_COMMUNE']==commune].tolist()[0] -
                df2019['TOTAL_ETA'][df2019['LIBL_COMMUNE']==commune].tolist()[0]))


# création de la carte OpenStreetMap du puy de dome indiquant la position de la commune sélectionnée
with col4:
    map = folium.Map([45.77, 3.15], zoom_start=9) # carte centrée sur la commune
    folium.vector_layers.Polygon(locations=dfgeocommune['geo'][indice_commune],
                                 fill_color='blue',
                                 popup = 'commune de ' + commune + ' canton de ' + df2020[df2020['LIBL_COMMUNE']==commune]['NOM_CANTON'].values[0]).add_to(map) # tracé du contour et de la surface de la commune
    
    folium.vector_layers.Polygon(locations=dfgeodepartement['geo'][0],
                                 fill_color=None).add_to(map) # tracé du contour du département

    folium_static(map) # Affichage de la carte dans Streamlit

st.text("Les variations sous les indices correspondent à l'évolution entre 2019 et 2020")
st.text("* : Donnée non disponible, valeur entre 0 et 5 ")
st.write('---')



st.header("**Evolution du nombre d'allocataires depuis 2014 à **"+commune)

année = [2014, 2015, 2016, 2017, 2018, 2019, 2020]
total, fem, hom, m75, p75, p84, dom, eta = [], [], [], [], [], [], [], []
code_commune = int(df2020[df2020['LIBL_COMMUNE']==commune]['CODE_COMMUNE'][0:1].values)

if code_commune==63255:
    st.write('Cette commune est issue de la fusion de Nonette et Orsonnette en 2016')
    for a in année[0:2]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                     int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63266)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63266)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63266)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63266)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63266)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63266)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63266)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63266)].values.sum()))
    for a in année[2:]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))

elif code_commune==63244:
    st.write('Cette commune est issue de la fusion de La Moutade et Cellule en 2016')
    for a in année[0:2]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                     int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63068)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63068)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63068)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63068)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63068)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63068)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63068)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63068)].values.sum()))
    for a in année[2:]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))

elif code_commune==63160:
    st.write('Cette commune est issue de la fusion de Flat et Aulhat Saint Privat en 2016')
    for a in année[0:2]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                     int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63018)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63018)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63018)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63018)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63018)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63018)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63018)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63018)].values.sum()))
    for a in année[2:]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))

elif code_commune==63226:
    st.write('Cette commune est issue de la fusion de Mezel et Dallet en 2019')
    for a in année[0:5]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                     int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63133)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63133)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63133)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63133)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63133)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63133)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63133)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63133)].values.sum()))
    for a in année[5:]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))

elif code_commune==63335:
    st.write('Cette commune est issue de la fusion de Saint Diery et Creste en 2019')
    for a in année[0:5]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                     int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63127)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63127)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63127)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63127)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63127)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63127)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63127)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63127)].values.sum()))
    for a in année[5:]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))

elif code_commune==63448:
    st.write('Cette commune est issue de la fusion de Vernet La Varenne et Chaméane en 2019')
    for a in année[0:5]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                     int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63078)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63078)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63078)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63078)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63078)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63078)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63078)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()) +
                   int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==63078)].values.sum()))
    for a in année[5:]:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        
else:
    for a in année:
        total.append(int(dfAPA63['TOTAL'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        fem.append(int(dfAPA63['TOTAL_FEM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        hom.append(int(dfAPA63['TOTAL_HOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        m75.append(int(dfAPA63['TOTAL_M75A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p75.append(int(dfAPA63['TOTAL_7584A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        p84.append(int(dfAPA63['TOTAL_P85A'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        dom.append(int(dfAPA63['TOTAL_DOM'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
        eta.append(int(dfAPA63['TOTAL_ETA'][(dfAPA63['ANNEE_REF']==a) & (dfAPA63['CODE_COMMUNE']==code_commune)].values.sum()))
    

col1, col2, col3, col4, col5 = st.columns([.1,.9,.1,.9,.1])
col2.subheader("Nombre total d'allocataires")
col2.write(' ')
fig, ax = plt.subplots()
plt.bar(x=année, height= total, color = 'steelblue')
plt.xlabel("")
plt.ylabel("")
col2.pyplot(fig)

choix = col4.radio(label='', options=['Par sexe', 'Par age','Par habitation'])

if choix == 'Par sexe':
    fig, ax = plt.subplots()
    plt.bar(x=année, height=fem, label='femmes')
    plt.bar(x=année, height=hom, bottom = fem, label='hommes')
    plt.legend(loc='lower left')
    if max(np.array(fem) + np.array(hom))<=10:
        plt.ylim(top=10.5)
    col4.pyplot(fig)
    
elif choix == 'Par age':
    fig, ax = plt.subplots()
    plt.bar(x=année, height=m75, label='Moins de 75 ans')
    plt.bar(x=année, height=p75, bottom=m75, label='De 75 à 84 ans')
    plt.bar(x=année, height=p84, bottom = np.array(m75) + np.array(p75), label='Plus de 84 ans')
    plt.legend(loc='lower left')
    if max(np.array(m75) + np.array(p75)+np.array(p84))<=10:
        plt.ylim(top=10.5)
    col4.pyplot(fig)
    
else :
    fig, ax = plt.subplots()
    plt.bar(x=année, height=dom, label='A domicile')
    plt.bar(x=année, height=eta, bottom = dom, label='En établissement')
    plt.legend(loc='lower left')
    if max(np.array(dom) + np.array(eta))<=10:
        plt.ylim(top=10.5)
    col4.pyplot(fig)
    col4.write("Les données ne sont comptabilisées qu'à partir de 2017")
