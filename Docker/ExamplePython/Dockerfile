FROM python:3.8.10

WORKDIR /app

COPY requirements.txt app/requirement.txt

RUN pip install --no-cache-dir --upgrade -r app/requirement.txt

COPY main.py app/main.py

EXPOSE 8001

CMD ["fastapi", "run", "app/main.py", "--port", "8001"]




