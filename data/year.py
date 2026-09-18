import pandas as pd
import streamlit as st

df_year = pd.read_csv("./data/team_record.csv")
df_year["승률"] = (
    df_year["승"] / df_year["일반 경기"] * 100).round(1)

# 전체 기간
def year():

    st.title("FC 하이브리드")

    played, percentage = st.columns(2)

    with played:
        with st.container(border=True):
            st.metric(
                label="모든 경기",
                value=df_year["일반 경기"].sum()
            )
    with percentage:
        with st.container(border=True):
            st.metric(
                label="승률",
                value=f'{df_year.loc[df_year["시즌"] == 2023, "승률"].item()}%'
            )

    win_kpi, draw_kpi, lose_kpi = st.columns(3)

    with win_kpi:
        with st.container(border=True):
            st.metric(
                label="승",
                value=df_year["승"].sum()
            )
    with draw_kpi:
        with st.container(border=True):
            st.metric(
                label="무",
                value=df_year["무"].sum()
            )
    with lose_kpi:
        with st.container(border=True):
            st.metric(
                label="패",
                value=df_year["패"].sum()
            )


# 2022
def year_2022():

    st.title("2022년")

    played, percentage = st.columns(2)

    with played:
        with st.container(border=True):
            st.metric(
                label="모든 경기",
                value=df_year.loc[df_year["시즌"] == 2022, "일반 경기"].iloc[0]
            )
    with percentage:
        with st.container(border=True):
            st.metric(
                label="승률",
                value=f'{df_year.loc[df_year["시즌"] == 2022, "승률"].item()}%'
            )


    win_kpi, draw_kpi, lose_kpi = st.columns(3)

    with win_kpi:
        with st.container(border=True):
            st.metric(
                label="승",
                value=df_year.loc[df_year["시즌"] == 2022, "승"].item()
            )
    with draw_kpi:
        with st.container(border=True):
            st.metric(
                label="무",
                value=df_year.loc[df_year["시즌"] == 2022, "무"].item()
            )
    with lose_kpi:
        with st.container(border=True):
            st.metric(
                label="패",
                value=df_year.loc[df_year["시즌"] == 2022, "패"].item()
            )
 # 2023
def year_2023():

    st.title("2023년")

    played, percentage = st.columns(2)

    with played:
        with st.container(border=True):
            st.metric(
                label="모든 경기",
                value=df_year.loc[df_year["시즌"] == 2023, "일반 경기"].iloc[0]
            )
    with percentage:
        with st.container(border=True):
            st.metric(
                label="승률",
                value=f'{df_year.loc[df_year["시즌"] == 2023, "승률"].item()}%'
            )


    win_kpi, draw_kpi, lose_kpi = st.columns(3)

    with win_kpi:
        with st.container(border=True):
            st.metric(
                label="승",
                value=df_year.loc[df_year["시즌"] == 2023, "승"].item()
            )
    with draw_kpi:
        with st.container(border=True):
            st.metric(
                label="무",
                value=df_year.loc[df_year["시즌"] == 2023, "무"].item()
            )
    with lose_kpi:
        with st.container(border=True):
            st.metric(
                label="패",
                value=df_year.loc[df_year["시즌"] == 2023, "패"].item()
            )
 # 2024
def year_2024():

    st.title("2024년")

    played, percentage = st.columns(2)

    with played:
        with st.container(border=True):
            st.metric(
                label="모든 경기",
                value=df_year.loc[df_year["시즌"] == 2024, "일반 경기"].iloc[0]
            )
    with percentage:
        with st.container(border=True):
            st.metric(
                label="승률",
                value=f'{df_year.loc[df_year["시즌"] == 2024, "승률"].item()}%'
            )

    win_kpi, draw_kpi, lose_kpi = st.columns(3)

    with win_kpi:
        with st.container(border=True):
            st.metric(
                label="승",
                value=df_year.loc[df_year["시즌"] == 2024, "승"].item()
            )
    with draw_kpi:
        with st.container(border=True):
            st.metric(
                label="무",
                value=df_year.loc[df_year["시즌"] == 2024, "무"].item()
            )
    with lose_kpi:
        with st.container(border=True):
            st.metric(
                label="패",
                value=df_year.loc[df_year["시즌"] == 2024, "패"].item()
            )

 # 2025
def year_2025():

    st.title("2025년")

    played, percentage = st.columns(2)

    with played:
        with st.container(border=True):
            st.metric(
                label="모든 경기",
                value=df_year.loc[df_year["시즌"] == 2025, "일반 경기"].iloc[0]
            )
    with percentage:
        with st.container(border=True):
            st.metric(
                label="승률",
                value=f'{df_year.loc[df_year["시즌"] == 2025, "승률"].item()}%'
            )

    win_kpi, draw_kpi, lose_kpi = st.columns(3)

    with win_kpi:
        with st.container(border=True):
            st.metric(
                label="승",
                value=df_year.loc[df_year["시즌"] == 2025, "승"].item()
            )
    with draw_kpi:
        with st.container(border=True):
            st.metric(
                label="무",
                value=df_year.loc[df_year["시즌"] == 2025, "무"].item()
            )
    with lose_kpi:
        with st.container(border=True):
            st.metric(
                label="패",
                value=df_year.loc[df_year["시즌"] == 2025, "패"].item()
            )
 # 2026
def year_2026():

    st.title("2026년")

    played, percentage = st.columns(2)

    with played:
        with st.container(border=True):
            st.metric(
                label="모든 경기",
                value=df_year.loc[df_year["시즌"] == 2026, "일반 경기"].iloc[0]
            )
    with percentage:
        with st.container(border=True):
            st.metric(
                label="승률",
                value=f'{df_year.loc[df_year["시즌"] == 2026, "승률"].item()}%'
            )

    win_kpi, draw_kpi, lose_kpi = st.columns(3)

    with win_kpi:
        with st.container(border=True):
            st.metric(
                label="승",
                value=df_year.loc[df_year["시즌"] == 2026, "승"].item()
            )
    with draw_kpi:
        with st.container(border=True):
            st.metric(
                label="무",
                value=df_year.loc[df_year["시즌"] == 2026, "무"].item()
            )
    with lose_kpi:
        with st.container(border=True):
            st.metric(
                label="패",
                value=df_year.loc[df_year["시즌"] == 2026, "패"].item()
            )

