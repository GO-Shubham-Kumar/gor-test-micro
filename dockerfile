FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
ENV PORT=8080
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]