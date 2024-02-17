import streamlit as st
import pandas as pd
st.title("Welcome Bano Qabil")

#creating dataset

df=pd.DataFrame({'first':[1,2,3,4,5,],'second':[6,7,8,9,10]})
st.write(df)

# or
df  #magic comments

import streamlit as st

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')


import streamlit as st

i1 = st.button("button 1")
st.write("value:", i1)

i2 = st.checkbox("reset button")
