import streamlit as st
from posts_manager.manager import DbManager
def main():
    st.title('IC:red[News]')
    st.divider()

    st.title('Admin')

    st.subheader("Adicionar artigo")

    author = st.text_input("Digite o nome do autor", max_chars=50)
    title = st.text_input("Digite o título do artigo",max_chars=60)
    subheader = st.text_input("Digite o subcabeçalho do artigo")
    caption = st.text_input("Digite uma legenda para o artigo")
    body = st.text_area("Digite o corpo do artigo")
    date = st.date_input('Data de publicação')
    imagem_upload = st.text_input("Link para uma imagem a ser associada")

    option = st.selectbox(
    'Categoria do artigo',
    ('Geral', 'Esportes', 'Economia'))

    if st.button("Publicar"):
        dbmanager = DbManager()
        dbmanager.create_table()
        dbmanager.add_post(author=author,title=title,subheader=subheader,caption=caption,body=body,date=date,category=option,image=imagem_upload)
        st.success(f"Postagem {title} salva")

if __name__=='__main__':
    main()