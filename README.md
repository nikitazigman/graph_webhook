## HOW TO RUN:
1. Sign up and install ngrok https://ngrok.com/
2. Create venv with poetry    
```
   poetry install
   poetry shell 
```
3. start ngrok 
```
ngrok http http://localhost:8080 
```
4. start fastapi app
```
python src/main.py
```
5. add subscription via graph api explorer 
```
POST https://graph.microsoft.com/v1.0/subscriptions
body = {
    "changeType": "created,updated,deleted",
    "notificationUrl": "<ngrok url>/test-emails",
    "lifecycleNotificationUrl": "<ngrok url>/lifecycle-notifications",
    "resource": "me/messages",
    "expirationDateTime": "2024-06-26T10:30:00.9356913Z",
    "clientState": "test state"
}
headers = {
    "Prefer": 'IdType="ImmutableId"'
}
```
6. enjoy 