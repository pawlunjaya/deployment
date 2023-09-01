from flask import Flask
from models import Model

application = Flask(__name__)

@application.route('/')
def index():
    #membuat objek dari kelas Model22
    model = Model()

    #Mengembalikan nilai yang diambil dari model
    return model.getText()
if __name__ == '__main__':
    application.run(debug=True)