import streamlit as st
import pandas as pd

# Tornar o display dos dados largos
st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Book", books)

df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

books_title = df_book["book title"][0]
books_genre = df_book["genre"][0]
books_price = df_book["book price"][0]
books_rating = df_book["rating"][0]
books_year = df_book["year of publication"][0]

st.title(books_title)
st.subheader(books_genre)

col1, col2, col3 = st.columns(3)
col1.metric("Price", books_price)
col2.metric("Rating", books_rating)
col3.metric("Year", books_year)

st.divider()

# Criar lista de comentarios

# for row in df_reviews_f.values:
#     st.write(row[2])
#     st.write(row[5])