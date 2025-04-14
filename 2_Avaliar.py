import streamlit as st
from supabase_utils import connect_supabase, load_lugares, add_or_update_avaliacao
from statistics import mean

st.set_page_config(page_title="Avaliar Locais", layout="wide")

# Conectar ao Supabase
client = connect_supabase()

# Carregar dados do Supabase
lugares = load_lugares(client)
usuario = st.session_state.get("usuario", "Rafael")  # Usuário global
st.title(f"🌟 Avaliar Locais ({usuario})")

# Filtrar lugares que ainda não foram avaliados pelo usuário
not_yet_rated = [lugar for lugar in lugares if not any(avaliacao["usuario"] == usuario for avaliacao in lugar.get("avaliacoes", []))]

if not not_yet_rated:
    st.info("Todos os lugares já foram avaliados por você. 🎉")
else:
    for lugar in not_yet_rated:
        with st.expander(f"{lugar['nome']} ({lugar['tipo']})", expanded=False):
            st.markdown(f"📍 **Endereço**: {lugar['endereco']}")
            st.markdown(f"📅 **Cadastrado em**: {lugar['data']}")
            if lugar.get("instagram"):
                st.markdown(f"[Instagram]({lugar['instagram']})")
            if lugar.get("imagem"):
                st.image(lugar["imagem"], use_container_width=True)

            # Exibição para avaliação
            st.markdown("### ✨ Sua Avaliação")
            nota = st.slider(f"Sua nota (0 a 5):", 0.0, 5.0, 0.0, 0.5, key=f"nota_{lugar['id']}")
            review = st.text_area("Seu comentário:", key=f"review_{lugar['id']}", height=100)

            # Botão para salvar a avaliação
            if st.button("Salvar avaliação", key=f"salvar_{lugar['id']}"):
                add_or_update_avaliacao(client, lugar["id"], usuario, nota, review)
                st.success(f"Avaliação para '{lugar['nome']}' salva com sucesso!")
                st.session_state["trigger_rerun"] = True

