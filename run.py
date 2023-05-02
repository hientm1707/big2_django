from setup_application import create_app
from gevent.pywsgi import WSGIServer
b2_app = create_app()
http_server = WSGIServer(('', 5002), b2_app)
http_server.serve_forever()