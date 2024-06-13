import streamlit as st

import components.authenticate as authenticate
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Check authentication when user lands on the home page.
authenticate.set_st_state_vars()

# Add login/logout buttons
if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()

import streamlit as st

if st.session_state["authenticated"]:
    st.write("hello")
    st.write(st.session_state['email'])
    components.html('<form><h2>hello</h2><script src="https://checkout.razorpay.com/v1/payment-button.js" data-payment_button_id="pl_OM7y6M8cW32bnZ" async> </script> </form>',height=600)

else:
    st.write("auth")
