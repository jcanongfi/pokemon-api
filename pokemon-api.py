#!flask/bin/python

from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from flask import abort
from flask import make_response
from flask import request

import os, fnmatch
import re
import datetime
import json
import yaml


## Initialisation flask
########################################################
app = Flask(__name__)
auth = HTTPBasicAuth()


## Initialisation directory backend
########################################################
path = "/tmp/pokemon-api"
access_rights = 0o700

if os.path.exists(path) and not os.path.isdir(path):
  print(" * Deleting %s file..." % path)
  os.remove(path)
if not os.path.exists(path):
  print(" * Initializing backend directory...")
  try:
    os.mkdir(path,access_rights)
  except OSError:
    print(" * Creation of the directory %s failed" % path)
    exit(99)
  else:
    print(" * Successfully created the directory %s " % path)



## Handler pour les reponses 404
########################################################
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'NOT FOUND'}), 404)


## Handler pour les reponses 405
########################################################
#@app.errorhandler(405)
#def not_found(error):
#    return make_response(jsonify({'error': 'METHOD NOT ALLOWED'}), 405)

def get_poke_file(id):
   file_lookup = path+"/"+id+".poke"
   nom = ""
   famille = ""
   if not os.path.exists(file_lookup):
     abort(404)
   if os.path.isdir(file_lookup):
     abort(404)
   poke_file = open(file_lookup, "r")
   poke_yml=yaml.load(poke_file,Loader=yaml.FullLoader)
   try:
     nom = (poke_yml['nom'])
   except KeyError:
     abort(404)
   try:
     famille = (poke_yml['type'])
   except KeyError:
     abort(404)
   poke_file.close()
   return { "id": id, "nom": nom, "type": famille }
   

## Obtention d'un pokemon selon son id
########################################################
@app.route('/pokemon/<string:id>', methods=['GET'])
def get_pokemon_id(id):
   datas = get_poke_file(id)
   return jsonify(datas)




## Obtention liste des pokemons
########################################################
@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    poke_list = []
    listOfFiles = os.listdir(path)
    pattern = "*.poke"
    for entry in listOfFiles:
      if fnmatch.fnmatch(entry, pattern):
        try:
          found = re.search('(.+?).poke', entry).group(1)
        except AttributeError:
          abort(400)
        poke_list.append(get_poke_file(found))
    return jsonify(poke_list)


## Creation d'un nouveau pokemon
########################################################
@app.route('/pokemon', methods=['POST'])
def create_pokemon():
    if not request.json or not 'nom' in request.json or not 'type' in request.json:
        abort(400)
# Todo : creer/utiliser un objet sequence pour eviter de redecouvrir
    seq = 0
    exists = True
    while exists:
      seq = seq + 1
      file_lookup = path+"/"+str(seq)+".poke"
      try:
        poke_file = open(file_lookup, "r")
      except FileNotFoundError:
        exists = False
    poke_file.close()
    pokemon = {
        'id': seq,
        'nom': request.json['nom'],
        'type': request.json['type']
    }
    poke_file = open(file_lookup, "w")
    yaml.dump(pokemon, poke_file)
    poke_file.close()
    return jsonify(pokemon), 201


## Page de vivacite
########################################################
@app.route('/health')
def health():
    return "ok\n"

## Page par defaut
########################################################
@app.route('/')
def index():
    return "pokemon-api\nAccepted methods :\nGET /pokemon\nGET /pokemon/<id>\nPOST /pokemon\nGET /health\n"


## Lancement de l'API
########################################################
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='8888')

