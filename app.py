from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://cdn.shopify.com/s/files/1/1416/6788/products/chicken_hayday_plush_02_1200x630.jpg?v=1516833567"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
