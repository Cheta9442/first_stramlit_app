import streamlit;
import pandas;

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
streamlit.title("My Parents New Healthy Dinner");

streamlit.header("Breakfast Favorites");

streamlit.text("🥣 Omega 3 & Blueberry oatmeal");
streamlit.text("🥗 kale, Spinach & Rocket Smoothie");
streamlit.text("🍞 Hard-Boiled Free Range Egg");
streamlit.text("🐔 Avocado Toast");


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index));

streamlit.dataframe(my_fruit_list);
