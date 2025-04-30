import streamlit as st

st.title("Calculator")
def addition(x,y):
    add = x + y 
    return add

def subtraction(x,y):
    sub = x - y
    return sub

def multiplication(x,y):
    multi = x * y
    return multi 

def division(x,y):
    div = x / y
    return div

def square(x,y):
    sqr = x ** y 
    return sqr

x = st.number_input("Enter Number", value = None, placeholder="Type a Number")
operator = st.selectbox("Enter a operator",("+", "-", "*", "/", "**"),index=None,placeholder="Select a Operator")


y = st.number_input("Enter another Number",value = None, placeholder="Type a Number")

if operator == "+":
    if y:
        result = addition(x,y)
        st.success(f"Your Result is {result}")
elif operator == "-":
    if y:
        result = subtraction(x,y)
        st.success(f"Your Result is {result}")
elif operator == "*":
    if y:
        result = multiplication(x,y)
        st.success(f"Your Result is {result}")
elif operator == "/":
    if y:
        if x != 0:
            result = division(x,y)
            st.success(f"Your Result is {result}")
        else:
            st.warning("Number Can not be Divided by 0")
elif operator == "**":
    if y:
        result = square(x,y)
        st.success(f"Your Result is {result}")
