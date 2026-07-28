"""
Script per inizializzare il Cosmos DB locale (emulatore).
Crea database 'appdb' e container 'richieste' con partition key /utente.
"""
from azure.cosmos import CosmosClient, PartitionKey

ENDPOINT = "https://localhost:8081"
KEY = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="

client = CosmosClient(ENDPOINT, KEY)

# Crea database
database = client.create_database_if_not_exists(id="appdb")
print(f"✅ Database 'appdb' pronto (id: {database.id})")

# Crea container
container = database.create_container_if_not_exists(
    id="richieste",
    partition_key=PartitionKey(path="/utente"),
)
print(f"✅ Container 'richieste' pronto (id: {container.id})")
