import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

def main():
    st.title('Tumor Shrinkage Prediction Tool')
    st.write('Please input the CEA and MTHFR levels to predict tumor shrinkage.')

    cea = st.number_input('CEA Level', min_value=0.0, step=0.01, format="%.2f")
    mthfr = st.number_input('MTHFR Level', min_value=0.0, step=0.01, format="%.2f")

    if st.button('Predict'):
        input_df = pd.DataFrame({'cea': [cea], 'mthfr': [mthfr]})
        prediction = model.predict(input_df)
        st.write(f'Predicted Tumor Shrinkage: {prediction[0]:.2f}%')

if __name__ == '__main__':
    main()