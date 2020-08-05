# pokemon-api

Begin API pokedex collecting pokemon files

Inspired by : https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

But this now works with files whereas in memory

## Prérequis

Installation virtualenv

Ex: centos 7 
```bash
sudo yum install -y python-virtualenv
```

## Préparation de l'environnement

```bash
git clone https://github.com/jcanongfi/pokemon-api.git
cd pokemon-api
virtualenv flask
flask/bin/pip install --upgrade pip
flask/bin/pip install flask
flask/bin/pip install flask_httpauth
chmod u+x pokemon-api.py
```

## Executer l'application

```bash
./pokemon-api.py
```

