import unittest
from flask import Blueprint, request, jsonify, current_app
from flask.testing import FlaskClient
from model.pessoa import db, Pessoa, init_app

pessoa_bp = Blueprint('pessoa_bp', __name__)

@pessoa_bp.route('/pessoas', methods=['GET'])
def listar_pessoas():
    pessoas = Pessoa.query.all()
    return jsonify([pessoa.__dict__ for pessoa in pessoas])

@pessoa_bp.route('/pessoas/<int:pessoa_id>', methods=['GET'])
def obter_pessoa(pessoa_id):
    pessoa = Pessoa.query.get(pessoa_id)
    if pessoa:
        json_data = pessoa.to_dict()

        return jsonify(json_data),200
    return jsonify({'message': 'Pessoa não encontrada'}), 404

@pessoa_bp.route('/pessoas', methods=['POST'])
def criar_pessoa():
    dados = request.get_json()
    nova_pessoa = Pessoa(**dados)
    json_data = nova_pessoa.to_dict()
    db.session.add(nova_pessoa)
    db.session.commit()
    return jsonify(json_data), 201

@pessoa_bp.route('/pessoas/<int:pessoa_id>', methods=['PUT'])
def atualizar_pessoa(pessoa_id):
    pessoa = Pessoa.query.get(pessoa_id)
    if pessoa:
        dados = request.get_json()
        pessoa.nome = dados.get('nome', pessoa.nome)
        pessoa.idade = dados.get('idade', pessoa.idade)
        db.session.commit()
        json_data = pessoa.to_dict()
        return jsonify(json_data)
    return jsonify({'message': 'Pessoa não encontrada'}), 404

@pessoa_bp.route('/pessoas/<int:pessoa_id>', methods=['DELETE'])
def excluir_pessoa(pessoa_id):
    pessoa = Pessoa.query.get(pessoa_id)
    if pessoa:
        db.session.delete(pessoa)
        db.session.commit()
        return jsonify({'message': 'Pessoa excluída com sucesso'}),204
    return jsonify({'message': 'Pessoa não encontrada'}), 404