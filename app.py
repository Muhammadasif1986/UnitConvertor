import streamlit as st
import pint

# Streamlit Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Google-Style UI Enhancements
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: white;
    }
    .stApp {
        max-width: 800px;
        margin: auto;
        padding: 20px;
        border-radius: 10px;
        background: white;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    }
    .stTitle {
        text-align: center;
        font-weight: bold;
        color: #4285F4;
        font-size: 32px;
    }
    .stSubheader {
        text-align: center;
        color: #666;
    }
    .stSelectbox, .stNumberInput, .stButton {
        font-size: 18px !important;
        border-radius: 10px !important;
    }
    .stSuccess {
        font-size: 22px !important;
        font-weight: bold;
        color: #34A853;
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        background: #E8F5E9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Pint Unit Registry
ureg = pint.UnitRegistry()

# Title
st.markdown("<h1 class='stTitle'>Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='stSubheader'>Created By M. Asif</h3>", unsafe_allow_html=True)
st.write("---")

# Conversion Categories
categories = ["Length", "Mass", "Time", "Speed", "Temperature", "Volume", "Data Transfer Rate"]

# Unit Dictionaries
unit_options = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
    "Mass": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Time": ["second", "minute", "hour", "day"],
    "Speed": ["meter per second", "kilometer per hour", "miles per hour"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "milliliter", "gallon", "cubic meter", "cup", "pint", "quart"],
    "Data Transfer Rate": ["bit per second", "kilobit per second", "megabit per second", "gigabit per second"]
}

# User selects category
category = st.selectbox(" Select Conversion Category", categories)

# User selects "From" and "To" units
from_unit = st.selectbox(" From Unit", unit_options[category])
to_unit = st.selectbox(" To Unit", unit_options[category])

# User input
value = st.number_input(" Enter Value", min_value=0.0, format="%.2f")

# Conversion Logic using Pint
if st.button(" Convert", use_container_width=True):
    try:
        if category == "Temperature":
            # Custom Temperature Conversion
            if from_unit == "celsius" and to_unit == "fahrenheit":
                converted_value = (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                converted_value = (value - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                converted_value = value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                converted_value = value - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                converted_value = (value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                converted_value = (value - 273.15) * 9/5 + 32
            else:
                converted_value = value  # Same unit case
        else:
            # Pint handles all other conversions
            converted_value = ureg.Quantity(value, from_unit).to(to_unit).magnitude

        st.markdown(f"<p class='stSuccess'> Converted Value: {converted_value:.2f} {to_unit}</p>", unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f" Conversion Error: {e}")
