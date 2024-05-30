from langchain.agents import ConversationalChatAgent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.runnables import RunnableConfig
from transformers import pipeline
import torch
import streamlit as st
from AI_assistant_DB import main
from AI_Assistant_Query import query_rag
import subprocess
import time
import sys
import os

#Populate the database
#main()


# Function to install Ollama if not already installed
def install_ollama():
    # Run the setup script
    subprocess.check_call(["/bin/bash", "setupollama.sh"])

# Function to start Ollama server as a subprocess
def start_ollama_server():
    process = subprocess.Popen(["ollama", "start", "--port", "8000"])
    time.sleep(3)  # Wait for the server to start
    return process

# Install Ollama
install_ollama()

# Start the Ollama server
ollama_process = start_ollama_server()

print(torch.__version__)
st.set_page_config(page_title="LangChain: Chat with search", page_icon="🦜")
st.title("🦜 My AI Assistant")

# Utilisation de transformers pour charger un modèle localement
#try:
#    #pipeline("text-generation", model="tiiuae/falcon-7b-instruct", trust_remote_code=True)
#    llm = pipeline("text-generation", model="gpt2", framework="pt")  # force PyTorch framework
#except RuntimeError as e:
#    st.error("Error loading model: " + str(e))
#    st.stop()

msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(
    chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
)
if len(msgs.messages) == 0 or st.sidebar.button("Reset chat history"):
    msgs.clear()
    msgs.add_ai_message("How can I help you?")
    st.session_state.steps = {}

avatars = {"human": "user", "ai": "assistant"}
for idx, msg in enumerate(msgs.messages):
    with st.chat_message(avatars[msg.type]):
        # Render intermediate steps if any were saved
        for step in st.session_state.steps.get(str(idx), []):
            if step[0].tool == "_Exception":
                continue
            with st.status(f"**{step[0].tool}**: {step[0].tool_input}", state="complete"):
                st.write(step[0].log)
                st.write(step[1])
        st.write(msg.content)

if prompt := st.chat_input(placeholder="Who won the Women's U.S. Open in 2018?"):
    st.chat_message("user").write(prompt)

    # Générer une réponse à l'aide du modèle local
    #response = llm(prompt, max_length=100)
    #response_text = response[0]["generated_text"]
    response_text = query_rag(prompt)

    with st.chat_message("assistant"):
        st.write(response_text)
        st.session_state.steps[str(len(msgs.messages) - 1)] = []
