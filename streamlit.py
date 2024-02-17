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


import streamlit as st

st.header('This is a header with a divider', divider='rainbow')
st.header('_ Sir.Ghufran Kamal_ is :blue[cool] :sunglasses:')
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://banoqabil.pk" target="_blank">Bano Qabil Alkhidmat </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
