import streamlit as st
import datetime

st.title("🧠 Smart Health Assistant")
st.write(f"🕒 Current Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

st.write(" Have you taken a meal?")
food = st.radio("Meal Taken?", ["Yes", "No"])
if food == "No":
    st.warning("⚠️ Please take a meal!")
else:
    st.success("✅ Good you have taken a meal.")

st.write(" Have you done any exercise today?")
exercise = st.radio("Exercise Done?", ["Yes", "No"])
if exercise == "No":
    st.warning("⚠️ Please do some exercise!")
else:
    st.success(" Well done!")

st.write(" Enter your food log:")
food_log = []
total_calories = 0

food_type = st.text_input("Enter food type:")
calories = st.number_input("Enter calories:", 0)

if st.button("Add Food"):
    food_log.append((food_type, calories))
    total_calories += calories
    st.success(f"Added {food_type} with {calories} calories.")

st.write("Total Calories:", total_calories)
if total_calories > 2200:
    st.error(" You are overeating!")
else:
    st.success(" You are eating well.")

st.info("💧 Remember to drink at least 2 litres of water daily!")

mood = st.text_input("How are you feeling today?")
if mood:
    st.write(f" It's okay to feel {mood}. Your emotions matter.")
