#Smtp via MS exchange

## Usage
Create config.ini, example is included
```
[settings]
smtp_server = mail.example.org
smtp_port = 25
smtp_user = sender
smtp_password = password
from_address = sender@example.org
to_addresses = to@example.org
subject = Subject
body = Body
```

Then use it:
```
from provplan_email_lib import *
e = Emailer()
e.send_email() # this will just send whatever is in config
e.disconnect()

```

You can override some config settings in ```send_email```. ```send_email``` takes the following
 ```send_email(from_address=None, to_addresses=None, subject=None, body=None)``` 


