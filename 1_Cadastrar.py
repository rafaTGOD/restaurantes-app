import streamlit as st
import os
from datetime import datetime
from supabase_utils import connect_supabase, add_lugar
import supabase

st.set_page_config(page_title="Cadastrar Lugar", layout="wide")

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

st.title("📌 Cadastrar Novo Lugar")

client = connect_supabase()  # Conectar ao Supabase

# Formulário para cadastro
with st.form(key="place_form"):
    col1, col2 = st.columns([2, 1])
    with col1:
        name = st.text_input("Nome do estabelecimento:")
    with col2:
        place_type = st.selectbox("Tipo:", ["", "Bar", "Restaurante", "Cafeteria"])
    
    col3, col4 = st.columns([2, 1])
    with col3:
        address = st.text_input("Endereço completo:")
    with col4:
        instagram = st.text_input("Instagram (link):")
    
    image = st.file_uploader("Foto do local (opcional):", type=["jpg", "jpeg", "png"])
    submit = st.form_submit_button("Salvar")

if submit:
    image_path = ""
    if image:
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{image.name}"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        with open(filepath, "wb") as f:
            f.write(image.getbuffer())
        image_path = filepath

    # Dados do novo lugar
    new_place = {
        "nome": name,
        "tipo": place_type,
        "endereco": address,
        "instagram": instagram,
        "imagem": image_path,
        "lista": "",
        "visitado": False,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    # Inserir dados no banco via Supabase
    novo_id = add_lugar(client, new_place)
    st.success(f"Lugar '{name}' cadastrado com sucesso!")
