import streamlit as st
from pymongo import MongoClient

st.title("App Streamlit com MongoDB")

# Conexão com o MongoDB
try:
    client = MongoClient('mongodb://mongo:27017/')
    db = client['meu_banco']
    collection = db['minha_colecao']
    st.success("Conectado ao MongoDB com sucesso!")
except Exception as e:
    st.error(f"Erro ao conectar ao MongoDB: {e}")

# Inserção de dados
if st.button("Inserir dado exemplo"):
    collection.insert_one({"nome": "Kauan", "idade": 25})
    st.success("Dado inserido no banco!")

# Atualização de dados
if st.button("Atualizar idade para 26"):
    result = collection.update_one({"nome": "Kauan"}, {"$set": {"idade": 26}})
    if result.modified_count > 0:
        st.success("Idade atualizada!")
    else:
        st.warning("Nenhum dado atualizado (verifique se 'Kauan' existe).")

# Leitura e exibição dos dados
st.subheader("Dados no MongoDB:")
dados = list(collection.find())
if dados:
    for doc in dados:
        nome = doc.get("nome", "")
        idade = doc.get("idade", "")
        nome_completo = nome + " Silva"  # Concatenação simples
        st.write(f"Nome completo: {nome_completo}, Idade: {idade}")
else:
    st.info("Nenhum dado encontrado no banco.")


