from tools import calculator, weather, summarize

def decide_tool(user_input):
    if "calculate" in user_input:
        return "calculator"
    elif "weather" in user_input:
        return "weather"
    elif "summarize" in user_input:
        return "summarize"
    return None

while True:
    user = input(">> ")
    tool = decide_tool(user.lower())

    if tool == "calculator":
        print(calculator(user.replace("calculate", "")))
    elif tool == "weather":
        print(weather())
    elif tool == "summarize":
        print(summarize(user.replace("summarize", "")))
    else:
        print("No tool found")
