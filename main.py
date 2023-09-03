import os
from textbase import bot, Message
from typing import List
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, ServiceContext, PromptHelper, StorageContext, load_index_from_storage
from langchain import OpenAI

import spacy
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text)
    return [sent.text for sent in doc.sents]

os.environ["OPENAI_API_KEY"] = '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'


@bot()
def on_message(message_history: List[Message], state: dict = None):

    # if index does not exist, create it else load it
    if not os.path.exists("index"):
        print("index.json does not exist, creating it")
        
        max_input_size = 4096
        num_outputs = 512
        max_chunk_overlap = 0.2
        chunk_size_limit = 600

        # llm predictor with langchain ChatOpenAI
        prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
        llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003"))

        # read documents from datadoc folder
        documents = SimpleDirectoryReader("datadoc", text_splitter=preprocess).load_data()

        # init index with documents data
        # This index is created using the LlamaIndex library. It processes the document content and constructs the index to facilitate efficient querying
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
        index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

        # save the created index
        index.storage_context.persist(persist_dir="index")

    # load index from storage
    storage_context = StorageContext.from_defaults(persist_dir="index")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()

    # query the index with the message
    bot_response = query_engine.query(message_history[-1]["content"][0]["value"])

    bot_response = str(bot_response)

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }
