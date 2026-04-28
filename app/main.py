import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data

st.set_page_config(page_title="African Climate Dashboard", layout="wide")

df = load_data()

st.title("🌍 African Climate Trend Dashboard")

# -------------------------
# SIDEBAR CONTROLS
# -------------------------

countries = st.multiselect(
    "Select Countries",
    df["Country"].unique(),
    default=df["Country"].unique()
)

year_range = st.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2015, 2026)
)

variable = st.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)

# -------------------------
# FILTER DATA
# -------------------------

filtered = df[
    (df["Country"].isin(countries)) &
    (df["Year"].between(year_range[0], year_range[1]))
]

# -------------------------
# LINE CHART (TREND)
# -------------------------

st.subheader("📈 Climate Trend Over Time")

fig, ax = plt.subplots()

for c in countries:
    temp = filtered[filtered["Country"] == c].groupby("Year")[variable].mean()
    ax.plot(temp.index, temp.values, label=c)

ax.set_title(f"{variable} Trend")
ax.legend()

st.pyplot(fig)

# -------------------------
# BOX PLOT
# -------------------------

st.subheader("📊 Distribution Analysis")

fig2, ax2 = plt.subplots()

sns.boxplot(data=filtered, x="Country", y=variable, ax=ax2)

st.pyplot(fig2)

# -------------------------
# SUMMARY
# -------------------------

st.subheader("📌 Summary Statistics")

st.dataframe(
    filtered.groupby("Country")[variable].describe()
)