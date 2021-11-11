FROM python:3.7-slim-buster

RUN mkdir /ds_api
WORKDIR /ds_api
ADD . /ds_api
RUN pip install virtualenv
RUN virtualenv api_vir_env
RUN . api_vir_env/bin/activate
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]

CMD ["app.py"]