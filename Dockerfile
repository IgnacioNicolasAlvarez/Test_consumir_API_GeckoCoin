FROM python:3.9

ENV PYTHONUNBUFFERED=0

WORKDIR /test_data_dev_per
RUN apt install g++ gcc libxslt-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["bash"]