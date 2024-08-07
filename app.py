import streamlit as st

st.title("Abdul Rehman's Calculator")

# Input fields
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)
operator = st.selectbox("Select operator", ["+", "-", "*", "/"])

# Calculate result
if st.button("Calculate"):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2
    st.write(f"Result: {result}")

# Option to quit
quit_option = st.radio("Do you want to quit the calculator?", ("No", "Yes"))
if quit_option == "Yes":
    st.stop()
