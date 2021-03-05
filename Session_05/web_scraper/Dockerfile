FROM python:alpine
COPY ./requirements.txt ./script.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python script.py
WORKDIR /
CMD ["ash"]