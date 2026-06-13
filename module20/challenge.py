
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {
    "book1" : {
           "Title": "Pride and Prejudice",
           "Author": "Jane Austen",
           "Year": "1813",
           "Genre":"Romance"
     },
     "book2" : {
           "Title": "The Lord of the Rings",
           "Author": "J.R.R. Tolkien",
           "Year": "1954",
           "Genre":"Fantasy"
     },
     "book3" : {
           "Title": "Frankenstein",
           "Author": "Mary Shelley",
           "Year": "1818",
           "Genre":"Horror"
     }
}


