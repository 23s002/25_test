import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="나의 소개 페이지",
    page_icon="👤",
    layout="centered"
)

# 사이드바 타이틀
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("현재 페이지: 소개")

# 메인 타이틀
st.title("👋 안녕하세요!")
st.markdown("아래는 저에 대한 간단한 소개입니다.")

# 프로필 사진
st.image("your_profile_image.jpg", width=200, caption="나의 사진")

# 소개 카드 스타일 박스
with st.container():
    st.subheader("🙋‍♂️ 기본 정보")
    st.write("""
    - **이름**: 홍길동  
    - **학교**: 한국대학교 컴퓨터공학과  
    - **취미**: 사진 찍기, 독서, 마라톤  
    - **이메일**: honggildong@example.com
    """)

# 추가 소개
st.subheader("💬 한 마디")
st.info("세상에 긍정적인 영향을 주는 개발자가 되는 것이 제 목표입니다!")

# 연락 버튼
st.subheader("📨 연락하기")
if st.button("이메일 보내기"):
    st.markdown("mailto:honggildong@example.com")

# 푸터
st.markdown("---")
st.markdown("© 2025 홍길동. All rights reserved.")
