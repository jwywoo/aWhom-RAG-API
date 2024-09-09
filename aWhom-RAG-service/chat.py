import streamlit as st
import os

from dotenv import load_dotenv
from util.db_connection import getting_persona
from retrieval.retrieval_chain import retrieval_chain_init
from generation.prompt_generation import get_prompt_generation
from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser



load_dotenv()

st.set_page_config(page_title="aWhom: aWoo", page_icon="🪖")

st.title("🪖 aWoo")
st.caption("Woo의 20대 후반 페르소나")

def get_ai_message(user_message):
    selected_persona = getting_persona(
        os.environ.get('MONGO_DB_KEY'),
        "HA-RAG-META",
        "generated_persona_prompt",
        1
    )
    retrieval_chain = retrieval_chain_init(selected_persona=selected_persona)
    prompt_for_generation = get_prompt_generation(selected_persona)
    llm = ChatOpenAI(temperature=0)
    final_rag_chain = (
        {
            "context": retrieval_chain,
            "question": itemgetter("question")
        }
        | prompt_for_generation
        | llm
        | StrOutputParser()
    )
    return final_rag_chain.invoke({"question":user_message})


if 'message_list' not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    with st.chat_message(message['role']):
        st.write(message["content"])

if user_question := st.chat_input(placeholder="Woo의 20대 후반의 페르소나와 대화 해 보세요!"):
    # User input
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({
        "role":"user",
        "content": user_question
    })
    
    with st.spinner("aWoo는 고민중!"):
        ai_message = get_ai_message(user_question)
        # Chatbot output
        with st.chat_message("ai"):
            st.write(ai_message)
    st.session_state.message_list.append({
        "role":"ai",
        "content": ai_message
    })