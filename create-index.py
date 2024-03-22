import logging
import sys
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext, load_index_from_storage
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


documents = SimpleDirectoryReader("data").load_data()

# bge embedding model
# no custom parameters has been passed to embedding model
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

index = VectorStoreIndex.from_documents(
    documents,
)
index.storage_context.persist(persist_dir="./indexes")