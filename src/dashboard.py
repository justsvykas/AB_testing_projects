import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


def configure_page() -> None:
    st.set_page_config(page_title="Dashboard for marketing campaign", layout="centered")


def load_data() -> pd.DataFrame:
    data_path = "src/marketing_campaign/data/raw_market_campaign.csv"
    return pd.read_csv(data_path)


def configure_overview() -> None:
    st.markdown("# Marketing Campaign Dashboard")
    st.markdown("This app generates dashboard to view sales as weeks progress")
    st.markdown("The aim is to have easily accessable dashboard of main metrics")


def plot_sales_by_week(df: pd.DataFrame) -> plt.Figure:
    st.markdown("## Sales in Thousands by Promotion and Week")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(
        data=df, x="week", y="SalesInThousands", hue="Promotion", ax=ax, errorbar=("ci", 95)
    )
    plt.title("Sales in Thousands by Promotion and Week")
    plt.xlabel("Week")
    plt.ylim(bottom=0)
    plt.ylabel("Sales in Thousands")
    plt.tight_layout()
    sns.despine()
    return fig


def plot_sales_by_promotion(df: pd.DataFrame) -> plt.Figure:
    st.markdown("## Sales in Thousands by Promotion")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax = sns.barplot(data=df, x="Promotion", y="SalesInThousands", ax=ax, errorbar=None)
    for i in ax.containers:
        ax.bar_label(i, fmt="%.1f")

    plt.title("Sales in Thousands by Promotion")
    plt.xlabel("Promotion")
    plt.ylim(bottom=0)
    plt.ylabel("Sales in Thousands")
    plt.tight_layout()
    sns.despine()
    return fig


def clean_data_with_user_options(raw_df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filter Options")
    promotion_options = st.sidebar.multiselect("Select Promotions", options=[1, 2, 3], default=[1, 2, 3])
    week_options = st.sidebar.multiselect("Select Weeks", options=[1, 2, 3, 4], default=[1, 2, 3, 4])
    market_options = st.sidebar.multiselect(
        "Select Market Size",
        options=["Large", "Medium", "Small"],
        default=["Large", "Medium", "Small"],
    )
    return raw_df[
        (raw_df["Promotion"].isin(promotion_options))
        & (raw_df["week"].isin(week_options))
        & (raw_df["MarketSize"].isin(market_options))
    ]


def main() -> None:
    configure_page()
    configure_overview()
    mc_raw_df = load_data()
    filtered_df = clean_data_with_user_options(mc_raw_df)
    st.pyplot(plot_sales_by_week(filtered_df))
    st.pyplot(plot_sales_by_promotion(filtered_df))


main()
