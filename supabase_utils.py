import os
from supabase import create_client, Client
from datetime import datetime

# Configurar Supabase
SUPABASE_URL = "https://dmkuwhmzgsemcsdyloay.supabase.co"  # Substitua pelo URL do projeto
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRta3V3aG16Z3NlbWNzZHlsb2F5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE2NTY3MTksImV4cCI6MjA1NzIzMjcxOX0.3uv1Yid7qruQ07qkn8BA_pHyVtB6rPPqplTVGH0ru1o"  # Substitua pela chave pública

def connect_supabase():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

# Função para carregar lugares do Supabase
def load_lugares(client):
    response = client.table("lugares").select("*").execute()
    lugares = response.data

    for lugar in lugares:
        avaliacoes_response = client.table("avaliacoes").select("*").eq("id_lugar", lugar["id"]).execute()
        lugar["avaliacoes"] = avaliacoes_response.data or []

    return lugares

# Função para carregar avaliações de lugares
def load_avaliacoes(client: Client):
    response = client.table("avaliacoes").select("*").execute()
    return response.data

# Função para adicionar um novo lugar
def add_lugar(client: Client, dados):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dados["data"] = now
    response = client.table("lugares").insert(dados).execute()
    return response.data

# Função para adicionar ou atualizar avaliação
def add_or_update_avaliacao(client: Client, id_lugar, usuario, nota, review):
    response = client.table("avaliacoes").select("*").eq("id_lugar", id_lugar).eq("usuario", usuario).execute()
    if response.data:  # Se já existe avaliação para este lugar e usuário
        update_resp = client.table("avaliacoes").update({
            "nota": nota,
            "review": review
        }).eq("id_lugar", id_lugar).eq("usuario", usuario).execute()
        return update_resp.data
    else:  # Caso contrário, insere nova avaliação
        insert_resp = client.table("avaliacoes").insert({
            "id_lugar": id_lugar,
            "usuario": usuario,
            "nota": nota,
            "review": review
        }).execute()
        return insert_resp.data
