import streamlit as st
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 20)
        self.cell(0, 10, self.title, ln=True, align="C")
        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.5)
        self.line(10, 30, 200, 30)
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 8, body)
        self.ln(6)

def gerar_pdf(nome, email, telefone, resumo, experiencias, formacao, habilidades):
    pdf = PDF()
    pdf.title = nome
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Contato
    pdf.set_font("Arial", "I", 11)
    contato = f"Email: {email} | Telefone: {telefone}"
    pdf.cell(0, 10, contato, ln=True, align="C")
    pdf.ln(10)

    # Resumo
    pdf.chapter_title("Resumo Profissional")
    pdf.chapter_body(resumo if resumo.strip() else "Não informado")

    # Experiências
    pdf.chapter_title("Experiências")
    pdf.chapter_body(experiencias if experiencias.strip() else "Não informado")

    # Formação
    pdf.chapter_title("Formação")
    pdf.chapter_body(formacao if formacao.strip() else "Não informado")

    # Habilidades
    pdf.chapter_title("Habilidades")
    pdf.chapter_body(habilidades if habilidades.strip() else "Não informado")

    return pdf

st.set_page_config(page_title="Gerador de Currículo", layout="centered")
st.title("📝 Gerador de Currículo Automático")

nome = st.text_input("Nome completo")
email = st.text_input("Email")
telefone = st.text_input("Telefone")
resumo = st.text_area("Resumo profissional (resuma quem é você)")
experiencias = st.text_area("Experiências profissionais")
formacao = st.text_area("Formação acadêmica")
habilidades = st.text_area("Habilidades e competências")

if st.button("Gerar Currículo em PDF"):
    if nome and email and telefone:
        pdf = gerar_pdf(nome, email, telefone, resumo, experiencias, formacao, habilidades)
        pdf.output("curriculo.pdf")
        with open("curriculo.pdf", "rb") as f:
            st.download_button("📄 Baixar Currículo", f, file_name="curriculo.pdf")
    else:
        st.warning("Por favor, preencha ao menos nome, email e telefone.")
