from flask import Blueprint, render_template, jsonify, request
import jwt
import datetime
import hashlib

bp = Blueprint('login', __name__, url_prefix='/jelly')

from pymongo import MongoClient




@bp.route('/signup')
def signup():
    return render_template('signup.html')


@bp.route('/login')
def login():
    msg = request.args.get('msg')
    return render_template('login.html', msg=msg)


@bp.route('/api/signup', methods=['POST'])
def api_signup():
    email_receive = request.form['email_give']
    pw_receive = request.form['pw_give']

    is_exist_email = bool(db.users.find_one({'email': email_receive}))

    if is_exist_email:
        return jsonify({'msg': '중복! 다른 이메일을 입력해주세요.'})
    else:
        pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

        db.users.insert_one({'email': email_receive, 'pw': pw_hash})

        return jsonify({'result': 'success'})


@bp.route('/api/login', methods=['POST'])
def api_login():
    email_receive = request.form['email_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    result = db.users.find_one({'email': email_receive, 'pw': pw_hash})

    if result is not None:
        payload = {
            'email': email_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=500)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@bp.route('/api/user', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        return jsonify({'result': 'success'})

    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '다시 로그인해주세요.'})

    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})