pip install streamlit
import streamlit as st

def largest_num(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

def main():
    st.title("Find the Largest Number")
    st.write("Enter three numbers below:")
    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")
    c = st.number_input("Enter third number")
    if st.button("Find Largest"):
        result = largest_num(a, b, c)
        st.write("The largest number is: ", result)

if __name__ == "__main__":
    main()
