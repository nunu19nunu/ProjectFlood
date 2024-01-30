import streamlit as st
import joblib
import pandas as pd

model = joblib.load('randomforestv2.pkl')  # Load your model file

selected_columns = {'flooding' :'น้ำท่วมขัง', 'overflow':'น้ำล้นตลิ่ง', 'flashflood':'น้ำท่วมฉับพลัน', 'feq2':'2 ปีครั้ง', 'feq3':'3 ปีครั้ง', 'feq4':'4 ปีครั้ง', 'house':'น้ำท่วมแต่ไม่ท่วมบ้าน',
                    'habitable':'น้ำท่วมบางส่วนแต่อาศัยได้', 'evacuated':'น้ำท่วมบ้านต้องอพยพ', 'transportation':'เส้นทางคมนาคม', 'benefit':'สาธารณประโยชน์', 'area':'พื้นที่การเกษตร', 'fishing':'การประมง', 'Jan':'มกราคม', 'Feb':'กุมภาพันธ์', 'Mar':'มีนาคม',
                    'Apr':'เมษายน', 'May':'พฤษภาคม', 'Jun':'มิถุนายน', 'Jul':'กรกฎาคม', 'Aug':'สิงหาคม', 'Sep':'กันยายน', 'Oct':'ตุลาคม', 'Nov':'พฤศจิกายน', 'Dec':'ธันวาคม'}

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


def main():
    st.title("โปรแกรมทำนายอุทกภัยในภาคใต้ :rain_cloud::lightning_cloud:")

    st.caption("อ้างอิงข้อมูล: กรมป้องกันและบรรเทาสาธารณภัย")

    input_features = {}

    # User input
    province_input = st.selectbox("กรุณาเลือกจังหวัด:", ["เลือกจังหวัด"] + list(province_mapping.values()))
    input_features['province'] = get_key_by_value(province_mapping, province_input)



    binary_labels = {
        1: "เคยเกิดขึ้น",
        0: "ไม่เคยเกิดขึ้น"
    }

    st.subheader("ประเภทในการเกิดอุทกภัย", divider='rainbow')
    for column in selected_columns:
        if selected_columns[column] in ['น้ำท่วมขัง', 'น้ำล้นตลิ่ง', 'น้ำท่วมฉับพลัน']:

            option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()), index=None, key=column)
            input_features[column] = get_key_by_value(binary_labels, option_input)
            if selected_columns[column] == "น้ำท่วมฉับพลัน":
                st.subheader("ความถี่ในการเกิดอุทกภัย", divider='rainbow')


        if selected_columns[column] in ["2 ปีครั้ง","3 ปีครั้ง", "4 ปีครั้ง"]:
            option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()), index=None, key=column)
            input_features[column] = get_key_by_value(binary_labels, option_input)
            if selected_columns[column] == "4 ปีครั้ง":
                st.subheader("ความรุนแรงในการเกิดอุทกภัย", divider='rainbow')

        elif selected_columns[column] in ["น้ำท่วมแต่ไม่ท่วมบ้าน","น้ำท่วมบางส่วนแต่อาศัยได้", "น้ำท่วมบ้านต้องอพยพ"]:
            option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()), index=None, key=column)
            input_features[column] = get_key_by_value(binary_labels, option_input)
            if selected_columns[column] == "น้ำท่วมบ้านต้องอพยพ":
                st.subheader("ผลกระทบในการเกิดอุทกภัย", divider='rainbow')

        elif selected_columns[column] in ["เส้นทางคมนาคม",'สาธารณประโยชน์', 'พื้นที่การเกษตร','การประมง']:
            option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()), index=None, key=column)
            input_features[column] = get_key_by_value(binary_labels, option_input)
            if selected_columns[column] == "การประมง":
                st.subheader("เดือนที่เคยเกิดอุทกภัย", divider='rainbow')


            col1, col2, col3 = st.columns(3)
        elif selected_columns[column] in ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน"]:
            with col1:
                option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()), index=None,
                                        key=column)
                input_features[column] = get_key_by_value(binary_labels, option_input)

        elif selected_columns[column] in ["พฤษภาคม","มิถุนายน", "กรกฎาคม", "สิงหาคม"]:
            with col2:
                option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()), index=None,
                                        key=column)
                input_features[column] = get_key_by_value(binary_labels, option_input)

        elif selected_columns[column] in ["กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]:

            with col3:
                option_input = st.radio(f'{selected_columns[column]}', list(binary_labels.values()), index=None,
                                        key=column)
                input_features[column] = get_key_by_value(binary_labels, option_input)

    if st.button("ทำนายความเสี่ยง"):
        check = True
        # Display result
        if province_input == "เลือกจังหวัด":
            st.warning("กรุณาเลือกจังหวัด")
        elif check == False:
            st.warning("กรุณาเลือกข้อมูลให้ครบถ้วน")
        else:
            input_data = pd.DataFrame([input_features])
            result = predict_province_result(input_data)
            st.markdown(f"{province_input}: **ความเสี่ยงเกิดน้ำท่วมระดับ {result}**")
            # st.markdown(f"ติดตามสอบถามข้อมูลหรือวิธีการป้องกันอุทกภัยเพิ่มเติมได้ที่ {link_mapping})")

        province_code = get_key_by_value(province_mapping, province_input)
        if province_code in link_mapping:
            link = link_mapping[province_code]
            st.markdown(f'''**ติดตามสอบถามข้อมูลหรือวิธีการป้องกันอุทกภัยเพิ่มเติมได้ที่** :
                        \n[กรมป้องกันและบรรเทาสาธารณภัยจังหวัด{province_input}]({link})
                        \n **สายด่วนตลอด 24 ชั่วโมง 📞1784🚨**''')
        else:
            st.warning("ไม่พบข้อมูลเพิ่มเติมสำหรับจังหวัดนี้")

if __name__ == '__main__':
    main()
