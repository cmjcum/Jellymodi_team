from flask import render_template, Blueprint, url_for, request, jsonify
from werkzeug.utils import redirect
from bson.objectid import ObjectId
import datetime

from pymongo import MongoClient




bp = Blueprint('detail', __name__, url_prefix='/detail')


@bp.route('/<post_id>')
def show_detail(post_id):
    post_info = db.posts.find_one({'_id': ObjectId(post_id)})
    post_info['_id'] = str(post_info['_id'])
    post_info['date'] = post_info['date'].strftime("%Y %m %d %a").upper()
    return render_template('detail.html', post_info=post_info)


@bp.route('/delete/<post_id>')
def delete_post(post_id):
    db.posts.delete_one({'_id': ObjectId(post_id)})
    return redirect(url_for('home'))

@bp.route('/update', methods=['POST'])
def edit_post():
    post_id = request.form['post_id']
    desc = request.form['desc']
    db.posts.update_one({'_id': ObjectId(post_id)}, {'$set': {'desc': desc}})
    return jsonify({'msg': 'success'})