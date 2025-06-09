import streamlit as st
import base64

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "🔵"
    elif 18.5 <= bmi < 25:
        return "Normal weight", "🟢"
    elif 25 <= bmi < 30:
        return "Overweight", "🟠"
    else:
        return "Obese", "🔴"

# Optional: Encode a local background image to base64
def get_base64_bg(file_path):
    with open(file_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

def main():
    st.set_page_config(page_title="BMI Calculator", page_icon="💪")


    st.title("💪 BMI Calculator")
    st.write("Calculate your Body Mass Index")

    # BMI chart image (optional)
    st.image("body.jpg")

    # Input
    weight = st.number_input("Enter your weight (kg)", format="%.2f")
    height = st.number_input("Enter your height (m)", format="%.2f")

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            category, emoji = get_bmi_category(bmi)
            st.success(f"Your BMI is **{bmi}**")
            st.info(f"Category: **{category}** {emoji}")
        else:
            st.error("Height must be greater than 0.")

if __name__ == "__main__":
    main()
