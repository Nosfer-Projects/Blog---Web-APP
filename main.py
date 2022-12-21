from flask import Flask, render_template
from post import Post
import requests

#Connect to API to get all posts
API = "https://api.npoint.io/d6281a1edce99b4598cf"
respone = requests.get(API).json()
all_posts= []
for post in respone:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_posts.append(post_object)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = all_posts)

@app.route("/post/<int:index>")
def display_post(index):
    post = None
    for blog_post in all_posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)
