import streamlit as st
from PIL import Image

st.set_page_config(page_title="Listinha de lugares", layout="wide")

# Estilo visual
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

# Seletor de usuário
st.markdown('<p class="selector-label">Selecione o usuário:</p>', unsafe_allow_html=True)
usuario = st.radio(label="", options=["Rafinha", "Maju"], index=0, horizontal=True)
st.session_state["usuario"] = usuario

# Conteúdo visual
col1, col2 = st.columns(2)
with col1:
    st.image("https://images.unsplash.com/photo-1600891964599-f61ba0e24092", use_container_width=True)

with col2:
    st.write("### O que você deseja fazer hoje?")
    st.write("👉 Use o menu lateral esquerdo para navegar entre as páginas do app.")
    st.write("- **Cadastrar:** Adicione um novo lugar")
    st.write("- **Avaliar:** Dê notas e comentários")
    st.write("- **Explorar:** Veja todos os lugares")
    st.write("- **Ranking:** Veja os melhores por categoria")
