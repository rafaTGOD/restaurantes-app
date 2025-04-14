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
.selector-label {
    font-size:18px !important;
    color: #264653;
    font-weight: bold;
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
    
    # Botões para navegação entre as páginas
    if st.button("📌 Cadastrar Novo Lugar"):
        st.st.query_params(page="1_Cadastrar")
    if st.button("🔍 Explorar Lugares Cadastrados"):
        st.st.query_params(page="2_Explorar")
    if st.button("🌟 Avaliar Locais"):
        st.st.query_params(page="2_Avaliar")
    if st.button("🏆 Ver Ranking por Tipo"):
        st.experimental_set_query_params(page="3_Ranking")



