# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
# Add code for get requests to back end
def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key, value in kwargs.items():
            params = params + keys + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print("GET from {} ".format(request_url))
    try:
        # call get method of request library with url and parameters
        response = request.get(request_url)
        return response.json()
    except:
        # if any error occurs
        print("Seem Network exception occured")

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        #call get methodof request library with url and parameters
        response = request.get(request_url)
        return response.json
    except Exception as error:
        print(f"Unexpected {error=}, {type(error)=}")
        print("Network exception occured")

# def post_review(data_dict):
# Add code for posting review
