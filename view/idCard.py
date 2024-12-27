# built-in package
from flask import jsonify, Blueprint,request
from sqlalchemy import func

from common.projectEnum import IdCardStatusEnum
from models import IdCard, db

id_card_bp = Blueprint('id_card', __name__)


@id_card_bp.route('/random_id_card', methods=['GET'])
def get_id_card():
    # 获取请求中传入的 status 参数（如果有的话）

    # 如果传入了 status 参数，则进行过滤
    id_card = IdCard.query.filter_by(status=IdCardStatusEnum.has_effectiveness.value).order_by(func.random()).first()

    # 返回查询结果的字典表示
    return jsonify(id_card.to_dict())


@id_card_bp.route('/update_id_card/<int:id>', methods=['PUT'])
def update_id_card(id):
    data = request.get_json()
    id_card = IdCard.query.get(id)
    id_card.status = data.get('status', id_card.status)
    db.session.commit()
    # 返回查询结果的字典表示
    return jsonify(id_card.to_dict())

