#porject 01: unit converter 

import streamlit as st 
 
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg,rgb(177, 223, 210), #5b548a);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.3);
    }
    h1{
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button{
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover{
        transform: scale(1.05);
        background: linear-gradient(45deg,rgb(64, 62, 180),rgb(10, 92, 110));
        color: black;
    }
    .result-box{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
        margin: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .footer{
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True 
)

#title and description
st.markdown("<h1> Unit Converter </h1>", unsafe_allow_html=True)
st.write("Seamlessly convert units of length, weight, and temperature.")

conversion_type = st.selectbox("choose conversion type", ["length", "weight", "temprature"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "length":
    with col1:
        from_unit = st.selectbox("from", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feet"]) 
elif conversion_type == "weight":
    with col1:
        from_unit = st.selectbox("from", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "temprature":
    with col1:
        from_unit = st.selectbox("from", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])


#converted function
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Milimeters': 1000, 
        'Miles': 0.000621371, 'Yards': 1.09361, 'Inches': 39.37, 'Feet': 3.28
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

            
def temprature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 +32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value -32) * 5/9 if to_unit == "Celsius" else (value -32) * 5/9 + 273.15 if to_unit == "kelvin" else value 
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5+32 if to_unit == "Fahrenheit" else value
    return value

#button for conversion

if st.button("🔄 Convert"):
    if conversion_type == "length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "temprature":
        result = temprature_converter(value, from_unit, to_unit)
    
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Created with ❤️ by Umama Shaikh</div>", unsafe_allow_html=True)
    
