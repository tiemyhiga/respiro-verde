import streamlit as st
import streamlit.components.v1 as components

with  open ("./styles-calculadora.css") as f: 
    st.markdown( f"<style> {f.read()} </style>" , unsafe_allow_html= True ) 

st.button("Clique aqui" , key="green_button")

st.title("Descubra quais as melhores plantas para seu jardim!")

st.write("Para te ajudar a escolher as plantas mais adequadas para seu jardim, preciso de algumas informações sobre o local onde você planeja plantar. Por favor, responda às seguintes perguntas:")

with st.form(key='form_plantas'):
    nome = st.text_input("Como gostaria de ser chamado(a)?", placeholder="Digite seu nome aqui")
    telefone = st.number_input("Qual é o seu telefone?", value=None, placeholder="Digite seu telefone aqui")
    email = st.text_input("Qual é o seu email?", placeholder="Digite seu email aqui")
    horas_sol = st.number_input("Quantas horas de sol seu jardim recebe por dia?", value=None, min_value=1, max_value=24)
    tamanho_jardim = st.number_input("Qual é o tamanho de seu jardim em metros quadrados?", value=None, min_value=10, max_value=10000)
    btn_form = st.form_submit_button(label='Enviar')

    if btn_form:
        if not nome or not telefone or not email or horas_sol == 0 or tamanho_jardim == 0:
            st.error("Por favor, preencha todos os campos corretamente.")
        else:
            st.success (f"Obrigada, {nome}! Suas informações foram recebidas com sucesso. Agora, vamos descobrir quais plantas são as melhores para seu jardim!")
            if horas_sol > 6 and tamanho_jardim >= 100:
                st.write ("Para seu jardim com mais de 6 horas de sol por dia, algumas plantas que você pode considerar são plantas frutíferas e alguns vegetais como:")
                st.markdown (" • Limão")
                st.markdown (" • Acerola")
                st.markdown (" • Graviola")
                st.markdown (" • Romã")
                st.markdown (" • Tomate")
                st.markdown (" • Quiabo")
                st.markdown (" • Maxixe")
                st.write ("Vale lembrar que todos esses vegetais podem ser cultivados em vasos, precisando apenas tomar cuidado com a profundidade do mesmo")
            elif horas_sol <= 6 and tamanho_jardim >= 100:
                st.write ("Para seu jardim com pelo menos 6 horas de sol por dia, algumas plantas que você pode considerar são plantas frutíferas e alguns vegetais como:")
                st.markdown (" • Jabuticaba")
                st.markdown (" • Acerola")
                st.markdown (" • Tomate")
                st.markdown (" • Cenoura")
                st.markdown (" • Couve-flor")
                st.write ("Vale lembrar que todos esses vegetais podem ser cultivados em vasos, precisando apenas tomar cuidado com a profundidade do mesmo")
            elif horas_sol <= 4 and tamanho_jardim >= 100:
                st.write ("Para seu jardim com pelo menos 4 horas de sol por dia, algumas plantas que você pode considerar são plantas frutíferas e alguns vegetais, como:")
                st.markdown (" • Morango")
                st.markdown (" • Amora")
                st.markdown (" • Tomate")
                st.markdown (" • Aspargo")
                st.write ("Vale lembrar que todos esses vegetais podem ser cultivados em vasos, precisando apenas tomar cuidado com a profundidade do mesmo")
            elif horas_sol > 6 and tamanho_jardim < 100:
                st.write ("Para seu jardim com mais de 6 horas de sol por dia, algumas plantas que você pode considerar são:")
                st.markdown (" • Cebolinha")
                st.markdown (" • Coentro")
                st.markdown (" • Acelga")
                st.markdown (" • Agrião")
            elif horas_sol <= 6 and tamanho_jardim < 100:
                st.write ("Para seu jardim com menos de 6 horas de sol por dia, algumas plantas que você pode considerar são:")
                st.markdown (" • Cenoura")
                st.markdown (" • Alho")
                st.markdown (" • Aspargos")
            elif horas_sol <= 4 and tamanho_jardim < 100:
                st.write ("Para seu jardim com pelo menos 4 horas de sol por dia, algumas plantas que você pode considerar são:")
                st.markdown (" • Salsa")
                st.markdown (" • Couve-flor")
                st.markdown (" • Alface")
                st.markdown (" • Rúcula")
            else:
                st.write("Desculpe, mas não conseguimos encontrar plantas adequadas para seu jardim com base nas informações fornecidas. Por favor, tente novamente com outras informações, obrigada!.")


