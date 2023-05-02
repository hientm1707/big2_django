from flask import jsonify, request, Blueprint

from sendgrid_sdk.models.sendgrid_client import SendGridClient
b2_bookstore = Blueprint('b2_bookstore', __name__, url_prefix='/')

@b2_bookstore.route('/api/email/send', methods=['GET', 'POST'])
def sendEmail():
    json_request = request.get_json()
    client = _get_Send_Grid_client_post(json_request['from'], json_request['to'], json_request['subject'],
                                        json_request['content'])
    response = client.send()
    if response.ok:
        return jsonify({
            "status": "true",
            "message": response.text
        }), response.status_code
    return jsonify({
        "status": "false",
        "message": response.text
    }), response.status_code

def _get_Send_Grid_client_post(_from, _to, _subject, _content):
    return SendGridClient('POST', _from, _to, _subject, _content)
