
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import webbrowser

load_dotenv() 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_gemini_repsonse(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    
    if uploaded_file is not None:
        
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    


st.set_page_config(page_title="Health App")

st.header("Health App")
st.write("App is designed to assist nutritionists and health enthusiasts in analyzing food items from uploaded images, calculating total calories, and providing a healthy diet plan.")
st.write("Calculate Total Calories: Users can upload an image containing food items, and the app will analyze the image, extract food items, and calculate the total calories present in those items.")
st.write("Healthy Diet Plan: In addition to calorie calculation, users can access a pre-defined healthy diet plan.")
st.subheader("Developed by vishnukanth.k")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit = st.button("Tell me the total calories")

input_prompt = """
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
            Finally you can also mention whether the food is healthy or not and also
            mention the
            percentage split of the ratio of carbohydrates,fats,fibers,sugar and other important 
            things required in our diet

Healthy Diet Plan:
1. Breakfast: Include oats, fruits, and nuts.
2. Lunch: Have a balanced meal with lean protein, vegetables, and whole grains.
3. Snack: Opt for yogurt or a piece of fruit.
4. Dinner: Keep it light with grilled fish or chicken, along with steamed vegetables.

"""



if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_repsonse(input_prompt, image_data, "")
    st.subheader("The Response is")
    st.write(response)

linkedin_button_clicked = st.button("Connect With Me On LinkedIn")
if linkedin_button_clicked:
    webbrowser.open_new_tab("https://www.linkedin.com/in/vishnukanth-k-a5552327b/")

diet_plan_button_clicked = st.button("Diet Plan")
if diet_plan_button_clicked:
    st.subheader("Healthy Diet Plan")
    st.write("1. Breakfast: Include oats, fruits, and nuts.")
    st.write("2. Lunch: Have a balanced meal with lean protein, vegetables, and whole grains.")
    st.write("3. Snack: Opt for yogurt or a piece of fruit.")
    st.write("4. Dinner: Keep it light with grilled fish or chicken, along with steamed vegetables.")
