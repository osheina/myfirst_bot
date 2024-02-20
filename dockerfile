FROM python:3.10-slim
ENV TOKEN='6700835388:AAHk9w02ibsTQgQ9BA8zOVNUdjqPgMQ4ygM'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python","bot.py" ]