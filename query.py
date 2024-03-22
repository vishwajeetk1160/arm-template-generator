import logging
import sys
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext, load_index_from_storage
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


documents = SimpleDirectoryReader("data").load_data()

# bge embedding model
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

# ollama
Settings.llm = Ollama(model="mistral", request_timeout=300.0)


# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./indexes")
# load index
index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("Give me a JSON arm template to deploy a storage account. It should contain default values")
print(response)