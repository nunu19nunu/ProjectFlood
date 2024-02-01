import streamlit as st
import joblib
import pandas as pd

model = joblib.load('randomforestv2.pkl')  # Load your model file

selected_columns = {'flooding': 'น้ำท่วมขัง', 'overflow': 'น้ำล้นตลิ่ง', 'flashflood': 'น้ำท่วมฉับพลัน',
                    'feq2': '2 ปีครั้ง', 'feq3': '3 ปีครั้ง', 'feq4': '4 ปีครั้ง', 'house': 'น้ำท่วมแต่ไม่ท่วมบ้าน',
                    'habitable': 'น้ำท่วมบางส่วนแต่อาศัยได้', 'evacuated': 'น้ำท่วมบ้านต้องอพยพ',
                    'transportation': 'เส้นทางคมนาคม', 'benefit': 'สาธารณประโยชน์', 'area': 'พื้นที่การเกษตร',
                    'fishing': 'การประมง', 'Jan': 'มกราคม', 'Feb': 'กุมภาพันธ์', 'Mar': 'มีนาคม',
                    'Apr': 'เมษายน', 'May': 'พฤษภาคม', 'Jun': 'มิถุนายน', 'Jul': 'กรกฎาคม', 'Aug': 'สิงหาคม',
                    'Sep': 'กันยายน', 'Oct': 'ตุลาคม', 'Nov': 'พฤศจิกายน', 'Dec': 'ธันวาคม'}

link_mapping = {
    1: "https://kbi.disaster.go.th/krabi/home",
    2: "https://cpn.disaster.go.th/CPN/home",
    3: "https://trg.disaster.go.th/TRANG/home",
    4: "https://nrt.disaster.go.th/nst/home",
    5: "https://nrt.disaster.go.th/nst/home",
    6: "https://ptn.disaster.go.th/ptn/home",
    7: "https://pna.disaster.go.th/png/home",
    8: "https://plg.disaster.go.th/plg/home",
    9: "https://pkt.disaster.go.th/pkt/home",
    10: "https://yla.disaster.go.th/yala/home",
    11: "https://rng.disaster.go.th/RANONG/home",
    12: "https://ska.disaster.go.th/dpmsk/home",
    13: "https://stn.disaster.go.th/satun/home",
    14: "https://sni.disaster.go.th/SNI/home"

}
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


# background = '''
# <style>
#   [data-testid = "stAppViewContainer"] {
#   background-image: url("https://www.matichon.co.th/wp-content/uploads/2017/01/%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%88%E0%B8%A7%E0%B8%9A1.jpg");
#   background-size : cover;
# </style>
#
# '''
# st.markdown(background, unsafe_allow_html=True)

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # If the value is not found


def predict_province_result(input_data):
    prediction = model.predict(input_data)
    predicted_class = prediction[0]

    risk_level_labels = {
        1: 'ต่ำมากหรืออาจจะไม่เกิดขึ้นเลย ',
        2: 'ต่ำ ',
        3: 'ปานกลาง ',
        4: 'สูง! ',
        5: 'สูงมาก!! '
    }
    predicted_risk_level = risk_level_labels[predicted_class]

    return predicted_risk_level





def isHaveNone(input_features):
    for column in selected_columns:
        print(input_features[column])
        if input_features[column] is None:
            print("eiei")
            return True
    return False


