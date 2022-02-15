FROM python:3.8.6-slim-buster

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED True

RUN apt-get update -qq \
 && apt-get install -qqy --no-install-recommends \
      gcc \
      python3-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

RUN addgroup --gid 1000 ml \
 && adduser --gecos "" \
      --home /usr/src/app \
      --shell /bin/bash \
      --uid 1000 \
      --gid 1000 \
      --disabled-password \
      ml

COPY ./requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p .local/bin .config .cache \
    mkdir -p /run/user/1000 \
    && chown ml:ml /run/user/1000

USER ml

ENV PATH="/usr/src/app/.local/bin:$PATH"

COPY --chown=ml:ml . .

#RUN chmod +x /usr/src/app/run.sh

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]