import requests
import os
import logging

logger = logging.getLogger(__name__)
class SendGridClient:
    def __init__(self, _method, _from, _to, _subject, _content):
        self._url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"
        self._method = _method
        self._from = _from
        self._to = _to
        self._subject = _subject
        self._content = _content

    def _get_payload(self):
        return {
            "personalizations": [
                {
                    "to": [{"email": self._to}],
                    "subject": self._subject
                }
            ],
            "from": {"email": self._from},
            "content": [
                {
                    "type": "text/plain",
                    "value": self._content
                }
            ]
        }

    def _get_headers(self):
        return {
            "Content-type": "application/json",
            "X-RapidAPI-Key": os.environ['X_RapidAPI_Key'],
            "X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
        }



    def send(self):
        logger.log(level=1, msg="SENDING EMAIL")
        return requests.request(self._method, self._url, json=self._get_payload(), headers=self._get_headers())
