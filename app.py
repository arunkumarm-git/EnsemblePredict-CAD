import streamlit as st
import joblib

def main():
    st.set_page_config(page_title="CAD Prediction", page_icon="🏥", layout="centered")
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
        }
        h1 {
            color: #2b7a78;
        }
        label {
            font-size: 16px;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #2b7a78;
            color: white;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Predictive Model for Coronary Artery Disease (CAD) 🫀')

    st.write('### Give the following details:')

    col1, col2 = st.columns(2)

    # User Inputs
    with col1:
        age = st.number_input('Age', min_value=0, max_value=120, value=50)
        sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
        chest_pain_type = st.selectbox('Chest Pain Type', options=[1, 2, 3, 4], format_func=lambda x: {
            1: 'Typical angina', 2: 'Atypical angina', 3: 'Non-anginal pain', 4: 'Asymptomatic'
        }[x])
        restbp = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, max_value=300, value=120)
        chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0, max_value=1000, value=200)
        

    with col2:
        fasting_blood_sugar = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
        restecg = st.selectbox('Resting Electrocardiographic Results', options=[0, 1, 2], format_func=lambda x: {
            0: 'Normal', 1: 'ST-T wave abnormality', 2: 'Left ventricular hypertrophy'
        }[x])
        max_heart_rate = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=250, value=150)
        exercise_induced_angina = st.selectbox('Exercise Induced Angina', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
        oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=1.0)
    
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[1, 2, 3], format_func=lambda x: {
            1: 'Upsloping', 2: 'Flat', 3: 'Downsloping'
        }[x])

    all_input = [age, sex, chest_pain_type, restbp, chol, fasting_blood_sugar, restecg, max_heart_rate, exercise_induced_angina, oldpeak, slope]

    @st.cache_resource
    def load_model():
        loaded_model = joblib.load('stacking_model.pkl')
        return loaded_model
    
    loaded_model = load_model()

    # Prediction
    if st.button("Predict"):
        result = loaded_model.predict([all_input])
        
        confidence_level = loaded_model.predict_proba([all_input])
        
        st.markdown("### Prediction Result:")
        
        if result[0] == 1:
            st.error(f"You have Coronary Artery Disease with a confidence level of {confidence_level[0][1]*100:.2f}%")
        else:
            st.success(f"You don't have Coronary Artery Disease with a confidence level of {confidence_level[0][0]*100:.2f}%")

if __name__ == '__main__':
    main()
