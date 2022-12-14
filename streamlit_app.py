import streamlit
import pandas

streamlit.title('What a test')

streamlit.header('Breakfast Menu')
streamlit.text('π₯£ Omega 3 & Blueberry Oatmeal')
streamlit.text('π₯ πKale, Spinach & Rocket Smoothie')
streamlit.text('π π₯Hard-Boiled Free-Range Egg')

streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
