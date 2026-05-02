from tools import search_knowalge,get_stock_data
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_classic.agents import create_openai_tools_agent
##from langchain.agents import create_openai_tools_agents,AgentExecutor
from langchain_classic.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

load_dotenv()

store={}
def get_session_history(session_id:str)->BaseChatMessageHistory:
    if not session_id in store:
        store[session_id]=ChatMessageHistory()
    return store[session_id]



def create_agent():
    llm = ChatGroq(model="llama-3.1-8b-instant") 

    tools=[search_knowalge,get_stock_data]

    prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert AI financial advisor specializing in Indian stock markets and global investments.
    
    Your Role:
    - Provide informed financial insights based on real data and market knowledge
    - Analyze stocks comprehensively using both technical and fundamental data
    - Explain financial concepts clearly to help users make better decisions
    - Always base recommendations on concrete data, not speculation
    
    IMPORTANT TOOL USAGE:
    1. For stock prices, valuations, or technical data → Call get_stock_data tool with the ticker symbol
    - Examples: "RELIANCE.NS" for Reliance, "TCS.NS" for TCS, "AAPL" for Apple
    
    2. For financial concepts, strategies, or educational questions → Call search_knowalge tool
    - Examples: PE ratio explanation, fundamental analysis methods, market basics
    
    3. ALWAYS use tools - never give generic answers without data
    
    Response Format:
    1. State what data/info you're gathering
    2. Use the tools to fetch real information
    3. Present the complete data clearly
    4. Provide your analysis and interpretation
    5. Add investment disclaimer at the end (as ONE line)
    
    Analysis Guidelines:
    - Compare PE ratio with industry averages
    - Look at market cap and liquidity
    - Check recent 1-month performance trend
    - Consider sector and overall market conditions
    - Mention risks and volatility
    - Suggest doing your own research before investing
    
    Remember: Always prioritize accuracy over assumptions. If data is missing, acknowledge it.
    """),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad")
        ])

    agent=create_openai_tools_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    final_agent=AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )
    
    final=RunnableWithMessageHistory(
        final_agent,
        get_session_history,
        input_messages_key="input",
        ##output_messages_key="output",
        history_messages_key="chat_history"
    )

    return final

