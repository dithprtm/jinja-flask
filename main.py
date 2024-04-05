from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/d28bfcf31f234a1ad09b").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)
print(post_objects)

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog in post_objects:
        if blog.id==index:
            requested_post=blog
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)
