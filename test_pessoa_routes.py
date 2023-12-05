import unittest
from flask import json
from model.pessoa import db as test_db, Pessoa, init_app
from app import create_app

class PessoaRoutesTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            test_db.session.remove()

    def test_criar_pessoa(self):
        payload = {'nome': 'João', 'idade': 25}
        response = self.client.post('/pessoas/', json=payload)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['nome'], 'João')
        self.assertEqual(data['idade'], 25)

    def test_obter_pessoa(self):
        pessoa = Pessoa(nome='Maria', idade=30)
        with self.app.app_context():
            test_db.session.add(pessoa)
            test_db.session.commit()

            response = self.client.get(f'/pessoas/{pessoa.id}')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data['nome'], 'Maria')
            self.assertEqual(data['idade'], 30)

    def test_atualizar_pessoa(self):
        pessoa = Pessoa(nome='Carlos', idade=40)
        with self.app.app_context():
            test_db.session.add(pessoa)
            test_db.session.commit()

            payload = {'nome': 'Carlos Atualizado', 'idade': 41}
            response = self.client.put(f'/pessoas/{pessoa.id}', json=payload)
            self.assertEqual(response.status_code, 200)

            updated_pessoa = Pessoa.query.get(pessoa.id)
            self.assertEqual(updated_pessoa.nome, 'Carlos Atualizado')
            self.assertEqual(updated_pessoa.idade, 41)
    
if __name__ == '__main__':
    unittest.main()
