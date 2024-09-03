import streamlit as st

def show():

    st.write("#")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write("")

    with col2:

        st.markdown("""
            <p style='text-align: left; font:sans-serif; font-size: 38px; font-weight:bold;'>ข้อมูลชนิดงูไทย</p>""",unsafe_allow_html=True)


        st.markdown("---")
        st.markdown(
            """
            <style>
            .snake-title {
                font-size: 19.5px;
                font-weight: bold;
            }
            .snake-image-container {
                display: flex;
                justify-content: space-evenly;
                flex-wrap: wrap;
            }
            .snake-image {
                height: 200px; /* Set a fixed height */
                object-fit: cover; /* Scale image to fit the height, cropping if necessary */
                width: 100%;
            }
            .snake-description {
                font-size: 16px;
                text-indent: 40px; 
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        snake_info = {
            "pit viper งูเขียวหางไหม้ท้องเหลือง": "</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;มีรูปร่างโดยรวม คือ มีหัวยาวมนใหญ่เป็นรูปสามเหลี่ยม คอเล็ก ตัวอ้วนสั้น ปลายหางมีสีแดง ลำตัวมีสีเขียวอมเหลืองสด บางตัวมีสีเขียวอมน้ำเงิน หางสีแดงสด บางตัวมีหางสีแดงคล้ำเกือบเป็นสีน้ำตาล อันเป็นที่มาของชื่อ จัดเป็นงูพิษอ่อน ผิดไปจากงูสกุลหรือชนิดอื่นในวงศ์เดียวกัน โดยผู้ที่ถูกกัดจะไม่ถึงกับเสียชีวิต นอกจากเสียแต่ว่ามีโรคหรืออาการอื่นแทรกแซง</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;พบกระจายพันธุ์ทั่วไปในภูมิภาคเอเชียใต้และเอเชียตะวันออกเฉียงใต้ จนถึงหมู่เกาะแปซิฟิก พบประมาณ 35 ชนิดในประเทศไทย พบชุกชุมในภาคกลางและภาคตะวันออก",
            "King cobra งูจงอาง": "</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;งูจงอางเป็นงูพิษที่มีลักษณะหัวกลมมน เกล็ดบริเวณส่วนหัวใหญ่ มีเขี้ยว 2 เขี้ยวที่ขากรรไกรด้านบน หน้าตาดุดัน จมูกทู่ มองเผิน ๆ คล้ายกับงูสิงดง ที่บริเวณขอบตาบนมีเกล็ดยื่นงองุ้มออกมา ทำให้หน้าตาของงูจงอางมองดูดุและน่ากลัว ส่วนบริเวณท่อนหางจะมีลักษณะคล้ายคลึงกันมากที่สุด มีม่านตากลม ลำคอมีขนาดสมส่วน ลำตัวขนาดใหญ่เรียวยาว แผ่แม่เบี้ยได้เช่นเดียวกับงูเห่า</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;งูจงอางมีการกระจายพันธุ์ตลอดทั้งเอเชียใต้ เอเชียตะวันออกเฉียงใต้ และพื้นที่ทางตอนใต้ของเอเชียตะวันออก (ภาคใต้ของประเทศจีน) ที่ซึ่งพบเห็นได้ไม่บ่อยนัก งูจงอางเป็นงูป่าโดยกำเนิดอย่างแท้จริง โดยจะอยู่กันเป็นคู่ อาศัยอยู่ในระดับสูงกว่าน้ำทะเลได้ถึง 2,000 เมตร บนภูเขาหรือในป่าไม้ งูจงอางจะอาศัยอยู่ในแหล่งน้ำลำธาร ตามบริเวณซอกหินหรือในโพรงไม้ หรือในป่าไผ่ทึบที่มีไผ่ต้นเตี้ย ๆ จำนวนมาก รวมทั้งในบริเวณป่าไม้ที่มีความชื้นแฉะที่มีความอบอุ่น"
        }

        snake_images = {
            "pit viper งูเขียวหางไหม้ท้องเหลือง": ["snakeimage/งูเขียวหางไหม้1.jpg","snakeimage/งูเขียวหางไหม้2.jpg", "snakeimage/งูเขียวหางไหม้3.jpg"],"King cobra งูจงอาง" : ["snakeimage/งูจงอาง1.jpg","snakeimage/งูจงอาง2.jpg","snakeimage/งูจงอาง3.jpg"]
        }

        image_width = 250   

        for snake, description in snake_info.items():
            st.markdown(f'<div class="snake-title">{snake}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="snake-description">{description}</div>', unsafe_allow_html=True)
            st.markdown("---")

            image_columns = st.columns(3)
            for i, col in enumerate(image_columns):
                if i < len(snake_images[snake]):  #original: width=image_width
                    col.image(snake_images[snake][i], use_column_width="always",)
            st.markdown("---")
            st.write("")


    with col3:
        st.write("")


if __name__ == "__main__":
    show()
