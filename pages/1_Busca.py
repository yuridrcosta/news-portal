import streamlit as st
from posts_manager.manager import DbManager

def main():
    st.title('IC:red[News]')
    st.divider()
    searchterm = st.text_input('Digite o termo a ser buscado')
    option = st.radio("Campo em que o termo está presente",("Título",'Corpo'))
    if st.button('Buscar'):
        dbmanager = DbManager()
        dbmanager.create_table()
        if option == 'Título':
            search = dbmanager.search_post_by_title(searchterm)
        else:
            search = dbmanager.search_post_by_body(searchterm)
        if search:
            st.write(f"{len(search)} artigos encontrados")
            for post in search:
                st.divider()
                st.title(post[1])
                st.subheader(post[2])
                if post[7]:
                    st.image(post[7],use_column_width=True)
                st.caption(post[3])
                st.caption(f'Autor: {post[0]}')
                st.caption(f'Data: {post[5]}')
                st.caption(f'Categoria: {post[6]}')
                st.markdown(post[4])
                st.divider()


if __name__=='__main__':
    main()