import streamlit as st
from supabase_utils import connect_supabase, load_lugares
from statistics import mean
import supabase

st.set_page_config(page_title="Ranking por Tipo", layout="wide")

# Conexão ao Supabase
client = connect_supabase()

# Carregar dados dos lugares do Supabase
lugares = load_lugares(client)

# Função para renderizar estrelas a partir de uma nota
def render_stars(nota):
    full = int(nota)
    half = 1 if nota - full >= 0.5 else 0
    empty = 5 - full - half
    return "⭐" * full + "🌓" * half + "☆" * empty

# Títulos e Tipos
st.title("🏆 Ranking por Tipo")
tipos = ["Restaurante", "Bar", "Cafeteria"]

# Gerar rankings por tipo
for tipo in tipos:
    if tipo == "Bar":
        st.subheader(f"🍹 Bares Melhor Avaliados")
    elif tipo == "Cafeteria":
        st.subheader(f"☕ Cafeterias Melhor Avaliadas")
    else:
        st.subheader(f"🍽️ {tipo}s Melhor Avaliados")
    
    # Filtrar dados pelo tipo
    filtrados = [lugar for lugar in lugares if lugar["tipo"] == tipo and lugar.get("avaliacoes")]
    if not filtrados:
        st.info(f"Nenhum {tipo.lower()} avaliado ainda.")
        continue

    # Ordenar pela média das avaliações
    filtrados.sort(key=lambda lugar: mean([avaliacao["nota"] for avaliacao in lugar["avaliacoes"]]) if lugar.get("avaliacoes") else 0, reverse=True)

    # Exibir rankings
    for i, lugar in enumerate(filtrados, 1):
        media = mean([avaliacao["nota"] for avaliacao in lugar["avaliacoes"]])
        st.markdown(f"### {i}. **{lugar['nome']}** — {render_stars(media)} ({media:.2f}/5)")
        st.markdown(f"🏷️ Lista: `{lugar['lista']}`")

        # Mostrar avaliações individuais em um expander
        with st.expander("Ver avaliações individuais"):
            for avaliacao in lugar["avaliacoes"]:
                st.markdown(f"**{avaliacao['usuario']}**: ⭐ {avaliacao['nota']} — _{avaliacao['review']}_")
