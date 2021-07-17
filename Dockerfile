FROM python:3.9

WORKDIR /server
COPY . /server/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD [ "flaskapp.py" ]