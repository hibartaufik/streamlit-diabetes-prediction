import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Diabetes Prediction" ,layout="wide")
    
pickle_in = open("knn_model.pkl", "rb")
classifier = pickle.load(pickle_in)


def predict_authentication(prg, glc, bp, skin, ins, bmi, dpf, age):
    prediction = classifier.predict([[prg, glc, bp, skin, ins, bmi, dpf, age]])
    print(prediction)
    return prediction

def main():
    st.title("Diabetes Prediction")
    st.write("Prediksi penyakit Diabetes dengan model pembelajaran mesin yang menggunakan algoritma K-Nearest Neighbors.")

    col1, col2 = st.columns((1, 1))
    with col1:
        st.subheader("Pregnancies")
        prg = st.slider("Total angka kehamilan", 0, 20)
        st.subheader("Glucose")
        glc = st.slider("Konsentrasi glukosa yang ada pada tubuh setelah 2 jam tes", 50, 300)
        st.subheader("Blood Pressure")
        bp = st.slider("Tekanan darah diastolik pasien", 20, 180)
        st.subheader("Skin Thickness")
        skin = st.slider("Triceps skin fold thickness (nilai yang digunakan untuk memperkirakan lemak tubuh)", 10, 100)

    with col2:
        st.subheader("Insulin")
        ins = st.slider("Jumlah serum insulin dalam tubuh", 10, 600)
        st.subheader("BMI")
        bmi = st.slider("Body Mass Index", 10.0, 100.0, step=0.1, format="%.1f")
        st.subheader("Diabetes Pidegree Function")
        dpf = st.slider("Indikator riwayat diabetes dalam keluarga", 0.1, 2.5, step=0.001, format="%.3f",)
        st.subheader("Age")
        age = st.slider("Umur", 5, 100)

    predict_result = ""

    if st.button("PREDIKSI!"):
        predict_result = predict_authentication(int(prg), int(glc), int(bp), int(skin), int(ins), float(bmi), float(dpf), int(age))
        if predict_result == 1:
            predict_result = "POSITIF"
            st.error(f"HASIL PREDIKSI: {predict_result}")
        else:
            predict_result = "NEGATIF"
            st.success(f"HASIL PREDIKSI: {predict_result}")
            st.balloons()



if __name__ == '__main__':
        main()