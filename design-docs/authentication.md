## Authentication

#### MSAL

**Step 1**
```shell
pip install msal
```

step **2**

Create an instance of MSAL

```python
import msal

auth = msal.ConfidentialClientApplication(
  config['client_id'],
  authority=authority['authority'],
  client_credential=config['secret']
)
```



