import streamlit as st
from app_company import main as  pag1
from app_startup import main as  pag2
#from pagxx import main as pagxx
from PIL import Image
import requests
from io import BytesIO

def main():
	################ load image from web #########################
	st.title("My multipage APP")
	# url='https://frenzy86.s3.eu-west-2.amazonaws.com/python/swear.png'
	# response = requests.get(url)
	# image = Image.open(BytesIO(response.content))
	# st.image(image, caption='',use_column_width=True)
	pag_name = ["pag1","pag2",]
	
	OPTIONS = pag_name
	sim_selection = st.selectbox('Seleziona la pagina', OPTIONS)

	if sim_selection == pag_name[0]:
		pag1()
	else:
		pag2()


if __name__ == '__main__':
	main()