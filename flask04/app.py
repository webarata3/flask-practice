from flask import Flask, render_template, make_response, url_for, redirect, abort
app = Flask(__name__)


@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('username', 'the username')
    return resp


@app.route('/redirect')
def redirect1():
    return redirect(url_for('redirect_test'))


@app.route('/redirect_test')
def redirect_test():
    return 'リダイレクトしました'


@app.route('/error_test')
def error_test():
    abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return '404エラーですよ'


if __name__ == '__main__':
    app.run()
