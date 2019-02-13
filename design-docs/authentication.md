# Authentication

## How Does MGCL Authenticate

```python
from auth import GraphAuth
from request import GraphRequest

class GraphClient:
    def __init__(self, options):
        self.options = options
        self.access_token = GraphAuth(options).get_access_token()

    def api(self, path):
        return GraphRequest(self.access_token, path, self.options)
```

The `GraphClient` class will depend on the `get_access_token()` method exposed by the `GraphAuth` class for authentication.
It then passes on the access token to the `GraphRequest` class. 
