import os

from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename

from models import db, Image  # 假设你已经在模型文件中定义了Image和db

# 创建蓝图
image_bp = Blueprint('image', __name__)

# 设置允许上传的文件类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# 检查文件扩展名
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 图片上传接口
@image_bp.route('/upload_image', methods=['POST'])
def upload_image():
    # 获取请求中的文件
    file = request.files.get('file')
    folder_path = request.form.get('folder', '')  # 从请求中获取文件夹路径，默认为空

    if not file:
        return jsonify({"error": "No file provided"}), 400

    # 检查文件扩展名是否合法
    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400

    # 安全地获取文件名
    filename = secure_filename(file.filename)

    # 获取上传文件夹的绝对路径
    static_folder = current_app.config['UPLOAD_FOLDER']  # 假设配置中已设置UPLOAD_FOLDER
    if folder_path:
        # 如果文件夹路径传递了，就使用它
        save_path = os.path.join(static_folder, folder_path)
    else:
        # 如果没有传递路径，就保存到默认目录
        save_path = static_folder

    # 确保文件夹存在，如果没有则创建
    os.makedirs(save_path, exist_ok=True)

    # 保存文件
    file.save(os.path.join(save_path, filename))

    # 保存图片信息到数据库

    image_path = os.path.join(folder_path, filename) if folder_path else filename

    # 创建 Image 实例
    image = Image(filename=filename, path=image_path)
    db.session.add(image)
    db.session.commit()

    relative_static_folder = current_app.config['UPLOAD_RELATIVE_FOLDER']  # 假设配置中已设置UPLOAD_FOLDER

    image_path = os.path.join(relative_static_folder, image_path)
    # 返回成功响应
    return jsonify({
        "message": "success",
        "file_path": image_path,
        "image_id": image.id
    }), 200
