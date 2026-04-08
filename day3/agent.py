import os
import re
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# 🔑 Load Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ ERROR: GROQ_API_KEY not found in .env file")
    exit()

os.environ["OPENAI_API_KEY"] = api_key

# 🚀 Groq LLM (latest working model)
llm = ChatOpenAI(
    model="llama-3.1-8b-instant",
    base_url="https://api.groq.com/openai/v1",
    temperature=0
)

# ================= TOOLS ================= #

def extract_expression(query):
    return "".join(re.findall(r'[0-9+\-*/().]+', query))

def calculator(expr):
    try:
        return str(eval(expr, {"__builtins__": None}, {}))
    except:
        return "Invalid expression"

def weather():
    return "Weather in Bhopal: 30°C"

def summarize(text):
    cleaned = re.sub(r'\bsummarize\b', '', text, flags=re.IGNORECASE).strip()

    if not cleaned:
        return "Nothing to summarize."

    try:
        prompt = f"Summarize this in one clear sentence:\n{cleaned}"
        response = llm.invoke(prompt)
        return response.content.strip()
    except:
        return cleaned[:60] + "..."

# ================= LLM DECISION ================= #

def get_prompt(query):
    return f"""
You are an AI agent that selects the correct tool.

TOOLS:
- calculator → math operations
- weather → weather queries
- summarize → text summarization

RULES:
- Return ONLY the tool name
- No explanation

EXAMPLES:
Query: What is 5+7?
Answer: calculator

Query: Tell me weather today
Answer: weather

Query: Summarize this paragraph
Answer: summarize

Now decide:

Query: {query}
Answer:
"""

def decide_tool(query):
    try:
        response = llm.invoke(get_prompt(query))
        tool = response.content.strip().lower()
        tool = tool.split()[0]

        print("LLM chose:", tool)
        return tool

    except Exception as e:
        print("❌ API ERROR:", e)
        print("⚠️ Using fallback...")

        query = query.lower()

        if any(op in query for op in ["+", "-", "*", "/"]):
            return "calculator"
        elif "weather" in query:
            return "weather"
        elif "summarize" in query:
            return "summarize"
        else:
            return "calculator"

# ================= MAIN LOOP ================= #

while True:
    query = input(">> ")

    if query.lower() in ["exit", "quit"]:
        print("👋 Exiting...")
        break

    tool = decide_tool(query)

    if tool == "calculator":
        expr = extract_expression(query)
        result = calculator(expr)

    elif tool == "weather":
        result = weather()

    elif tool == "summarize":
        result = summarize(query)

    else:
        result = "No tool matched"

    print("Output:", result)
