FROM python:3.9

ENV PYTHONUNBUFFERED=0

WORKDIR /exam-ignacio-alvarez
RUN apt install g++ gcc libxslt-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["bash", "init_app.sh"]