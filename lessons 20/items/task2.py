server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },

    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}


for datakey, key in server_data.items():
    print(f'{datakey}:')
    for this_key, value in key.items():
        print(f'  {this_key}:{value}')