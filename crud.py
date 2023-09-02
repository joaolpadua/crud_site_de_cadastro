import streamlit as st

#C:\Users\jlpad\AppData\Local\Microsoft\WindowsApps\python.exe -m streamlit run crud.py



# Título
st.title("Meu Portfólio")

# Seção "Sobre Mim"
st.header("Sobre Mim")
st.write("Sou um desenvolvedor Python apaixonado por programação e tecnologia. "
         "Tenho experiência em desenvolvimento web e estou sempre em busca de aprender coisas novas.")

# Seção "Formação"
st.header("Formação")
st.write("Bacharel em Ciência da Computação - Universidade ABC (2015-2019)")

# Seção "Redes Sociais"
st.header("Redes Sociais")

# Link para o LinkedIn
st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/seu-perfil)")

# Link para o GitHub
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Profile-green?style=flat-square&logo=github)](https://github.com/seu-usuario)")

# Link para o Twitter
st.markdown("[![Twitter](https://img.shields.io/badge/Twitter-Profile-lightblue?style=flat-square&logo=twitter)](https://twitter.com/seu-usuario)")

# Seção de Contato
st.header("Contato")
st.write("E-mail: seu-email@example.com")

# Rodapé
st.write("© 2023 Seu Nome")
