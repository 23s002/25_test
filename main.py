import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="나의 소개 페이지",
    page_icon="👤",
    layout="centered"
)

# 사이드바
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("현재 위치: 소개 페이지")

# 메인 제목
st.title("👋 반갑습니다! 저는 홍길동입니다.")

# 간단 소개
st.markdown("""
안녕하세요! 저는 **영동일고등학교**에 재학 중인 학생입니다.  
다양한 기술을 배우고 사람들과 협업하는 걸 좋아합니다.
""")

# 정보 박스
with st.container():
    st.subheader("🧾 기본 정보")
    st.write("""
    - **이름**: 김윤준  
    - **학교**: 영동일고등학교  
    - **취미**: 잠
    - **이메일**: 23s002@ydi.hs.kr 
    """)

# 한 마디
st.subheader("💬 한 마디")
st.success("안녕하세요")

# 연락 버튼
st.subheader("📨 연락하기")
if st.button("이메일 보내기"):
    st.markdown("📧 이메일: [23s002@ydi.hs.kr](23s002@ydi.hs.kr)")

# 푸터
st.markdown("---")
st.caption("© 2025 홍길동. All rights reserved.")
