from flask import render_template, request, jsonify, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
from skimage import io
from skimage.transform import resize
import jinja2
import cv2
import jwt
import datetime, random, os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from pymongo import MongoClient


bp = Blueprint('post', __name__, url_prefix='/post')

model = tf.keras.models.load_model('static/emotionModel.h5')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

label = {'0': 'angry',
         '1': 'happy',
         '2': 'notbad',
         '3': 'sad'}

jelly_url = None

@bp.route('/')
def post_page():
    return render_template('post.html')

@bp.route('/change', methods=['POST'])
def change_pic_to_emoji():
    global jelly_url

    face_img = request.files['face_img']

    path = save_img(face_img, './static/img/log/')

    result = classify_emotion(detection_face(path))
    emotion = label[result]

    jelly_url = f'../static/img/jellyticon/{emotion}{random.randrange(1, 5)}.png'

    return jsonify({'url': jelly_url})




@bp.route('/upload', methods=['POST'])
def upload():

    desc_receive = request.form['desc_give']
    face_img_receive = request.form['face_img_give']

    doc = {
        'desc_receive': 'desc_receive',
        'face_img_receive': 'face_img_receive'
    }
    db.users.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})







    desc = request.form['desc']
    try:
        additional_img = request.files['additional_img']
        path = '.' + save_img(additional_img, './static/img/post/')
    except:
        path = ''

    time = datetime.datetime.utcnow()

    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        doc = {
            'email': payload['email'],
            'desc': desc,
            'emoji': jelly_url,
            'img': path,
            'date': time
        }

        db.posts.insert_one(doc)

        return jsonify({'msg': 'msg'})

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login", msg="다시 로그인해주세요."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login", msg="로그인 정보가 존재하지 않습니다."))


def save_img(img, default_path):
    timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    path = default_path + timestamp + secure_filename(img.filename)
    img.save(path)
    return path


def detection_face(img_path):
    ori_img = cv2.imread(img_path)
    ori_img = cv2.resize(ori_img, dsize=(0, 0), fx=0.4, fy=0.4, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(ori_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, minSize=(200, 200))
    widths = []
    for face in faces:
        widths.append(face[2])

    max_index = widths.index(max(widths))
    max_face = faces[max_index]
    img_y1 = max_face[1]
    img_y2 = max_face[1] + max_face[3]
    img_x1 = max_face[0]
    img_x2 = max_face[0] + max_face[2]
    face_img = ori_img[img_y1:img_y2, img_x1:img_x2]
    cv2.imwrite(img_path, face_img)

    return img_path


def classify_emotion(img_path):
    img = io.imread(img_path)
    img = resize(img, (224, 224))

    img = np.asarray(img)

    image = img.reshape((-1, 224, 224, 3))
    y_pred = model.predict(image)
    result = np.argmax(y_pred)

    return str(result)