# Curd app

## Bugs encountered

### Empty response

While creating the `/getRecord` endpoint, I had added some print statements to see if everything is working correctly. One of them was

```python
print(cur.fetchall())
```

because `cur.fetchall()` method returns the output of the query, when I called it again for responding to the request, it gave an empty array `[]` as the output because there was no query made.

This was easily fixed by removing the print statement. In the future, if the project is large enough, it would be better to use a logging library to avoid these bugs.


### No valid response

```python
TypeError: The view function did not return a valid response. The return type must be a string, dict, list, tuple with headers or status, Response instance, or WSGI callable, but it was a int.
```

This error occurs when your function does not return any valid response. After creating the api endpoints for features that do not have a response to return, I returned just the response code by `return 200` which caused an error.

To fix this, I just replaced the return statement 

```python
return "OK"
```
response codes can be added by doing

```python
return "OK", 200
```

**Resources used**: [1](https://stackoverflow.com/questions/73183394/view-function-did-not-return-a-valid-response-the-return-type-must-be-a-string)

## Null values

While trying to fetch the names and numbers from the request, I kept getting null values instead of the data in the request. 

This was caused by using the post request method to fetch the values for a get request. I had to replace 

```python
request.form.get("name")
```
with 
```python
request.args.get("name")
```
which fixed the issue

**Resources used**: [1](https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request) [2](https://www.geeksforgeeks.org/get-the-data-received-in-a-flask-request/)


## References

1. [Flask – (Creating first simple application)](https://www.geeksforgeeks.org/flask-creating-first-simple-application/)
2. [ How to Use CURL to Send API Requests ](https://devqa.io/curl-sending-api-requests/)
3. [Contacts app](https://github.com/HACKER097/Contacts-app)


## Breaking the app

### Trying large values

It was my thought that trying absurdly large values (2,499,858 chars, enough to crash mousepad) would crash the server, or give an error at the very least. But That did not happen. Infact sqlite was able to handle it perfectly, and return the correct data when requested.

## Trying unicode

Unicode also works perfectly, sqlite was able to handle unicode and return the correct data. Viewing the database, the unicode chars are stored in unicode, and not formated or encoded in any other way.

## Trying special chars

Even though sqlite is able to insert and access data which contains all special chars (eg `!@#$%^&*()_+{}|:"<>?`), there is an issue with post the way we are making post requests.

* Inserting `!@#$%^&*()_+{}|:"<>?` manually inserts `!@#$%^&*()_+{}|:"<>?`

* Inserting `!@#$%^&*()_+{}|:"<>?` using the api inserts `!@#$%^`

The issue seems to be with `&` because everything after it is truncated before incersion. Tryig the same string without `&` inserts everything correctly

* Inserting `!@#$%^*()_+{}|:"<>?` using api inserts `!@#$%^*()_+{}|:"<>?`