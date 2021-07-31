import requests
import tkinter as tk

def getNews():
    api_key = "55caf269dde74b62bcf20e5fa3a929a6"
    url = "http://newsapi.org/v2/top-headlines?country=in&apikey="
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + my_articles[i] + "\n"

        print(my_news)



canvas = tk.Tk()
canvas.geometry("900*600")
canvas.title("News App")

button = tk.Button(canvas, font = 24, text = "Reload", command = getNews)
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify = "left")
label.pack(pady = 20)

getNews()

canvas.mainloop()