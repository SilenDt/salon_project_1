from flask import Flask, render_template

# from controllers.appointments_controller import appointments_blueprint
from controllers.clients_controller import clients_blueprint
from controllers.stylists_controller import stylists_blueprint

app = Flask(__name__)

# app.register_blueprint(appointments_blueprint)
# app.register_blueprint(clients_blueprint)
app.register_blueprint(stylists_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
