FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install pyspark pandas matplotlib seaborn
CMD ["echo", "Project container"]
