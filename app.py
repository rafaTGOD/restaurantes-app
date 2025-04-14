
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Listinha de lugares", layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:48px !important;
    font-weight: bold;
}
.subtitle {
    font-size:24px !important;
    color: #6c757d;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">🍽️ Listinha de lugares (Word 2.0)</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Criando listas e fazendo reviews pq somos profissionais 🤓👆</p>', unsafe_allow_html=True)

# Seletor de usuário global estilizado
st.markdown('<p class="selector-label">Selecione o usuário:</p>', unsafe_allow_html=True)
usuario = st.radio(label="", options=["Rafinha", "Maju"], index=0, horizontal=True)
st.session_state["usuario"] = usuario


col1, col2 = st.columns(2)
with col1:
    st.image("https://images.unsplash.com/photo-1600891964599-f61ba0e24092", use_container_width=True)
with col2:
    st.write("### O que você deseja fazer hoje?")
    st.page_link("pages/1_Cadastrar.py", label="📌 Cadastrar Novo Lugar", icon="📝")
    st.page_link("pages/2_Explorar.py", label="🔍 Explorar Lugares Cadastrados", icon="🌎")
    st.page_link("pages/2_Avaliar.py", label="🌟 Avaliar Locais", icon="📋")
    st.page_link("pages/3_Ranking.py", label="🏆 Ver Ranking por Tipo", icon="📊")


