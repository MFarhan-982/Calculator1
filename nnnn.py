import streamlit as st

# Set page configuration and theme
st.set_page_config(page_title="FARHAN's Calculator", layout="centered")
# Initialize session state variables if they don't exist
if 'display' not in st.session_state:
    st.session_state.display = ''
if 'result' not in st.session_state:
    st.session_state.result = None

st.title("Calculator")

# Function to update display
def append_to_display(value):
    st.session_state.display += value

# Function to clear display
def clear_display():
    st.session_state.display = ''
    st.session_state.result = None

# Function to calculate result
def calculate_result():
    try:
        st.session_state.result = eval(st.session_state.display)
        st.session_state.display = str(st.session_state.result)
    except:
        st.session_state.display = 'Error'

# Function to handle backspace
def backspace():
    st.session_state.display = st.session_state.display[:-1]

# Display panel
display_value = st.text_input('', value=st.session_state.display, key='input_panel')
st.session_state.display = display_value  # Update display when typing with keyboard

# Calculator buttons layout
col1, col2, col3, col4 = st.columns(4)

# First row
with col1:
    st.button('7', on_click=append_to_display, args=('7',))
with col2:
    st.button('8', on_click=append_to_display, args=('8',))
with col3:
    st.button('9', on_click=append_to_display, args=('9',))
with col4:
    st.button('/', on_click=append_to_display, args=('/',))

# Second row
with col1:
    st.button('4', on_click=append_to_display, args=('4',))
with col2:
    st.button('5', on_click=append_to_display, args=('5',))
with col3:
    st.button('6', on_click=append_to_display, args=('6',))
with col4:
    st.button('.*', on_click=append_to_display, args=('*',))

# Third row
with col1:
    st.button('1', on_click=append_to_display, args=('1',))
with col2:
    st.button('2', on_click=append_to_display, args=('2',))
with col3:
    st.button('3', on_click=append_to_display, args=('3',))
with col4:
    st.button('.-', on_click=append_to_display, args=('-',))

# Fourth row
with col1:
    st.button('0', on_click=append_to_display, args=('0',))
with col2:
    st.button('.', on_click=append_to_display, args=('.',))
with col3:
    st.button('=', on_click=calculate_result)
with col4:
    st.button('.+', on_click=append_to_display, args=('+',))

# Fifth row - Clear and Backspace
col1, col2 = st.columns(2)
with col1:
    st.button('Clear', on_click=clear_display)
with col2:
    st.button('Backspace', on_click=backspace)