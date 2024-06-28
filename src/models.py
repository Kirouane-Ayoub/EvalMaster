import settings
from dotenv import load_dotenv
from llama_index.core import ServiceContext
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.llms.cohere import Cohere
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.llama_cpp.llama_utils import (
    completion_to_prompt,
    messages_to_prompt,
)

load_dotenv()


embed_model = CohereEmbedding(
    model_name=settings.COHERE_EMBEDDING_MODEL,
    input_type="search_query",
)
Cohere_llm = Cohere(model=settings.COHERE_LLM_MODEL)


prometheus_llm = LlamaCPP(
    model_path=settings.PROMETHEUS_LLM_MODEL_PATH,
    temperature=0.0,
    max_new_tokens=2048,
    context_window=8192,
    model_kwargs={"n_gpu_layers": -1},
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=False,
)
# Create the service context with the cohere model for generation and embedding model
service_context = ServiceContext.from_defaults(llm=Cohere_llm, embed_model=embed_model)
