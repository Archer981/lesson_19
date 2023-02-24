# Напишите декоратор `auth_required` который проверяет 
# наличие в запросе заголовка 
# Authorization (содержание заголовка может быть любым)
from flask import Flask, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False


def auth_required(func):
    def wrapper():
        if 'Authorization' not in request.headers:
            return '', 401
        else:
            return func()
    return wrapper
    # TODO Напишите Ваш код здесь


                  
@app.route("/")            # Для самопроверки запустите приложение 
@auth_required             # и попробуйте отправить GET-запросы
def get_page():            # C заголовком Authorization и без
   return {}

if __name__=="__main__":
    app.run()
