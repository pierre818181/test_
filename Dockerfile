FROM runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "handler.py"]
