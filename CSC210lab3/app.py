from flask import Flask, render_template, abort
import json

app = Flask(__name__)

# 加载用户数据
with open('users.json') as f:
    users_dict = json.load(f)


@app.route('/users/<int:uid>')
def user_profile(uid):
    # Since the keys in the JSON are strings, we need to convert the uid to a string for proper matching
    user = users_dict.get(str(uid))
    if not user:
        abort(404)
    return render_template('start.html', user=user, users_dict=users_dict)

@app.errorhandler(404)
def page_not_found(e):
    # Note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True) 