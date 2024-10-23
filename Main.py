import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #4682b4 30%, #98fb98 100%); /* Lighter blue to more light green */
    }
    .stApp * {
        color: #ffffff !important; /* Make all text white */
    }
    </style>
    """,
    unsafe_allow_html=True
)


col1 = st.columns(1)

with col1[0]:
    st.title("My life story")
    content = """"Hi im Joshua i was born on 22-09-2005
    im 19 at the time of writing this and this is my life story 
    i am gonna put it in different pages each year a different page 
    at least ill try maybe there are some years merged we will see
    """
    st.write(content)

timeline = [

    {"year": 2005, "event": """I was born in maastricht way to early to be presise ...... 
                            if they dint take me out later i couldve died i was really small when i was born i was on the intensive care because i was to light of weight"""},
    {"year": 2006, "event": "this year i dont really know much about yet ill ask my parents for some stuff"},
    {"year": 2007, "event": "same as 2006"},
    {"year": 2008, "event": "same as 2006"},
    {"year": 2009, "event": "This year my sister nina was born and she was born just on time we went on vacation with our grandparent and parents to zeeland"},
    {"year": 2010, "event": ""},
    {"year": 2011, "event": "this was my first year on primary school"},
    {"year": 2012, "event": "this was my second year on primary school"},
    {"year": 2013, "event": "this was my third year on primary school"},
    {"year": 2014, "event": "this was my fourth year on primary school"},
    {"year": 2015, "event": "this was my fifth year on primary school"},
    {"year": 2016, "event": "this was my sixth year on primary school"},
    {"year": 2017, "event": "this was my seventh year on primary school"},
    {"year": 2018, "event": "this was my last year on primary school"},
    {"year": 2019, "event": "this was my first highschool year i was super nervous and i had a lot of eczema it was really bad if i get stressed you can see it i get sick and my whole skin is full of eczema"},
    {"year": 2020, "event": "this year was my second high school year i got bullied by an old classmate i had before highschool i hated him with all my heart he trew chips at me when he saw me outside of school and made fun of me if i met him on the street now today in 2024 i dont know what i would do if he still bullied me i would honestly lose control and beat him to the ground"},
    {"year": 2021, "event": "This was my third year in highschool that was my first year i dint get bullied or talked about"},
    {"year": 2022, "event": "This year was free i dint have anything i had a bad day and night rhythm and thats because my grandpa passed away adn my final examination and my graduation i dint go to my graduation because of my grandpa "},
    {"year": 2023, "event": "This year i dint have any school i had a college with electro technic and i got to hear i got autism it was not as bad to recieve the news as i excpected but still it was expected because my dad also has autism but he has adhd with it to"},
    # Add more years here
    {"year": 2024, "event": "Turned 19 and started learning HTML, CSS, and Python"}
]

for entry in timeline:
    st.subheader(f"{entry['year']}")
    if st.checkbox(f"Show details for {entry['year']}"):
        st.write(entry['event'])
