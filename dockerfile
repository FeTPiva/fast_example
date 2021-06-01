FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 80

COPY ./credit_score /credit_score
COPY ./requirements.txt /credit_score/

RUN pip install -r /credit_score/requirements.txt

CMD ["uvicorn", "credit_score.main:app", "--host", "0.0.0.0", "--port", "8000"]
