FROM python:3.10.8-alpine3.16

WORKDIR /app/

COPY requirements.txt /app/requirements.txt

#Setup requirements
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run"]