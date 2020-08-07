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
seq = 1

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


## Obtention d'un pokemon selon son id
########################################################
@app.route('/pokemons/<string:task_id>', methods=['GET'])
def get_task(task_id):
   file_lookup = path+"/"+task_id+".poke"
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
#    datas = [ { "id": 1, "nom": "pikachu", "type": "elec" },{ "id": 2, "nom": "bulbizzare", "type": "eau" } ]
#   datas = { "id": task_id , "nom": "pikachu", "type": "elec" }
   datas = { "id": task_id, "nom": nom, "type": famille }
   return jsonify(datas)




## Obtention liste des pokemons
########################################################
@app.route('/pokemons', methods=['GET'])
def get_pokemons():
#    json_list = []
    listOfFiles = os.listdir(path)
    pattern = "*.poke"
    print("toto")
    for entry in listOfFiles:
      print(entry)
      if fnmatch.fnmatch(entry, pattern):
        print(entry)
#
#            try:
#              found = re.search('json_(.+?).json', entry).group(1)
#            except AttributeError:
#              found = 'Error' # apply your error handling
##            print(found)
#            json_list.append(found)
#            #json_list.append(entry)
##    return jsonify({'pokemons': json_list})
#    json_list = [ { "id": 1, "nom": "pikachu", "type": "elec" } ]
    json_list = [ { "id": 1, "nom": "pikachu", "type": "elec" },{ "id": 2, "nom": "bulbizzare", "type": "eau" } ]
    return jsonify(json_list)


## Creation d'un nouveau pokemon
########################################################
@app.route('/pokemon', methods=['POST'])
def create_pokemon():
    if not request.json or not 'nom' in request.json or not 'type' in request.json:
        abort(400)
 #TODO# Tester precence/existence du fichier
#    print seq
#    seq = seq + 1
#    print seq
#    filename = path+"/json_"+timestamp+".json"
#    new_fichier = open(filename, "w")
#    new_fichier.write(json.dumps(request.json, indent=4))
#    new_fichier.close()
#    task = {
#        'id': timestamp,
#        'title': request.json['title'],
#        'description': request.json.get('description', ""),
#        'done': False
#    }
    print(request.json) 
    pokemon = {
        'id': 1,
        'nom': request.json['nom'],
        'type': request.json['type']
    }
#    return jsonify({'pokemon': pokemon}), 201
    return jsonify(pokemon), 201
#    return jsonify({'task': task}), 201



## Page de vivacite
########################################################
@app.route('/health')
def health():
    return "ok\n"

## Page par defaut
########################################################
@app.route('/')
def index():
    return "pokemon-api\nAccepted methods :\nGET /pokemons\nPOST /pokemon\nGET /health\n"


## Lancement de l'API
########################################################
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='8888')


