import streamlit as st
import fitz  # PyMuPDF para ler PDF
import openai
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configura o título e layout da página
st.set_page_config(page_title="Resumidor de PDF", layout="centered")
st.title("📄 Resumidor de PDF com IA")
st.write("Faça upload de um PDF e receba um resumo automático com inteligência artificial.")

# Upload do arquivo PDF
uploaded_file = st.file_uploader("Selecione um arquivo PDF", type="pdf")

# Função para extrair texto do PDF usando PyMuPDF
def extract_text_from_pdf(pdf_file):
    with
