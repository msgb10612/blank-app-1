import streamlit as st

# 스트림릿 앱 제목 설정
st.title("🍿 영화관 세트 메뉴 조합기")
st.subheader("선택 가능한 모든 메뉴 조합을 확인해보세요!")

# 원본 옵션 데이터 (오타 수정: } -> ])
popcorn_options = ["기본", "카라멜", "어니언"]
drink_options = ["생수", "탄산음료"]

# 시각적인 구분을 위한 선 추가
st.markdown("---")

# 원본 for문 루프 및 출력 로직 유지
for popcorn in popcorn_options:
    for drink in drink_options:
        # st.write를 사용하여 스트림릿 화면에 출력
        st.write(f"🎬 **세트메뉴:** {popcorn} 팝콘, {drink}")