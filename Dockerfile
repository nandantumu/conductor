FROM python:3.7

WORKDIR /code
COPY Pip* /code/

RUN pip install --upgrade pip &&\
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

COPY . /code

WORKDIR /code
RUN python3 setup.py develop

ENTRYPOINT ["tail", "-f", "/dev/null"]