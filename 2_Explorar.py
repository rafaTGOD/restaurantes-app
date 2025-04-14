import streamlit as st
from supabase_utils import connect_supabase, load_lugares
from statistics import mean
from dateutil import parser

st.set_page_config(page_title="Explorar Lugares", layout="wide")

# Conectar ao Supabase e carregar lugares
client = connect_supabase()
lugares = load_lugares(client)

# Usuário global
usuario = st.session_state.get("usuario", "Rafael")
st.title(f"🌎 Explorar Lugares Cadastrados ({usuario})")

# Filtros
st.sidebar.header("🔎 Filtros")
filter_type = st.sidebar.selectbox("Filtrar por tipo:", ["Todos", "Bar", "Restaurante", "Cafeteria"])
filter_lista = st.sidebar.text_input("Filtrar por nome da lista:")
sort_by = st.sidebar.selectbox("Ordenar por:", ["Nota média", "Tipo", "Data"])

# Estatísticas globais
st.sidebar.header("📊 Estatísticas Globais")
total_places = len(lugares)
total_evaluated = sum(1 for lugar in lugares if lugar.get("avaliacoes"))
avg_rating = (
    mean(
        [
            mean([avaliacao["nota"] for avaliacao in lugar["avaliacoes"]])
            for lugar in lugares if lugar.get("avaliacoes")
        ]
    )
    if total_evaluated > 0
    else 0
)
st.sidebar.markdown(f"- **Total de lugares:** {total_places}")
st.sidebar.markdown(f"- **Já avaliados:** {total_evaluated} ({(total_evaluated / total_places * 100):.2f}%)")
st.sidebar.markdown(f"- **Média geral de avaliações:** ⭐ {avg_rating:.2f}/5")

# Aplicar filtros
filtered = [lugar for lugar in lugares if (filter_type == "Todos" or lugar["tipo"] == filter_type)]
if filter_lista:
    filtered = [lugar for lugar in filtered if filter_lista.lower() in lugar["lista"].lower()]

# Ordenar
if sort_by == "Nota média":
    filtered.sort(
        key=lambda lugar: mean([avaliacao["nota"] for avaliacao in lugar["avaliacoes"]]) if lugar.get("avaliacoes") else 0,
        reverse=True,
    )
elif sort_by == "Tipo":
    filtered.sort(key=lambda lugar: lugar["tipo"])
elif sort_by == "Data":
    filtered.sort(key=lambda lugar: parser.parse(lugar["data"]), reverse=True)

# Exibição dos lugares
st.markdown("## 🌟 Lugares Cadastrados")
for lugar in filtered:
    with st.expander(f"{lugar['nome']} ({lugar['tipo']})"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**Endereço:** {lugar['endereco']}")
            st.markdown(
                f"📍 [Abrir no Google Maps](https://www.google.com/maps/search/{lugar['endereco'].replace(' ', '+')})"
            )
            if lugar.get("instagram"):
                st.markdown(f"📸 [Instagram]({lugar['instagram']})")
            st.markdown(f"🏷️ Lista: `{lugar['lista']}`")
            st.markdown(f"📅 Cadastrado em: {lugar['data']}")

            # Verificar se há avaliações
            if lugar.get("avaliacoes"):
                st.markdown("### 🧾 Avaliações:")
                for avaliacao in lugar["avaliacoes"]:
                    st.markdown(
                    f"**{avaliacao['usuario']}**: ⭐ {avaliacao['nota']} — _{avaliacao['review']}_"
                               )
                media = mean([avaliacao["nota"] for avaliacao in lugar["avaliacoes"]])
                st.markdown(f"**Média geral**: ⭐ {media:.2f}/5")
            else:
                st.markdown("### 🧾 Este lugar ainda não foi avaliado.")

        with col2:
            if lugar.get("imagem"):
                st.image(lugar["imagem"], use_container_width=True)