def main():
    st.title("โปรแกรมทำนายอุทกภัยในภาคใต้ :rain_cloud::lightning_cloud:")

    st.caption("อ้างอิงข้อมูล: กรมป้องกันและบรรเทาสาธารณภัย")

    # เก็บค่าที่user ทำการ input
    input_features = {}

    # User input
    province_input = st.selectbox("กรุณาเลือกจังหวัด:", ["เลือกจังหวัด"] + list(province_mapping.values()))
    input_features['province'] = get_key_by_value(province_mapping, province_input)

    binary_labels = {
        1: "เคยเกิดขึ้น",
        0: "ไม่เคยเกิดขึ้น"
    }

    st.subheader("ประเภทในการเกิดอุทกภัย", divider='rainbow')
    select_all_checkbox1 = st.checkbox('เคยเกิดขึ้นทั้งหมด', key="select_all_checkbox1")
    for column in selected_columns:
        if selected_columns[column] in ['น้ำท่วมขัง', 'น้ำล้นตลิ่ง', 'น้ำท่วมฉับพลัน']:

            if select_all_checkbox1:
                selected_value1 = "เคยเกิดขึ้น"
            else:
                selected_value1 = None
            option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()),
                                    index=None if selected_value1 is None else 0, key=column)
            input_features[column] = get_key_by_value(binary_labels, option_input)
            if selected_columns[column] == "น้ำท่วมฉับพลัน":
                st.subheader("ความถี่ในการเกิดอุทกภัย", divider='rainbow')
                select_all_checkbox2 = st.checkbox('เคยเกิดขึ้นทั้งหมด', key="select_all_checkbox2")

        if selected_columns[column] in ["2 ปีครั้ง", "3 ปีครั้ง", "4 ปีครั้ง"]:

            if select_all_checkbox2:
                selected_value2 = "เคยเกิดขึ้น"
            else:
                selected_value2 = None
            option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()),
                                    index=None if selected_value2 is None else 0, key=column)
            input_features[column] = get_key_by_value(binary_labels, option_input)
            if selected_columns[column] == "4 ปีครั้ง":
                st.subheader("ความรุนแรงในการเกิดอุทกภัย", divider='rainbow')
                select_all_checkbox3 = st.checkbox('เคยเกิดขึ้นทั้งหมด', key="select_all_checkbox3")

        elif selected_columns[column] in ["น้ำท่วมแต่ไม่ท่วมบ้าน", "น้ำท่วมบางส่วนแต่อาศัยได้", "น้ำท่วมบ้านต้องอพยพ"]:
            if select_all_checkbox3:
                selected_value3 = "เคยเกิดขึ้น"
            else:
                selected_value3 = None
            option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()),
                                    index=None if selected_value3 is None else 0, key=column)
            input_features[column] = get_key_by_value(binary_labels, option_input)
            if selected_columns[column] == "น้ำท่วมบ้านต้องอพยพ":
                st.subheader("ผลกระทบในการเกิดอุทกภัย", divider='rainbow')
                select_all_checkbox4 = st.checkbox('เคยเกิดขึ้นทั้งหมด', key="select_all_checkbox4")

        elif selected_columns[column] in ["เส้นทางคมนาคม", 'สาธารณประโยชน์', 'พื้นที่การเกษตร', 'การประมง']:
            if select_all_checkbox4:
                selected_value4 = "เคยเกิดขึ้น"
            else:
                selected_value4 = None
            option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()),
                                    index=None if selected_value4 is None else 0, key=column)
            input_features[column] = get_key_by_value(binary_labels, option_input)
            if selected_columns[column] == "การประมง":
                st.subheader("เดือนที่เคยเกิดอุทกภัย", divider='rainbow')
                select_all_checkbox5 = st.checkbox('เคยเกิดขึ้นทั้งหมด', key="select_all_checkbox5")

            col1, col2, col3 = st.columns(3)
        elif selected_columns[column] in ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน"]:
            if select_all_checkbox5:
                selected_value5 = "เคยเกิดขึ้น"
            else:
                selected_value5 = None
            with col1:
                option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()),
                                        index=None if selected_value5 is None else 0,
                                        key=column)
                input_features[column] = get_key_by_value(binary_labels, option_input)

        elif selected_columns[column] in ["พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม"]:
            with col2:
                option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()),
                                        index=None if selected_value5 is None else 0,
                                        key=column)
                input_features[column] = get_key_by_value(binary_labels, option_input)

        elif selected_columns[column] in ["กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]:

            with col3:
                option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()),
                                        index=None if selected_value5 is None else 0,
                                        key=column)
                input_features[column] = get_key_by_value(binary_labels, option_input)

    if st.button("ทำนายความเสี่ยง"):
        isNone = isHaveNone(input_features)
        # Display result
        if province_input == "เลือกจังหวัด":
            st.warning("กรุณาเลือกจังหวัด")
        elif isNone == True:
            st.warning("กรุณาเลือกข้อมูลให้ครบถ้วน")
        else:
            input_data = pd.DataFrame([input_features])
            result = predict_province_result(input_data)
            st.markdown(f"<h2>{province_input}: ความเสี่ยงเกิดน้ำท่วมระดับ {result}<h/2>", unsafe_allow_html=True)
            if result == 'สูงมาก!! ':
                st.markdown(
                    '<p style="font-size:20px;"> หมายถึง ความเสี่ยงที่ทำให้เกิดผลกระทบร้ายแรงมาก ต้องวางแผนและดำเนินการป้องกันอย่างด่วนที่สุด</p>',
                    unsafe_allow_html=True)
            elif result == 'สูง':
                st.markdown(
                    '<p style="font-size:20px;"> หมายถึง ความเสี่ยงที่ทำให้เกิดความรุนแรงและก่อให้เกิดผลกระทบ ยังไม่จำเป็นต้องป้องกันทันที แต่ต้องมีการวางแผนและเตรียมการสำหรับอนาคตอันใกล้</p>',
                    unsafe_allow_html=True)
            elif result == 'ปานกลาง ':
                st.markdown(
                    '<p style="font-size:20px;"> หมายถึง ความเสี่ยงที่ทำให้เกิดความรุนแรงยังไม่มากแต่อาจจะก่อให้เกิดผลกระทบพอสมควร การป้องกันยังไม่ต้องเร่งด่วน และอาจจำเป็นหรือไม่จำเป็นที่ต้องเตรียมการป้องกัน ขึ้นอยู่กับสถานการณ์ ณ เวลานั้น</p>',
                    unsafe_allow_html=True)
            elif result == 'ต่ำ':
                st.markdown(
                    '<p style="font-size:20px;"> หมายถึง ความเสี่ยงต่ำที่มีผลกระทบที่น้อยและไม่รุนแรง อาจจะไม่ต้องดำเนินการป้องกันหรืออะไรเป็นพิเศษ</p>',
                    unsafe_allow_html=True)
            else:
                st.markdown(
                    '<p style="font-size:20px;"> หมายถึง ความเสี่ยงที่แทบไม่มีโอกาสในการเกิดอุทกภัย ถ้าเกิดก็จะมีผลกระทบที่ไม่รุนแรงเลยหรือมีผลกระทบน้อยมาก ไม่จำเป็นต้องดำเนินการอะไรเลย</p>',
                    unsafe_allow_html=True)

        province_code = get_key_by_value(province_mapping, province_input)
        if province_code in link_mapping:
            link = link_mapping[province_code]
            st.markdown(f'''**ติดตามสอบถามข้อมูลหรือวิธีการป้องกันอุทกภัยเพิ่มเติมได้ที่** :
                        \n[กรมป้องกันและบรรเทาสาธารณภัยจังหวัด{province_input}]({link})
                        \n**สายด่วนตลอด 24 ชั่วโมง 📞1784🚨**''')
        else:
            st.warning("ไม่พบข้อมูลเพิ่มเติมสำหรับจังหวัดนี้")


if __name__ == '__main__':
    main()
