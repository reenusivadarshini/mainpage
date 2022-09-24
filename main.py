from PIL import Image


image = Image.open('header.png')
st.sidebar.image(image)

st.image(image, caption=' ')

