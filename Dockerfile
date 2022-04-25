FROM python:3
FROM gorialis/discord.py

RUN mdir -p /usr/src/esie-bot
WORKDIR /usr/src/esie-bot

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]