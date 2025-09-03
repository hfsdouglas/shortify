# shorti.fy

Shortify é uma aplicação simples e eficiente para encurtar links, tornando URLs longas em versões curtas e fáceis de compartilhar. Ideal para quem deseja praticidade e organização no dia a dia digital. 🚀🔗

## Para fazer a instalação das dependências
Crie um ambiente virtual isolado para as dependências do projeto.
~~~shell
python -m venv venv
~~~

Ative o ambiente virtual.
~~~shell
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
~~~

Instale as dependências do requirements.txt
~~~shell
pip install -r requirements.txt
~~~

Confira se está funcionando!
~~~shell
python -m flask --version
~~~

>Certifique-se de estar dentro da **hierarquia de pastas** do projeto.

## Para inicializar as configurações de banco de dados
~~~shell
flask --app app init-db
~~~

Após inicializar as configurações do banco de dados já é possível de rodar a aplicação. 

## Para rodar a aplicação em ambiente de desenvolvimento
~~~shell
flask --app app run
~~~
