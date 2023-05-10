import os
import pandas as pd
import sqlite3

class DbManager:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS news_portal_posts(author TEXT,title TEXT, subheader TEXT, caption TEXT, body TEXT, date DATE,category TEXT, image TEXT)')

    def add_post(self,author, title, subheader, caption, body, date, category,image):
        self.c.execute(f'INSERT INTO news_portal_posts(author,title,subheader,caption,body,date,category,image) VALUES (?,?,?,?,?,?,?,?)',(author, title, subheader, caption, body, date, category,image))
        self.conn.commit()
    
    def view_all_posts(self):
        self.c.execute('SELECT * FROM news_portal_posts')
        posts = self.c.fetchall()
        return posts

    def search_post_by_title(self,term):
        self.c.execute(f"SELECT * FROM news_portal_posts WHERE title LIKE '%{term}%'")
        result = self.c.fetchall()
        return result
    
    def search_post_by_body(self,term):
        self.c.execute(f"SELECT * FROM news_portal_posts WHERE body LIKE '%{term}%'")
        result = self.c.fetchall()
        return result

DATA_FOLDER = os.path.join(os.getcwd(),'data')
if not os.path.exists(DATA_FOLDER):
    os.mkdir(DATA_FOLDER)
