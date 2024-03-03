FROM python:3.11-slim
ENV DASH_DEBUG_MODE True

WORKDIR /

COPY . .

RUN set -ex && \
    pip install -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "-b", ":80", "application:application"]

