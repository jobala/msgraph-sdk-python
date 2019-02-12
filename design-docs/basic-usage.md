## Microsoft Graph Python Client Library


#### Installation

Run `pip install msgraph-sdk`

#### Authentication

The Microsoft Graph Python Client Library uses [MSAL](https://github.com/AzureAD/microsoft-authentication-library-for-python)
for authentication. MSAL doesn't ship with this library.


#### Initialize  Microsoft Graph Client With An Authentication Provider

```python
from msgraph import Client

client = Client.init(msal, options)

# Add middlewares
client.use(redirectHandler)
```

#### Make Requests to Graph
```python
user = client.api('/me').get()
```
 
