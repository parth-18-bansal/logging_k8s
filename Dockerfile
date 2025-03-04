FROM python:3.12-slim

# set the working directory
WORKDIR /app

# copy the requirements file
COPY requirements.txt ./

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the main files
COPY . .

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]


