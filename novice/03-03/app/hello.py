from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "index page"

@app.route("/hello")
def hello():
    return "hello, world"

@app.route('/user/<user_name>')
def show_user_profile(user_name):
    # show the user profile for that user
    return f'User, {user_name}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post, {post_id}'    

if __name__ == "__main__":
    app.run()    