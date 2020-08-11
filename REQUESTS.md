# Get all pokemons

```bash
curl localhost:8888/pokemon
curl -s localhost:8888/pokemon | jq
```

# Get a pokemon by id

```bash
curl -s localhost:8888/pokemon/1
curl -s localhost:8888/pokemon/1 | jq
```

# Create a pokemon 

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"nom": "Pikachu", "type": "elec"}' localhost:8888/pokemon
curl -s -H "Content-Type: application/json" -X POST -d '{"nom": "Pikachu", "type": "elec"}' localhost:8888/pokemon | jq
```

# Delete a pokemon

```bash
curl -s -X DELETE localhost:8888/pokemon/1
```

# Update a pokemon

## Full update 

```bash
curl -s -X PUT -H "Content-Type: application/json" -d '{"nom": "Pikachu", "type": "elec"}' localhost:8888/pokemon/6 | jq
```

## Partial update

TODO

