import os

import settings
import weaviate
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.vector_stores.weaviate import WeaviateVectorStore
from models import service_context

load_dotenv()

# Reads pdfs at "./" path
documents = SimpleDirectoryReader(input_dir=settings.INPUT_DATA_PATH).load_data()
# Connect to cloud instance
cluster_url = os.getenv("WCD_DEMO_URL")
api_key = os.getenv("WCD_DEMO_RO_KEY")

client = weaviate.connect_to_wcs(
    cluster_url=cluster_url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key),
)
# Connect to local instance
# client = weaviate.connect_to_local()

vector_store = WeaviateVectorStore(weaviate_client=client)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, service_context=service_context
)

hybrid_query_engine = index.as_query_engine(
    vector_store_query_mode="hybrid",
    similarity_top_k=4,
    alpha=0.5,
)

default_query_engine = index.as_query_engine(similarity_top_k=4)
