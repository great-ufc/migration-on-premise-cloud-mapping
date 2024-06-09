FROM python:3.11-slim AS runner

COPY ./backend /backend

WORKDIR /backend

RUN pip3 install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
