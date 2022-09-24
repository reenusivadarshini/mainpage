from PIL import Image

st.sidebar.image(image)

image = Image.open('header.png')

st.image(image, caption=' ')

