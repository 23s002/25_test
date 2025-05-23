import streamlit as st

# MBTI별 추천 직업 데이터
mbti_jobs = {
    "INTJ": ["🔬 데이터 과학자", "📊 전략 기획자", "💡 UX 디자이너"],
    "INFP": ["🎨 작가", "🎼 음악가", "💬 심리상담사"],
    "ENTP": ["📢 마케팅 전문가", "💼 창업가", "🎤 발표자"],
    "ESFJ": ["👩‍🏫 교사", "👩‍⚕️ 간호사", "🧑‍🍳 요리사"],
    "ISTP": ["🛠 기계 엔지니어", "🚓 경찰관", "💻 백엔드 개발자"],
    "ENFP": ["🎭 배우", "🌍 여행 기획자", "🧠 창의 워크숍 퍼실리테이터"],
    # 필요한 MBTI 유형 모두 추가 가능
}

# 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 직업 추천기 🔮",
    page_icon="🧠",
    layout="centered"
)

# 타이틀 영역
st.title("🧠 MBTI로 알아보는 직업 추천 💼")
st.markdown("당신의 **MBTI 유형**을 선택하면, 성격에 맞는 멋진 직업을 추천해드릴게요! 🚀")

# 사이드바
st.sidebar.title("🌈 메뉴")
st.sidebar.markdown("➡️ [MBTI 검사하러 가기](https://www.16personalities.com/ko)")

# MBTI 선택
selected_mbti = st.selectbox("🔍 나의 MBTI는?", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 유형을 위한 직업 추천")
    jobs = mbti_jobs.get(selected_mbti, [])
    for job in jobs:
        st.success(f"✅ {job}")

    st.markdown("---")
    st.info("※ 이 결과는 참고용으로 활용하세요. 진로는 스스로의 흥미와 역량을 반영해 결정하는 것이 가장 중요합니다. 🌱")

# 푸터
st.markdown("---")
st.caption("📌 제작자: 홍길동 | 2025 © CareerMatch AI")

