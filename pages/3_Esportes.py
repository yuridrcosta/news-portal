import streamlit as st
from posts_manager.manager import DbManager

def main():
    st.title('Esportes')
    dbmanager = DbManager()
    dbmanager.create_table()
    posts = dbmanager.view_all_posts()
    
    for post in posts:
        if post[6]=='Esportes':
            st.divider()
            st.title(post[1])
            st.subheader(post[2])
            st.caption(post[3])
            st.caption(f'Autor: {post[0]}')
            st.caption(f'Data: {post[5]}')
            st.markdown(post[4])
            st.divider()

if __name__=='__main__':
    main()