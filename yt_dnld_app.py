import streamlit as st
from yt_dnld import Downloader

st.set_page_config(page_title='My Tube',layout='wide')
st.markdown(f"""
    <style>
    .stApp {{background-image: url(https://img.freepik.com/free-photo/red-light-round-podium-black-background-mock-up_43614-950.jpg?w=740&t=st=1705394040~exp=1705394640~hmac=8f5842185c46b0b6cb9fc55af2708e2ce741cae56961a27b193bf14241099513); 
                background-attachment: fixed;
                background-size: cover}}
    </style>
    """, unsafe_allow_html=True)
url=st.text_input('Paste URL Here',placeholder='https://www.youtube.com/')
vi=Downloader(url)
if url:
    v_info= vi.video()
    col1, col2= st.columns([1,1.5], gap="small")
    with st.container():
        with col1:            
            st.image(v_info["image"])   
        with col2:
            st.subheader("Video Details ⚙️")
            res_inp = st.selectbox('__Select Resolution__', v_info["resolutions"])
            id = v_info["resolutions"].index(res_inp)            
            st.write(f"__Title:__ {v_info['title']}")
            st.write(f"__Length:__ {v_info['length']} sec")
            st.write(f"__Resolution:__ {v_info['resolutions'][id]}")
            st.write(f"__Frame Rate:__ {v_info['fps'][id]}")
            st.write(f"__Format:__ {v_info['format'][id]}")
            file_name = st.text_input('__Save as 🎯__', placeholder = v_info['title'])
            if file_name:        
                if file_name != v_info['title']:
                    file_name+=".mp4"
            else:
                file_name = v_info['title'] + ".mp4"

        button = st.button("Download ⚡️")
        if button:
            with st.spinner('Downloading...'):
                try:
                    ds = v_info["streams"].get_by_itag(v_info['itag'][id])
                    ds.download(filename= file_name, output_path= "downloads/")
                    st.success('Download Complete', icon="✅")       
                    st.balloons()
                except:
                    st.error('Error: Save with a different name!', icon="🚨")

au_button=st.button('Only MP3')
if au_button:
    au=vi.audio()
    try:
        au.download(output_path='MP3_downloads/')
        st.success('Download Complete', icon="✅")       
        st.balloons()
    except:
        st.error('Error: Save with a different name!', icon="🚨")

          