import streamlit as st
st.title('BMI Calculator')
st.header("Hello, let's calculate your body mass index")

weight = st.number_input('weight', )
height = st.number_input('height', )
if st.button("Calculate BMI") == True:
    (weight / (height ** 2)) * 10000
if st.button('Body mass status') == True:
    bmi = ((weight / (height ** 2)) * 10000)
    if bmi <= 18.4:
        st.write("You are underweight")
    elif bmi > 18.5 and bmi < 24.9:
        st.write("Your weight is normal")
    elif ((weight / (height ** 2)) * 10000) > 25 and bmi < 39.9:
        st.write("You are overweight")
    elif ((weight / (height ** 2)) * 10000) >= 40:
        st.write("You are obese")
