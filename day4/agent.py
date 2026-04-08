import re

# ================= TOOLS ================= #

def extract_numbers(query):
    return list(map(int, re.findall(r'\d+', query)))

def calculate_average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

def summarize(avg):
    return f"The average is {avg}, which represents a central value."

# ================= PLANNER ================= #

def plan_task(query):
    steps = []

    if "average" in query:
        steps.append("extract_numbers")
        steps.append("calculate_average")

    if "summarize" in query:
        steps.append("summarize")

    return steps

# ================= EXECUTOR ================= #

def execute_plan(query):
    steps = plan_task(query)
    print("Plan:", steps)

    data = None

    for step in steps:

        if step == "extract_numbers":
            data = extract_numbers(query)
            print("Step 1 - Numbers:", data)

        elif step == "calculate_average":
            data = calculate_average(data)
            print("Step 2 - Average:", data)

        elif step == "summarize":
            data = summarize(data)
            print("Step 3 - Summary:", data)

    return data

# ================= MAIN ================= #

while True:
    query = input(">> ")

    if query.lower() in ["exit", "quit"]:
        print("👋 Exiting...")
        break

    result = execute_plan(query)

    print("Final Output:", result)
