def api(app): 
    @app.route('/api/url')
    def home_api():
        return "Welcome to the API Route" 

    @app.route('/api/url', methods=['POST'])
    def create_short_url():
        # Cria uma URL curta e salva no banco de dados

        return {
            short_url: 'http://shortly/abc123',
        }