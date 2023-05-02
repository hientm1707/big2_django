from flask import Flask, render_template
from flask_redis import FlaskRedis
# Define the WSGI application object
app = Flask(__name__)

#Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.ecommerce_bookstore.controllers import first_mod as first_mod

redis_client = FlaskRedis(app)
# Register blueprint(s)
app.register_blueprint(first_mod)

if __name__ == '__main__':
    app.run(port=5050)