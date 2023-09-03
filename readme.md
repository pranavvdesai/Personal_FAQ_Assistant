# Custom Chatbot for your personal data

## Overview

The Personalised FAQ Chatbot is a custom chatbot designed to answer user queries related to a specific content. Users can upload a text document containing information about anything, and the chatbot leverages the power of Large Language Models (LLMs) to provide responses to questions based on the uploaded document.

## Use Cases

- **Website FAQ:** The chatbot can be used to answer user queries related to a website's content. For example, a user can upload a text file containing information about a website's features, and the chatbot can answer questions related to those features. This can be useful for websites that have a lot of content and want to provide a better user experience. The users can ask questions about the website, take help from the chatbot, and get answers to their queries. <br><br>
**For example:** For websites like Amazon or Flipkart, the chatbot can be used to answer questions related to the products available on the website. The users can ask questions about the products, take help from the chatbot, get personalized recommendations, and make a purchase decision. <br><br>
- **Customer Support:** The chatbot can be used to answer customer queries related to a product or service. For example, a user can upload a text file containing information about a product, and the chatbot can answer questions related to that product. This can be useful for companies that want to provide better customer support and reduce the number of support tickets. <br><br>
- **Knowledge Base Enhancement:** Organizations can use the chatbot to enhance their knowledge base. Users can upload documents such as manuals, guides, or FAQs, and the chatbot can provide instant answers to questions, making it easier for customers and employees to find information. <br><br>
- **Educational Assistance:** Educational institutions can employ the chatbot to help students with their coursework. Students can upload relevant course materials, and the chatbot can answer questions, provide explanations, and assist with homework or research.


## Features

- **Document Upload:** Users can upload a text file containing website information or any other content.
- **Natural Language Processing:** The chatbot utilizes LLMs to understand and process user queries.
- **Customization:** Developers can fine-tune the chatbot for specific tasks, such as summarization, translation, or sentiment analysis.
- **LlamaIndex Integration:** The chatbot integrates with LlamaIndex for efficient data indexing and retrieval.
- **LangChain Support:** LangChain simplifies interaction with LLM providers like OpenAI, making it easier to integrate different LLM models.

## How It Works

1. Users upload a text document containing information.
2. LlamaIndex creates an index from the document data, making it highly efficient to query.
3. When a user submits a question, the chatbot searches for relevant segments within the index.
4. The identified segments are paired with the user's query and sent to the LLM (GPT-3.5-turbo) via LangChain.
5. The LLM generates a personalized response based on the user's query and the document content.

## Creating index
![image](https://github.com/pranavvdesai/Personal_FAQ_Assistant/assets/74852751/1627de47-8586-4183-b4af-3a237645417e)

## Querying index
![image](https://github.com/pranavvdesai/Personal_FAQ_Assistant/assets/74852751/75e0bcd3-73a3-4651-84a8-6017b8e428ed)


