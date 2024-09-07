import streamlit as st


st.set_page_config(page_title="aWhom: aWoo", page_icon="🪖")

st.title("🪖 aWoo")
st.caption("Woo의 20대 후반 페르소나")

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

print(f"before: {st.session_state.message_list}")


for message in st.session_state.message_list:
    with st.chat_message(message['role']):
        st.write(message["content"])

if user_question := st.chat_input(placeholder="Woo의 20대 후반의 페르소나와 대화 해 보세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({
        "role":"user",
        "content": user_question
    })
        
print(f"after: {st.session_state.message_list}")