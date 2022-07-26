from flask import Flask, render_template, request, redirect, url_for
import jinja2
import jwt
import datetime

from api import login, detail, post

# Flask 객체 인스턴스 생성
app = Flask(__name__)

app.register_blueprint(login.bp)
app.register_blueprint(detail.bp)
app.register_blueprint(post.bp)


from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.zjibj.mongodb.net/luster0?retryWrites=true&w=majority')
db = client.dbjellymodi
SECRET_KEY = 'JELLY'

@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        posts = list(db.posts.find({"email": payload['email']}))
        for post in posts:
            print('for')
            post['Y-M'] = post['date'].strftime('%Y%m')
            post['day'] = post['date'].strftime('%d')

        posts.sort(key=lambda x: (-int(x['Y-M']), x['day']))

        temp = {}
        for post in posts:
            try:
                temp[post['date'].strftime('%Y %B')].append(post)

            except:
                temp[post['date'].strftime('%Y %B')] = [post]
        return render_template('index.html', temp=temp)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login", msg="다시 로그인해주세요."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login", msg="로그인 정보가 존재하지 않습니다."))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)