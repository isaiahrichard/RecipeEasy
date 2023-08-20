from flask import Flask
from routes.users import users

app = Flask(__name__)
app.register_blueprint(users)

if __name__ == "__main__":
    app.run(debug=True)
