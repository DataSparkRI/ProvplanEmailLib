#Smtp mailer

## Usage
If you want to use a config file, create one ex:config.ini. An example is included
```
[settings]
smtp_server = mail.example.org
smtp_port = 25
smtp_user = sender
smtp_password = password

```

Then use it:
```
from provplan_email_lib import *
e = Emailer(config_file='/tmp/config.ini') #path to config file
e.send_email(to_addresses='dude@programming.org',subject='Tesing out the code.', body='Unit test!',from_address='thatdude@testcase.org') 
e.disconnect()

```

Alternatively dont use a config file.
```
e = Emailer(None, smtp_server, smtp_port, smtp_user, smtp_password)
e.send_email(to_addresses='dude@programming.org',subject='Tesing out the code.', body='Unit test!',from_address='thatdude@testcase.org') 
e.disconnect()
```
