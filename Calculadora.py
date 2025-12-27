import streamlit as st

st.title("Descubra quais as melhores plantas para seu jardim!")

st.write("Para te ajudar a escolher as plantas mais adequadas para seu jardim, preciso de algumas informações sobre o local onde você planeja plantar. Por favor, responda às seguintes perguntas:")

with st.form(key='form_plantas'):
    nome = st.text_input("Qual é o seu nome?", placeholder="Digite seu nome aqui")
    telefone = st.number_input("Qual é o seu telefone?", placeholder="Digite seu telefone aqui")
    email = st.text_input("Qual é o seu email?", placeholder="Digite seu email aqui")
    horas_sol = st.number_input("Quantas horas de sol seu jardim recebe por dia?", min_value=1, max_value=24)
    tamanho_jardim = st.number_input("Qual é o tamanho de seu jardim em metros quadrados?", min_value=10, max_value=10000)
    btn_form = st.form_submit_button(label='Enviar')

    if btn_form:
        if not nome or not telefone or not email or horas_sol == 0 or tamanho_jardim == 0:
            st.error("Por favor, preencha todos os campos corretamente.")
        else:
            st.success(f"Obrigado, {nome}! Suas informações foram recebidas com sucesso. Agora, vamos descobrir quais plantas são as melhores para seu jardim!")
            if horas_sol > 6 and tamanho_jardim >= 100:
                st.write("Para seu jardim com mais de 6 horas de sol por dia, algumas plantas que você pode considerar são: plantas frutíferas como limão, acerola, graviola, romã você pode considerar alguns vegetais como tomate, quiabo, maxixe entre outros, vale lembrar que todos esses vegetais podem ser cultivados em vasos, precisando apenas tomar cuidado com a profundidade do mesmo")
            elif horas_sol <= 6 and tamanho_jardim >= 100:
                st.write("Para seu jardim com pelo menos 6 horas de sol por dia, algumas plantas que você pode considerar são: plantas frutíferas como jabuticaba, acerola, você pode considerar alguns vegetais como tomate, cenoura e couve flor entre outros, vale lembrar que todos esses vegetais podem ser cultivados em vasos, precisando apenas tomar cuidado com a profundidade do mesmo")
            elif horas_sol <= 4 and tamanho_jardim >= 100:
                st.write("Para seu jardim com pelo menos 4 horas de sol por dia, algumas plantas que você pode considerar são: plantas frutíferas como morango e amora, você pode considerar alguns vegetais como tomate, aspargos, vale lembrar que todos esses vegetais podem ser cultivados em vasos, precisando apenas tomar cuidado com a profundidade do mesmo")

            elif horas_sol > 6 and tamanho_jardim < 100:
                st.write("Para seu jardim com mais de 6 horas de sol por dia, algumas plantas que você pode considerar são: plantas como Cebolinha, coentro, acelga e agrião")
            elif horas_sol <= 6 and tamanho_jardim < 100:
                st.write("Para seu jardim com menos de 6 horas de sol por dia, algumas plantas que você pode considerar são: plantas como cenoura, alho e aspargos")
            elif horas_sol <= 4 and tamanho_jardim < 100:
                st.write("Para seu jardim com pelo menos 4 horas de sol por dia, algumas plantas que você pode considerar são: plantas como salsa, couve flor, alface e rúcula")
            else:
                st.write("Desculpe, mas não conseguimos encontrar plantas adequadas para seu jardim com base nas informações fornecidas. Por favor, tente novamente com outras informações, obrigada!.")
