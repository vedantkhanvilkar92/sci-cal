import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")

st.title("🧮 Scientific Calculator")

# Input field
expression = st.text_input("Enter expression (e.g., sin(30), log(10), 2**5, sqrt(9)):")

# Allowed math functions
allowed_functions = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log10,
    "ln": math.log,
    "sqrt": math.sqrt,
    "pi": math.pi,
    "e": math.e,
    "factorial": math.factorial
}

# Convert degrees to radians for trig functions
def evaluate_expression(expr):
    try:
        # Replace functions to python-friendly
        expr = expr.replace("sin", "math.sin(math.radians")
        expr = expr.replace("cos", "math.cos(math.radians")
        expr = expr.replace("tan", "math.tan(math.radians")

        # Adjust closing brackets for radians conversion
        expr = expr.replace(")", "))")

        # Evaluate safely
        result = eval(expr, {"__builtins__": None}, {"math": math})
        return result
    except Exception as e:
        return f"Error: {e}"

# Calculate button
if st.button("Calculate"):
    output = evaluate_expression(expression)
    st.success(f"Result: {output}")

# Side panel info
with st.sidebar:
    st.header("Supported Functions")
    st.write("""
    - sin(x) → Sine  
    - cos(x) → Cosine  
    - tan(x) → Tangent  
    - log(x) → Log base 10  
    - ln(x) → Natural log  
    - sqrt(x) → Square root  
    - factorial(x) → x!  
    - pi, e  
    - Arithmetic operations: +, -, *, /, %, **  
    """)
