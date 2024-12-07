from flask import Blueprint, jsonify, request
from .models import Cementeries
from .schemas import CementeriesSchema
from .extentions import db

main_bp = Blueprint('main', __name__)

# Routes
@main_bp.route('/')
def hello_world():
    return "<p>Hello, World</p>"

@main_bp.route('/cementeries', methods=['GET'])
def list_cementeries():
    all_cementeries = Cementeries.query.all()
    result = CementeriesSchema(many=True).dump(all_cementeries)
    return jsonify(result)

@main_bp.route('/cementeries/<int:id>', methods=['GET'])
def get_cementery(id):
    cementery = Cementeries.query.get(id)
    return CementeriesSchema().jsonify(cementery)

@main_bp.route('/cementeries', methods=['POST'])
def add_cementery():
    data = request.get_json()
    new_cementery = Cementeries(name=data['name'], code=data['code'])
    db.session.add(new_cementery)
    db.session.commit()
    return CementeriesSchema().jsonify(new_cementery)

@main_bp.route('/cementeries/<int:id>', methods=['PUT'])
def update_cementery(id):
    data = request.get_json()
    cementery = Cementeries.query.get(id)
    cementery.name = data['name']
    cementery.code = data['code']
    db.session.commit()
    return CementeriesSchema().jsonify(cementery)

@main_bp.route('/cementeries/<int:id>', methods=['DELETE'])
def delete_cementery(id):
    cementery = Cementeries.query.get(id)
    db.session.delete(cementery)
    db.session.commit()
    return CementeriesSchema().jsonify(cementery)
