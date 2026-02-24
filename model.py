import google.generativeai as genai
import ast
import operator

# -------------------------------
# Configure Gemini API Key
# -------------------------------
genai.configure(api_key="AIzaSyCkB4s4G13N6D3QXYF2LisowOk0whiiBlw") #i have changed the key :)

# Best Gemini Model
model = genai.GenerativeModel("models/gemini-2.5-flash")


# -------------------------------
# SAFE Calculator Tool Function
# -------------------------------
def safe_calculator(expr):
    ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }

    def eval_node(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return ops[type(node.op)](
                eval_node(node.left),
                eval_node(node.right)
            )
        else:
            raise ValueError("Invalid Expression")

    tree = ast.parse(expr, mode="eval")
    return eval_node(tree.body)


# -------------------------------
# AI Agent Function
# -------------------------------
def ai_agent(user_input):

    # Step 1: LLM decides if calculator tool is needed
    decision_prompt = f"""
    You are an AI agent.

    User Query: {user_input}

    Step 1:
    Decide if this query requires a mathematical calculation.

    If YES return:
    TOOL:CALCULATOR

    If NO return:
    TOOL:NO
    """

    decision = model.generate_content(decision_prompt).text.strip()

    # Print Decision Step
    if decision == "TOOL:NO":
        return "❌ Agent Decision: This query does not need calculation tool."

    print("✅ Agent Decision: Calculation tool can solve this.")

    # Step 2: LLM extracts math expression
    extract_prompt = f"""
    User Query: {user_input}

    Extract ONLY the mathematical expression.

    Example:
    Input: What is 10 + 5 * 2?
    Output: 10+5*2

    Return only expression.
    """

    expression = model.generate_content(extract_prompt).text.strip()

    print(f"🧠 LLM Extracted Expression: {expression}")

    # Step 3: Tool Call
    try:
        result = safe_calculator(expression)
        return f"✅ Final Answer: {result}"
    except:
        return "⚠️ Tool Error: Invalid math expression."


# -------------------------------
# Run Loop
# -------------------------------
while True:
    user = input("\nEnter query (or exit): ")

    if user.lower() == "exit":
        print("Agent stopped.")
        break

    print(ai_agent(user))
