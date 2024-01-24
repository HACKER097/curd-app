# Curd app

## Bugs encountered

### No valid response

```python
TypeError: The view function did not return a valid response. The return type must be a string, dict, list, tuple with headers or status, Response instance, or WSGI callable, but it was a int.
```

This error occurs when your function does not return any valid response. After creating the api endpoints for features that do not have a response to return, I returned just the response code by `return 200` which caused an error.

To fix this, I just replaced the return statement `return "OK"`, response codes can be added by doing `return "OK", 200`

Resources used: [1](https://stackoverflow.com/questions/73183394/view-function-did-not-return-a-valid-response-the-return-type-must-be-a-string)

## Null values

While trying to fetch the names and numbers from the request, I kept getting null values instead of the data in the request. 

This was caused by using the post request method to fetch the values for a get request. I had to replace `request.form.get("name")` with `request.args.get("name")` which fixed the issue

Resources used: [1](https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request) [2](https://www.geeksforgeeks.org/get-the-data-received-in-a-flask-request/)


## References

1. [Flask – (Creating first simple application)](https://www.geeksforgeeks.org/flask-creating-first-simple-application/)
2. [ How to Use CURL to Send API Requests ](https://devqa.io/curl-sending-api-requests/)
3. [Contacts app](https://github.com/HACKER097/Contacts-app)
