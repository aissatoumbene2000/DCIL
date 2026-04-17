import streamlit as st

st.title("INTERFACE GRAPHIQUE")

st.header("section title")

st.subheader("section hub")

st.write ("La géomatique est étroitement liée à l’information géographique qui est la représentation d’un objet ou d’un phénomène localisé dans l’espace. Ainsi, la géomatique regroupe l’ensemble des outils et méthodes permettant de représenter, d’analyser et d’intégrer des données géographiques.")

st.markdown(
"""
La géomatique est étroitement liée à l’information géographique qui est la représentation d’un objet ou d’un phénomène localisé dans l’espace.
Ainsi, la géomatique regroupe l’ensemble des outils et méthodes permettant de représenter, d’analyser et d’intégrer des données géographiques.
"""


)

st.image("Diomaye.jpeg", width = 150)



st.button ("envoyer")

st.number_input("saisir un nombre")

st.text_input("saisir votre nom")

st.time_input("time")

st.date_input("date")


st.radio("Genre", ["G" , "F"])

st.selectbox ("Modules python", ["streamlit","panda","flask"])

st.multiselect ("Genre", ["G" , "F" ,"i" ,"h"])

st.text_area("commentaire")







