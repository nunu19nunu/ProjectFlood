import streamlit as st
import joblib
import pandas as pd

model = joblib.load('randomforestv2.pkl')  # Load your model file

selected_columns = {'flooding':'น้ำท่วมขัง' , 'overflow':'น้ำล้นตลิ่ง', 'flashflood':'น้ำท่วมฉับพลัน', 'feq2':'2 ปีครั้ง', 'feq3':'3 ปีครั้ง', 'feq4':'4 ปีครั้ง', 'house':'น้ำท่วมแต่ไม่ท่วมบ้าน',
                    'habitable':'น้ำท่วมบางส่วนแต่อาศัยได้', 'evacuated':'น้ำท่วมบ้านต้องอพยพ', 'transportation':'เส้นทางคมนาคม', 'benefit':'สาธารณประโยชน์', 'area':'พื้นที่การเกษตร', 'fishing':'การประมง', 'Jan':'มกราคม', 'Feb':'กุมภาพันธ์', 'Mar':'มีนาคม',
                    'Apr':'เมษายน', 'May':'พฤษภาคม', 'Jun':'มิถุนายน', 'Jul':'กรกฎาคม', 'Aug':'สิงหาคม', 'Sep':'กันยายน', 'Oct':'ตุลาคม', 'Nov':'พฤศจิกายน', 'Dec':'ธันวาคม'}


province_mapping = {
    1: "กระบี่",
    2: "ชุมพร",
    3: "ตรัง",
    4: "นครศรีธรรมราช",
    5: "นราธิวาส",
    6: "ปัตตานี",
    7: "พังงา",
    8: "พัทลุง",
    9: "ภูเก็ต",
    10: "ยะลา",
    11: "ระนอง",
    12: "สงขลา",
    13: "สตูล",
    14: "สุราษฎร์ธานี"
}

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # If the value is not found

def predict_province_result(input_data):

    prediction = model.predict(input_data)
    predicted_class = prediction[0]

    risk_level_labels = {
        1: 'Low',
        2: 'Moderate',
        3: 'Medium',
        4: 'High',
        5: 'Very High'
    }
    predicted_risk_level = risk_level_labels[predicted_class]

    return predicted_risk_level

def main():
    st.title("การทำนายความเสี่ยงน้ำท่วมในภาคใต้")
    input_features = {}

    # User input
    province_input = st.selectbox("กรุณาเลือกจังหวัด:", ["เลือกจังหวัด"] + list(province_mapping.values()))
    input_features['province'] = get_key_by_value(province_mapping, province_input)

    # Create radio buttons for each variable
    for column in selected_columns:
        # Map for binary columns
        binary_labels = {
            1: "เกิด",
            0: "ไม่เกิด"
        }
        option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()), key=column)
        input_features[column] = get_key_by_value(binary_labels, option_input)

    if st.button("ทำนาย"):

        # Display result
        if province_input == "เลือกจังหวัด":
            st.warning("กรุณาเลือกจังหวัด.")
        else:
            input_data = pd.DataFrame([input_features])
            result = predict_province_result(input_data)
            st.text(f"{province_input}: ความเสี่ยงเกิดน้ำท่วม {result}")
            # st.text(f"{province_input}: ความน่าจะเป็นเกิดน้ำท่วม {result * 100:.2f}%")

if __name__ == '__main__':
    main()

    # User input


    # # Split the header into sections
    # section1 = ['น้ำท่วมขัง', 'น้ำล้นตลิ่ง', 'น้ำท่วมฉับพลัน']
    # section2 = ['2 ปีครั้ง', '3 ปีครั้ง', '4 ปีครั้ง']
    # section3 = ['น้ำท่วมแต่ไม่ท่วมบ้าน', 'น้ำท่วมบางส่วนแต่อาศัยได้', 'น้ำท่วมบ้านต้องอพยพ']
    # section4 = ['เส้นทางคมนาคม', 'สาธารณประโยชน์', 'พื้นที่การเกษตร', 'การประมง']
    # section5 = ['มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'สิงหาคม', 'กันยายน',
    #             'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']
    #
    # # Display the header using st.beta_columns
    # col1, col2, col3, col4, col5 = st.columns(5)
    #
    # with col1:
    #     st.text(section1[0])
    #     st.text(section1[1])
    #     st.text(section1[2])
    #
    # with col2:
    #     st.text(section2[0])
    #     st.text(section2[1])
    #     st.text(section2[2])
    #
    # with col3:
    #     st.text(section3[0])
    #     st.text(section3[1])
    #     st.text(section3[2])
    #
    # with col4:
    #     st.text(section4[0])
    #     st.text(section4[1])
    #     st.text(section4[2])
    #     st.text(section4[3])
    #
    # with col5:
    #     for month in section5:
    #         st.text(month)