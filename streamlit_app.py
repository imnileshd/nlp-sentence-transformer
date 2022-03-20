import streamlit as st
import helper

APP_NAME = "Smart Contact Form!"

st.set_page_config(
    page_title=APP_NAME,
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.markdown("Made with love using [streamlit](https://streamlit.io/)")
st.sidebar.image(
    "images/contact.png"
)

st.sidebar.title(APP_NAME)

st.header(APP_NAME)

form_expander = st.expander(label='Contact Form')
with form_expander:
    sample_queries = [
        "How to cancel my service?",
        "new application",
        "please send my bills"
    ]       
    show = st.checkbox("Show Sample Queries")
    with st.form('Contact Form'):
        name = st.text_input('Name: ')
        email = st.text_input('Email Address:')
        if show:
            query = st.selectbox('Select Sample Query:', sample_queries, key=1)
        else:
            query = st.text_input('Ask Query:', 'Pay Online')
        submitted = st.form_submit_button('Submit')

if submitted:
    # show the result response
    st.subheader("Result")
    responses = helper.get_query_responses(query, top_k=1)
    st.json(responses)

    st.subheader("Response")
    st.success(f"Hello {name},\n{responses[0]['Response']}\nThanks")