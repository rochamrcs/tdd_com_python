FROM python:3.14-slim

RUN python -m venv /venv  
ENV PATH="/venv/bin:$PATH"  

COPY requirements_prod.txt .
RUN pip install -r requirements_prod.txt

COPY src /src

WORKDIR /src

RUN python manage.py migrate --noinput

CMD ["gunicorn", "--bind", ":8888", "superlists.wsgi:application"]