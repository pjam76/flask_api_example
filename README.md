# Introduction
This is a very simple example of an Flask based API on top of a python application. For this toy example I have a
written a simple XKCD style password generator and wrapped it in a flask API with a Swagger UI interface. The Flask API
can then be wrapped in a WSGI, NGINX docker ready for production.

For the list of words I have used `/usr/share/dict/words` found on most Linux systems. 

# Testing
To test the application locally, then run `app/main.py` and access the url: http://127.0.0.1:5000

# Docker container
Run the following command to build the Docker image

```python
docker build -t pw_api:0.1 .
```

Initialize a instance of the image 

```python
docker run -d -p 80:80 pw_api:0.1
```

Access the container in a browser on port 80: http://127.0.0.1/
