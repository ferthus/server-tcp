# server-tcp
[dummy] Server and Client use protocol TCP for the comunication

# Install dependency for develop
```shell
    $ pip3 install -r requirements.txt
```

# Execute server
```shell
    $ export SERVER_HOST="127.0.0.1"  # => only for change the value default
    $ export SERVER_HOST="5005" # => only for change the value default
    $ python3 server.py
```

# Execute client
```shell
    $ export CLIENT_HOST="127.0.0.1"  # => only for change the value default
    $ export CLIENT_HOST="5005" # => only for change the value default
    $ python3 client.py
```

# Execute case 1
```shell
    $ python3 client.py
    prompt: hola
    server: HOLA
```

# Execute case 2
```shell
    $ python3 client.py
    prompt: DESCONEXION
    server: bye
```
