FROM python:3.14-slim

RUN python -m venv /venv  
ENV PATH="/venv/bin:$PATH"  

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src /src

WORKDIR /src

RUN python manage.py migrate --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]