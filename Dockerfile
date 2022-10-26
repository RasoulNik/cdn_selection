FROM python
COPY ./requirements.txt /app/requirements.txt

RUN #pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install  --upgrade -r /app/requirements.txt

ARG CACHEBUST=1
#COPY ./app /app
RUN mkdir -p /app
#CMD ["bash", "-c","python3 /app/main.py"]
CMD ["bash", "-c","python3 /app/endpoint.py"]