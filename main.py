from PIL import Image
image = Image.open('Mental Health (1).png')

st.sidebar.image(image)

image = Image.open('header.png')

st.image(image, caption=' ')

