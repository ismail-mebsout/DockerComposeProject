FROM python:3.7-slim-buster

RUN mkdir /frontend_dir
WORKDIR /frontend_dir
ADD . /frontend_dir
RUN pip install virtualenv
RUN virtualenv front_vir_env
RUN . front_vir_env/bin/activate
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]