import streamlit as st

def find_largest_number(n1, n2, n3):
    return max(n1, n2, n3)

def main():
    st.title("Find the Largest Number")

    
    n1 = st.number_input("Enter the first number:", value=0.0)
    n2 = st.number_input("Enter the second number:", value=0.0)
    n3 = st.number_input("Enter the third number:", value=0.0)


    largest_number = find_largest_number(n1, n2, n3)
    st.write(f"The largest number is: {largest_number}")

if __name__ == "__main__":
    main()
