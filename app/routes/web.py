def web(app): 
    @app.route('/')
    def home():
        return "Welcome to the Web Route"

    @app.route('/<short_id>')
    def redirect_short_url(short_id):
        # Procura pela URL longa no banco de dados utilizando o short_id

        return {
            "short_id": short_id,
            "url": 'http://example.com/long-url',
        }