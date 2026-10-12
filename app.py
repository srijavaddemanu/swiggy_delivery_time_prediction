import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Swiggy Delivery Time Prediction",page_icon="🍔",layout="wide")



with open('swiggy_model.pkl','rb') as f:
    model = pickle.load(f)
    
df = pd.read_csv('swiggy_demographic.csv')

st.title('Swiggy Delivery Time Prediction')
st.write('Enter the details to predict the estimated time of delivery')

st.image(r"C:\Users\Admin\Downloads\swiggy.png",width=1600)

col1, col2,col3 = st.columns(3)

with col1:
    
    age = st.number_input('Rider age',min_value=18,max_value=50)	

    ratings = st.number_input('Rider Rating',min_value=1.0,max_value=5.0,step=0.1)

    vehicle_condition = st.selectbox('Vehicle Condition',[0,1,2,3])

    type_of_vehicle = st.selectbox('Type of vehicle',['motorcycle', 'scooter', 'electric_scooter', 'bicycle'])
    
    weather = st.selectbox('Weather',['sunny', 'stormy', 'sandstorms', 'cloudy', 'fog', 'windy'])

    traffic = st.selectbox('Traffic',['high', 'jam', 'low', 'medium'])

    multiple_deliveries = st.selectbox('Multiple Deliveries',[ 0,1,2,3])


with col2:
    
    type_of_order = st.selectbox('Type of order',['snack', 'drinks', 'buffet', 'meal'])

    festival = st.selectbox('festival',['yes','no'])

    order_day_of_week = st.selectbox('Order_day_of_week',['saturday', 'friday', 'tuesday', 'monday', 'sunday', 'wednesday', 'thursday'])

    order_month = st.selectbox('Order_month',[2,3,4])

    order_day = st.number_input('Order_day',min_value=1,max_value=31)

    order_time_of_day = st.selectbox('Order_time_of_day',['morning', 'evening', 'afternoon', 'night', 'after_midnight'])

    order_time_hour = st.number_input('Order_time_hour',min_value=0,max_value=23)


with col3:
    
    city_type = st.selectbox('City_type',['urban', 'metropolitian', 'semi-urban'])

    city_name = st.selectbox('City_name',['INDO', 'BANG', 'COIMB', 'CHEN', 'HYD', 'RANCHI', 'MYS', 'DEH',
    'KOC', 'PUNE', 'LUDH', 'KNP', 'MUM', 'KOL', 'JAP', 'SUR', 'GOA','AURG', 'AGR', 'VAD', 'ALH', 'BHP'])

    is_weekend = st.selectbox('is_weekend',[0,1])
        
    pickup_time_minutes = st.number_input('pickup_time_minutes',min_value=0,max_value=15)

    distance = st.number_input('Distance (km)',min_value=0,max_value=100)
        

if st.button('Predict delivery time'):
    input_data = pd.DataFrame({
            'age' : [age],
            'ratings' : [ratings],
            'vehicle_condition' : [vehicle_condition],
            'weather' : [weather],
            'traffic' : [traffic],
            'type_of_order' : [type_of_order],
            'type_of_vehicle' : [type_of_vehicle],
            'multiple_deliveries' : [multiple_deliveries],
            'festival' : [festival],
            'city_type' : [city_type],
            'city_name' : [city_name],
            'order_month' : [order_month],
            'order_day' : [order_day],
            'order_time_of_day' : [order_time_of_day],
            'order_time_hour' : [order_time_hour],
            'order_day_of_week' : [order_day_of_week],
            'is_weekend' : [is_weekend],
            'pickup_time_minutes' : [pickup_time_minutes],
            'distance' : [distance]
            })
    prediction = model.predict(input_data)
    st.success(f'Estimated time of delivery is {prediction[0]:.2f} minutes for {distance} km distance')
    
