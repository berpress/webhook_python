# webhook_python
## A simple server for testing webhooks
Language: Python 

Framework: Flask 


Endpoints:

**POST /webhook**

Send data to server. Return 200 status code.

**GET /webhook**

Return last sended data.


For local use
```python
python run main.py
```

Example

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"test","password":"test"}' \
  http://127.0.0.1:5000/webhook
{
  "status": "success"
}
```
and GET request
```
curl\
  --request GET \
  http://127.0.0.1:5000/webhook

{
  "password": "test",
  "username": "test"
}
```
