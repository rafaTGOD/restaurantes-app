# Listinha de lugares

Descrição

Este projeto é uma aplicação interativa, desenvolvida com Streamlit, que permite aos usuários cadastrar, explorar, avaliar e rankear lugares gastronômicos. Os dados são armazenados no Supabase para garantir um backend robusto e confiável.

Funcionalidades Principais

📌 Cadastro de Locais

Insira informações como nome, tipo, endereço, imagens e Instagram.

Conecte os dados ao banco de dados Supabase.


🌟 Avaliar Locais

Avalie locais cadastrados com notas de 0 a 5.

Escreva um review para personalizar sua avaliação.

Organize os lugares em listas personalizadas.


🌎 Explorar Locais

Utilize filtros por tipo, listas ou ordenação (nota média, tipo ou data).

Veja estatísticas globais sobre os locais cadastrados.

Exiba avaliações associadas a cada lugar.


🏆 Ranking por Tipo

Veja os lugares mais bem avaliados por tipo (Restaurante, Bar, Cafeteria).

Ordene por média das notas e exiba detalhes das avaliações.

Tecnologias Utilizadas
Frontend: Streamlit

Backend: Supabase (PostgreSQL)

Bibliotecas Python:

streamlit

supabase

folium (mapas interativos)

python-dateutil

statistics


Instalação e Execução
Clone o repositório:

bash
git clone https://github.com/seu-usuario/minha-lista-gastronomica.git
cd minha-lista-gastronomica
Instale as dependências:

bash
pip install -r requirements.txt
Conecte ao Supabase:

Certifique-se de que o arquivo supabase_utils.py está configurado com suas credenciais:

python
SUPABASE_URL = "https://seu-projeto.supabase.co"
SUPABASE_KEY = "sua-chave-publica"
Execute o aplicativo:

bash
streamlit run app.py
Em seguida, navegue para as demais páginas, como 2_Avaliar.py, 3_Ranking.py e 2_Explorar.py.

Estrutura do Projeto
text
/minha-lista-gastronomica/
├── 1_Cadastrar.py       # Página de cadastro de locais
├── 2_Avaliar.py         # Página de avaliações
├── 2_Explorar.py        # Página de exploração de locais
├── 3_Ranking.py         # Página de ranking por tipo
├── supabase_utils.py    # Utilitários para conexão ao Supabase
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do projeto
Como Fazer o Deploy
Configure o GitHub:

Crie um repositório no GitHub e faça o upload dos arquivos do projeto.

Use o Streamlit Community Cloud:

Acesse Streamlit Community Cloud.

Conecte seu repositório ao Streamlit.

Configure variáveis de ambiente para suas credenciais do Supabase (se necessário).

Clique em Deploy e obtenha o link público da sua aplicação.

Contribuição
Contribuições são bem-vindas! Para relatar problemas ou sugerir melhorias, abra uma Issue no repositório.

Licença
Este projeto está licenciado sob a MIT License.

Este README fornece uma visão completa do seu projeto, incluindo estrutura, funcionalidades e instruções de uso. 😊
