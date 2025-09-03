import json
import string
from flask import request, jsonify
from random import choice

from app.models.link import Link
from app.database.db import db

def api(app):
    @app.route('/api/link')
    def home_api():
        return "Welcome to the API Route" 

    @app.route('/api/link', methods=['POST'])
    def create_short_url():
        data = json.loads(request.get_data().decode('utf-8'))
        link = data.get('link')

        if not link or len(str(link)) == 0:
            return jsonify({"message": "Sem link"}), 400

        # Cria uma URL curta e salva no banco de dados
        texto = ''.join(choice(string.ascii_letters) for _ in range(6))

        new_link = Link(
            link=link,
            short_link=texto
        )

        db.session.add(new_link)
        db.session.commit()

        return jsonify({"message": "Link criado com sucesso!", "short_link": "http://localhost:5000/" + texto }), 200