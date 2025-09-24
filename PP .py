import streamlit as st
import openai
import os

# Load OpenAI API key from environment (set in Streamlit Cloud secrets later)
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🍽️ AI Meal Planner for Health Conditions")

# User input
health_condition = st.text_input("Enter health condition (e.g. diabetes, high blood pressure)")
ingredients = st.text_area("Available ingredients (comma separated)")
calories = st.number_input("Target daily calories", min_value=100, max_value=5000, step=50)

if st.button("Generate Meal Plan"):
    if not health_condition or not ingredients:
        st.warning("Please enter health condition and ingredients.")
    else:
        prompt = f"""
        You are a nutritionist AI. Create a healthy meal plan for a patient with {health_condition}.
        Use the following ingredients if possible: {ingredients}.
        Target daily calories: {calories}.
        Give breakfast, lunch, dinner, and snacks with simple cooking instructions.
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            meal_plan = response["choices"][0]["message"]["content"]
            st.subheader("✅ Suggested Meal Plan")
            st.write(meal_plan)

        except Exception as e:
            st.error(f"Error: {str(e)}")
