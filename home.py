import streamlit as st
import streamlit.components.v1 as components



def show():

    
    st.write("#")

    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        st.write("")

    with col2:
        st.markdown("<p style='text-align: right; font-size: 48px; font-weight:bold;'>ยินดีต้อนรับสู่ <span style= color:#06402B; font-style:italic;>Snakies</span></p>", unsafe_allow_html=True)

        col4, col5, col6 = st.columns([2,3,2])

        with col4:
            st.write("")

        with col5:
            st.image("images/Snakeimage2vector.svg")

        with col6:
            st.write("")


       
        st.markdown("""
        <style>
            .custom-text {
                line-height: 1.5; 
                font-size: 19.5px;  
            }
            .custom-text span {
                color: #06402B;
                font-weight: bold;
            }
            .custom-text green {
                color: #06402B;
            }
            .custom-text strong {
                font-weight: bold;
            }
            .custom-text line {
                text-decoration: underline; 
            }
            .custom-text strongnline {
                font-weight: bold;
                text-decoration: underline;   
            }
            .custom-text mission {
                font-size: 30px;
            }d
            .custom-text redirect {
                font-size: 22px;
            }
            .small-text {
                line-height: 1.6;
                font-size: 17.2px;   
            }
        </style>
        <p class="custom-text">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       <span>SNAKIES (สเน็กกี้ส์)</span> -พวกเรามีความตั้งใจที่จะพัฒนาความปลอดภัยของทุกคน โดยใช้ SNAKIES สำหรับจำแนกชนิดของงูและ แจ้งให้ทุกคนทราบว่างูที่ท่านสนใจเป็นชนิดไหน และมีอันตรายต่อมนุษย์หรือไม่ มากไปกว่านั้น ยังช่วยลดระยะเวลาในการรักษาตัวจากการถูกงูกัด เนื่องจากสามารถวินิจฉัยความอันตรายได้จากชนิดของงูได้อย่างทันท่วงที และให้ข้อมูลของงูชนิดต่าง ๆ แก่ผู้ที่สนใจพวกเราหวังว่าเว็บไซต์ของเราจะสามารถอำนวยความสะดวกและเป็นประโยชน์ต่อผู้ใช้ทุกคน
        </p>
        <br>

        """, unsafe_allow_html=True)
        st.markdown("""
        <p style='text-align: left; font-size: 25px; font-weight:bold;'>
        ทดลองใช้ บริการเพียง กดไปที่หน้า <span style= color:#06402B; >Snakies</span> page
        </p><br><br>
        """, unsafe_allow_html=True)


        # Insert the SVG image here using st.image
        st.markdown("""
            <p class="custom-text"> 
                <mission><strong><green>ภารกิจของพวกเรา</green></strong></mission>
                :<br>
                1) เพื่อเพิ่มประสิทธิภาพในการรักษาตัวจากการถูกงูกัด<br>
                2) เพื่อสร้างความรู้ความเข้าใจในด้านต่างๆของงูแต่ละชนิด<br>
                3) เพื่อพัฒนาการเข้าถึงข้อมูลของสัตว์ในธรรมชาติที่พบได้ทั่วไป
            </p>
        """, unsafe_allow_html=True)

        #with col11:
           # st.image("assets/model3d.jpg")



        #st.button("Try Our App",type="primary",on_click= switch_page('TumorVision')) //this no work

        st.markdown("<p style='text-align: center; font-size: 30px; font-weight:bold; text-decoration: underline;'>จุดเด่นของเรา</p>", unsafe_allow_html=True)

        st.markdown("""
        <style>
        .flex-container {
            display: flex;
            justify-content: space-evenly;
            gap: 0px;
        }

        .custom-box {
            border: 2px solid #06402B;
            border-radius: 18px;
            padding: 20px;
            background-color: #f9f9f9;
            height: 300px; /* Adjust the height as needed */
            width: 250px; /* Adjust the width as needed */
            display: flex;
            align-items: center;
            justify-content: space-evenly;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .custom-box p {
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: #06402B;
            margin: 0;
        }
        </style>
        """, unsafe_allow_html=True)

        col7, col8, col9= st.columns([1, 1, 1], gap="medium")
        with col7:
            st.markdown("""
                <div class="flex-container">
                    <div class="custom-box">
                        <p>นำเทคโนโลยีปัญญาประดิษย์เข้ามามีส่วนร่วม</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        with col8:
            st.markdown("""
                <div class="flex-container">
                    <div class="custom-box">
                        <p>วิเคราะห์ชนิดงูไทยได้อย่างแม่นยำมีความแม่นยำ</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        with col9:
            st.markdown("""
                <div class="flex-container">
                    <div class="custom-box">
                        <p>เป็นมิตรต่อผู้ใช้ เพียงแค่อัพโหลดรูปและรอผล</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

       
        #st.info("This is the Home page demo. You can customize this content with more information about your project.")

    with col3:
        st.write("")


if __name__ == "__main__":
    show()
