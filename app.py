import streamlit as st

"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)


## Here we would like to add some controllers in order to ask the user to input the characteristics of the penguin. We need to know all the inputs required by our model to make a prediction.


st.title("Penguin Species Prediction")

"""# Categorical inputs"""
island = st.selectbox(
    "Island",
    ["Biscoe", "Dream", "Torgersen"]
)

sex = st.selectbox(
    "Sex",
    ["Male", "Female"]
)

"""# Numerical inputs"""
bill_length_mm = st.number_input(
    "Bill length (mm)", min_value=0.0
)

bill_depth_mm = st.number_input(
    "Bill depth (mm)", min_value=0.0
)

flipper_length_mm = st.number_input(
    "Flipper length (mm)", min_value=0.0
)

body_mass_g = st.number_input(
    "Body mass (g)", min_value=0.0
)

"""
"""

import requests
url = 'http://localhost:8001/predict'

if st.button("Predict Species"):
  params = {
      "island": island,
      "bill_length_mm": bill_length_mm,
      "bill_depth_mm": bill_depth_mm,
      "flipper_length_mm": flipper_length_mm,
      "body_mass_g": body_mass_g,
      "sex": sex,
  }
  try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    prediction = response.json()
    st.success(f"Predicted Species: **{prediction}**")
  except requests.exceptions.RequestException as e:
    st.error(f"Error calling the API: {e}")
"""
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Of course... The `requests` package 💡

What are the steps to follow in order to call an API ?

1. Which url will you use? Save it in a variable so you can easily change it later...

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
"""
