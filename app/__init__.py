from flask import Flask, render_template

# Define the WSGI application object
webapp = Flask(__name__)

# Configurations
webapp.config.from_object('config')


# Sample HTTP error handling
@webapp.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.ecommerce_bookstore.controllers import ecommerce_bookstore

# Register blueprint(s)
webapp.register_blueprint(ecommerce_bookstore)
