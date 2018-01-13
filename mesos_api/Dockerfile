FROM alpine
MAINTAINER Christian Adell "chadell@gmail.com"
RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api.py"]