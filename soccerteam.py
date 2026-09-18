import pandas as pd
import streamlit as st

from data.year import year, year_2022, year_2023, year_2024, year_2025, year_2026
from data.player1 import player_1, player_2, player_3
from data.player2 import player_4, player_5

df_year = pd.read_csv("./data/team_record.csv")


st.set_page_config(
    page_title="FC하이브리드",
    layout="centered",
    initial_sidebar_state="expanded",
    page_icon="⚽"
)

# 사이드바
with st.sidebar:

    page = st.radio(
        "페이지 선택",
        ["팀기록", "선수기록"],
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] [data-testid="stRadio"] label p {
            font-size: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 팀기록을 선택했을 때만 팀 연도 표시
    if page == "팀기록":

        selected_year = st.radio(
            "연도를 눌려주세요",
            [
                "전체",
                "2022",
                "2023",
                "2024",
                "2025",
                "2026",
            ]
        )


    # 선수기록을 선택했을 때만 선수 목록 표시
    if page == "선수기록":

        selected_player = st.radio(
            "선수를 선택해주세요",
            [
                "권혁준",
                "김진섭",
                "김태균",
                "김현진",
                "윤재민",
            ]
        )


# year.py (팀기록 화면)
if page == "팀기록":

    if selected_year == "전체":
        year()

    elif selected_year == "2022":
        year_2022()

    elif selected_year == "2023":
        year_2023()

    elif selected_year == "2024":
        year_2024()

    elif selected_year == "2025":
        year_2025()

    elif selected_year == "2026":
        year_2026()




# 선수기록 화면
elif page == "선수기록":

    if selected_player == "권혁준":
        player_1()

    elif selected_player == "김진섭":
        player_2()

    elif selected_player == "김태균":
        player_3()

    elif selected_player == "김현진":
        player_4()

    elif selected_player == "윤재민":
        player_5()