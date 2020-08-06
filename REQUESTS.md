# Get all pokemons

```bash
curl localhost:8888/pokemons
curl -s localhost:8888/pokemons | jq
```

# Get one pokemon by id

```bash
curl -s localhost:8888/pokemons/1
curl -s localhost:8888/pokemons/1 | jq
```

# Create one pokemon 

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"nom": "Pikachu", "type": "elec"}' localhost:8888/pokemon
curl -s -H "Content-Type: application/json" -X POST -d '{"nom": "Pikachu", "type": "elec"}' localhost:8888/pokemon | jq
```

