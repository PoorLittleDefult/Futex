from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/<password>')
def index(password):
    
    #hashed_value = generate_password_hash(password)

    stored_password = 'pbkdf2:sha256:260000$myqBbrBakeEy5hft$99e24ad5dc617b3e84c1190554709e66c9c65d4c5486378228799d5984752c2b'

    result = check_password_hash(stored_password, password)


    return str(result)


if __name__ == '__main__':
    app.run(debug=True)


