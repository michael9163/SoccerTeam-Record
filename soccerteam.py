import pandas as pd
import streamlit as st

from player_record.player1 import player_1, player_2, player_3
from player_record.player2 import player_4, player_5


st.set_page_config(
    page_title="FC하이브리드",
    layout='centered',
    initial_sidebar_state="expanded",
    page_icon="⚽"
)


## 본문
st.title("FC 하이브리드")


with st.container():
    with st.container(border=True):
        st.metric(
            label="모든 경기",
            value=172,
        )

win_kpi, draw_kpi, lose_kpi = st.columns(3)

with win_kpi:
    with st.container(border=True):
        st.metric(
            label="승",
            value=99
        )
with draw_kpi:
    with st.container(border=True):
        st.metric(
            label="무",
            value=20
        )
with lose_kpi:
    with st.container(border=True):
        st.metric(
            label="패",
            value=47
        )



## 사이드바
with st.sidebar:

    st.title("팀기록")

    st.title("선수기록")


    menu = st.radio(
        "선수를 선택해주세요",
        [
            "권혁준",
            "김진섭",
            "김태균",
            "김현진",
            "윤재민",
         ]
    )

if menu == '권혁준':
    player_1()
elif menu == '김진섭':
    player_2()
elif menu == '김태균':
    player_3()
elif menu == '김현진':
    player_4()
elif menu == '윤재민':
    player_5()