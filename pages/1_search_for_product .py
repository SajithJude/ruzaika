import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Recomendation system")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("search for a product here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)

