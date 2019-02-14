# Microsoft Graph Python Client Library

## Installation

Run `pip install msgraph-sdk`

## Authentication

The Microsoft Graph Python Client Library uses [MSAL](https://github.com/AzureAD/microsoft-authentication-library-for-python)
for authentication out of the box.

It reads environment variables automatically from a `.env` file at the project root.
Your `.env` file should have the following properties.

```bash
AUTHORITY=<AUTHORITY>
CLIENT_ID=<CLIENT_ID>
SECRET=<SECRET>
SCOPES=<SCOPES>
```

## Initialize  Microsoft Graph Client.

```python
from msgraph import Client

scopes = ['User.Read']

client = Client(scopes)
```

## Make Requests to Graph

```python
user = client.api('/me').get()
```
