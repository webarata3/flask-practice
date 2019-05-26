from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# /user/test_taro
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


# /post/123
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


# /path/aaa/bbb
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login'
    else:
        return 'show_login_page'


if __name__ == '__main__':
    app.run()
