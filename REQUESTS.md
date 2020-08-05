```bash

curl localhost:8888/pokemons

curl -s  localhost:8888/pokemons | jq

curl -i -H "Content-Type: application/json" -X POST -d '{"nom": "Pikachu", "type": "elec"}' localhost:8888/pokemon



```

