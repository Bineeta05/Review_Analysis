import streamlit as st
from PIL import Image
import joblib
st.title('Review Analysis')
test_model = joblib.load('Movie_Reviews')
ip = st.text_input('Enter your message in 2-3 lines')
op = test_model.predict([ip])
if st.button('Predict'):
  if (op[0]=='pos'):
    st.title('Positive Review')
    image_pos = Image.open('/content/drive/MyDrive/Practice Colab/Positive Review.png')
    st.image(image_pos, caption=None, width=None, use_column_width=None)
  else:
    st.title('Negative Review')
    image_neg = Image.open('/content/drive/MyDrive/Practice Colab/Negative Review.png')
    st.image(image_neg, caption=None, width=None, use_column_width=None)

