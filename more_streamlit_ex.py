import datetime
import streamlit as st

d = st.date_input("When's your birthday", datetime.date(2000, 7, 6))
st.write('Your birthday is:', d)


import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "apps": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
    }
)

st.data_editor(
    data_df, 
    column_config={
        "apps": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        )
    },
    hide_index=True,
)

import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

'''
# python -m pip install plotly
import plotly.express as px

df = px.data.gapminder()

fig = px.bar(df, x="continent", y="pop", color="continent",
  animation_frame="year", animation_group="country", range_y=[0,4000000000])
fig.show()
'''

import streamlit as st
import sqlite3

# Connect to the database
conn = sqlite3.connect('students.db')

# Create a cursor
cursor = conn.cursor()

# Define the registration form
def registration_form():
    name = st.text_input("Name")
    age = st.number_input("Age")
    class_name = st.selectbox("Class", get_class_options())

    if st.button("Register"):
        # Insert the student into the database
        cursor.execute("""
            INSERT INTO students (name, age, class_id)
            VALUES (?, ?, (SELECT id FROM classes WHERE name = ?))
        """, (name, age, class_name))

        # Commit the changes
        conn.commit()

        # Display a success message
        st.write("Student registered successfully!")

# Define a function to get the class options
def get_class_options():
    cursor.execute("SELECT name FROM classes")
    return [row[0] for row in cursor.fetchall()]

# Define a function to create a class
def create_class():
    name = st.text_input("Name")
    max_age = st.number_input("Max age")
    min_age = st.number_input("Min age")

    if st.button("Create"):
        # Insert the class into the database
        cursor.execute("""
            INSERT INTO classes (name, max_age, min_age)
            VALUES (?, ?, ?)
        """, (name, max_age, min_age))

        # Commit the changes
        conn.commit()

        # Display a success message
        st.write("Class created successfully!")

# Display the registration form and the class management buttons
registration_form()
st.button("Create class", on_click=create_class)

# Close the cursor and connection
cursor.close()
conn.close()
