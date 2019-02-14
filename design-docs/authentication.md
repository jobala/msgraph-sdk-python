# Authentication

## How Does MGCL Authenticate

```python
from auth import GraphAuth, MsalAuth
from request import GraphRequest, Requests

class GraphClient:
    def __init__(self, scopes):
        config = self.get_config_from_env(scopes)
        access_token = GraphAuth(config, MsalAuth()).get_access_token()
        self.graphRequest = GraphRequest(access_token, Requests())

    def api(self, path, options):
        return self.graphRequest.path(path, options)
        
    def get_config_from_env(self, scopes):
        return 'options with scopes'
```

The `GraphClient` class will depend on the `get_access_token()` method exposed by the `GraphAuth` class for authentication.
It then passes on the access token to the `GraphRequest` class.
