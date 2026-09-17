import pandas as pd
import streamlit as st


# 전체 기간
def year():

    st.title("FC 하이브리드")

    with st.container(border=True):
        st.metric(
            label="모든 경기",
            value=172
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


# 2022
def year_2022():

    st.title("2022년")

    with st.container(border=True):
        st.metric(
            label="모든 경기",
            value=31
        )

    win_kpi, draw_kpi, lose_kpi = st.columns(3)

    with win_kpi:
        with st.container(border=True):
            st.metric(
                label="승",
                value=17
            )
    with draw_kpi:
        with st.container(border=True):
            st.metric(
                label="무",
                value=2
            )
    with lose_kpi:
        with st.container(border=True):
            st.metric(
                label="패",
                value=10
            )
 # 2023
def year_2023():

    st.title("2023년")

    with st.container(border=True):
        st.metric(
            label="모든 경기",
            value=40
        )

    win_kpi, draw_kpi, lose_kpi = st.columns(3)

    with win_kpi:
        with st.container(border=True):
            st.metric(
                label="승",
                value=29
            )
    with draw_kpi:
        with st.container(border=True):
            st.metric(
                label="무",
                value=4
            )
    with lose_kpi:
        with st.container(border=True):
            st.metric(
                label="패",
                value=6
            )
 # 2024
def year_2024():

    st.title("2024년")

    with st.container(border=True):
        st.metric(
            label="모든 경기",
            value=40
        )

    win_kpi, draw_kpi, lose_kpi = st.columns(3)

    with win_kpi:
        with st.container(border=True):
            st.metric(
                label="승",
                value=23
            )
    with draw_kpi:
        with st.container(border=True):
            st.metric(
                label="무",
                value=2
            )
    with lose_kpi:
        with st.container(border=True):
            st.metric(
                label="패",
                value=13
            )
 # 2025
def year_2025():

    st.title("2025년")

    with st.container(border=True):
        st.metric(
            label="모든 경기",
            value=35
        )

    win_kpi, draw_kpi, lose_kpi = st.columns(3)

    with win_kpi:
        with st.container(border=True):
            st.metric(
                label="승",
                value=15
            )
    with draw_kpi:
        with st.container(border=True):
            st.metric(
                label="무",
                value=8
            )
    with lose_kpi:
        with st.container(border=True):
            st.metric(
                label="패",
                value=12
            )
 # 2026
def year_2026():

    st.title("2026년")

    with st.container(border=True):
        st.metric(
            label="모든 경기",
            value=26
        )

    win_kpi, draw_kpi, lose_kpi = st.columns(3)

    with win_kpi:
        with st.container(border=True):
            st.metric(
                label="승",
                value=15
            )
    with draw_kpi:
        with st.container(border=True):
            st.metric(
                label="무",
                value=4
            )
    with lose_kpi:
        with st.container(border=True):
            st.metric(
                label="패",
                value=6
            )
