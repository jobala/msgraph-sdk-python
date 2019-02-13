# Authentication

## How Does MGCL Authenticate

```python
from auth import GraphAuth, MsalAuth
from request import GraphRequest, Requests

class GraphClient:
    def __init__(self, options):
        access_token = GraphAuth(options, auth=MsalAuth()).get_access_token()
        self.graphRequest = GraphRequest(access_token, request=Requests, options)

    def api(self, path, options):
        return self.graphRequest.path(path, options)
```

The `GraphClient` class will depend on the `get_access_token()` method exposed by the `GraphAuth` class for authentication.
It then passes on the access token to the `GraphRequest` class.
