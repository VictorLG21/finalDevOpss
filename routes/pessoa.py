from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields
from model.pessoa import db, Pessoa

api = Api()

bp = Blueprint('pessoa', __name__)

api.init_app(bp)
ns = api.namespace('pessoas', description='Operações relacionadas a Pessoas')

pessoa_model = api.model('Pessoa', {
    'id': fields.Integer(readonly=True),
    'nome': fields.String(required=True, description='Nome da pessoa'),
    'idade': fields.Integer(required=True, description='Idade da pessoa'),
})

@ns.route('/')
class PessoaResource(Resource):
    @ns.marshal_list_with(pessoa_model)
    def get(self):
        pessoas = Pessoa.query.all()
        return pessoas

    @ns.expect(pessoa_model)
    @ns.marshal_with(pessoa_model)
    def post(self):
        dados = request.get_json()
        nova_pessoa = Pessoa(**dados)
        db.session.add(nova_pessoa)
        db.session.commit()
        return nova_pessoa, 201

@ns.route('/<int:pessoa_id>')
class PessoaDetailResource(Resource):
    @ns.marshal_with(pessoa_model)
    def get(self, pessoa_id):
        pessoa = Pessoa.query.get(pessoa_id)
        if pessoa:
            return pessoa
        api.abort(404, f"Pessoa {pessoa_id} não encontrada")

    @ns.expect(pessoa_model)
    @ns.marshal_with(pessoa_model)
    def put(self, pessoa_id):
        pessoa = Pessoa.query.get(pessoa_id)
        if pessoa:
            dados = request.get_json()
            pessoa.nome = dados.get('nome', pessoa.nome)
            pessoa.idade = dados.get('idade', pessoa.idade)
            db.session.commit()
            return pessoa
        api.abort(404, f"Pessoa {pessoa_id} não encontrada")

    def delete(self, pessoa_id):
        pessoa = Pessoa.query.get(pessoa_id)
        if pessoa:
            db.session.delete(pessoa)
            db.session.commit()
            return '', 204
        api.abort(404, f"Pessoa {pessoa_id} não encontrada")
