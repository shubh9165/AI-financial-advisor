import streamlit as st
from agents import create_agent

st.set_page_config(page_title="AI Financial Advisor", page_icon="📈")
st.title("📈 AI Financial Advisor")
st.caption("Powered by LangChain + Groq + Zerodha Varsity")

if "agent" not in st.session_state:
    with st.spinner("Loading advisor..."):
        st.session_state.agent = create_agent()

if "session_id" not in st.session_state:
    st.session_state.session_id = "user_1"

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input("Ask about any stock or investment..."):
    st.chat_message("user").write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Fetching data and analyzing..."):
            response = st.session_state.agent.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": st.session_state.session_id}}
            )
            answer = response.get("output", str(response))
            st.write(answer)

    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": answer})