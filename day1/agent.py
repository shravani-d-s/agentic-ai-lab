def decide_action(user_input):
    if "calculate" in user_input:
        return "calculator"
    elif "date" in user_input:
        return "date"
    elif "hello" in user_input:
        return "greet"
    return "unknown"

def execute(action, user_input):
    if action == "calculator":
        expr = user_input.replace("calculate", "")
        return eval(expr)
    elif action == "date":
        from datetime import datetime
        return datetime.now()
    elif action == "greet":
        return "Hello!"
    return "Unknown command"

while True:
    user = input(">> ")
    action = decide_action(user.lower())
    result = execute(action, user)
    print(result)
