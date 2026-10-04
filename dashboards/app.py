import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Netflix Content Intelligence",
    page_icon="🎬",
    layout="wide"
)


# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/netflix_titles.csv")

    df["date_added"] = df["date_added"].str.strip()
    df["date_added"] = pd.to_datetime(
        df["date_added"],
        format="%B %d, %Y",
        errors="coerce"
    )

    return df


df = load_data()


# -----------------------------
# Title
# -----------------------------
st.title("🎬 Netflix Content Intelligence")
st.markdown(
    "Explore Netflix content, ratings, release years, and content trends."
)


# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

if st.sidebar.button("Clear All Filters"):
    st.session_state["content_type"] = df["type"].unique().tolist()
    st.session_state["rating"] = []
    st.session_state["release_year"] = (
        int(df["release_year"].min()),
        int(df["release_year"].max())
    )
    st.session_state["title_search"] = ""

content_type = st.sidebar.multiselect(
    "Content Type",
    options=df["type"].unique(),
    default=st.session_state.get(
        "content_type",
        df["type"].unique().tolist()
    ),
    key="content_type"
)

rating = st.sidebar.multiselect(
    "Rating",
    options=sorted(df["rating"].dropna().unique()),
    default=st.session_state.get("rating", []),
    key="rating"
)

release_year = st.sidebar.slider(
    "Release Year",
    min_value=int(df["release_year"].min()),
    max_value=int(df["release_year"].max()),
    value=st.session_state.get(
        "release_year",
        (
            int(df["release_year"].min()),
            int(df["release_year"].max())
        )
    ),
    key="release_year"
)

title_search = st.sidebar.text_input(
    "Search Title",
    value=st.session_state.get("title_search", ""),
    key="title_search"
)

filtered_df = df[
    df["type"].isin(content_type)
]

if rating:
    filtered_df = filtered_df[
        filtered_df["rating"].isin(rating)
    ]

filtered_df = filtered_df[
    filtered_df["release_year"].between(
        release_year[0],
        release_year[1]
    )
]

if title_search:
    filtered_df = filtered_df[
        filtered_df["title"].str.contains(
            title_search,
            case=False,
            na=False
        )
    ]
# -----------------------------
# Title Details
# -----------------------------
st.subheader("Title Details")

st.dataframe(
    filtered_df[
        ["title", "type", "release_year", "rating", "country"]
    ],
    use_container_width=True
)

# -----------------------------
# Top Genres
# -----------------------------
st.subheader("Top Genres")

genres = (
    filtered_df["listed_in"]
    .dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

fig, ax = plt.subplots(figsize=(10, 5))

genres.sort_values().plot(
    kind="barh",
    color="lavender",
    ax=ax
)

ax.set_xlabel("Number of Titles")
ax.set_ylabel("Genre")
ax.set_title("Top 10 Genres")

st.pyplot(fig)
# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Titles", len(filtered_df))

with col2:
    st.metric(
        "Movies",
        len(filtered_df[filtered_df["type"] == "Movie"])
    )

with col3:
    st.metric(
        "TV Shows",
        len(filtered_df[filtered_df["type"] == "TV Show"])
    )


# -----------------------------
# Content Type Distribution
# -----------------------------
st.subheader("Content Type Distribution")

type_counts = filtered_df["type"].value_counts()

fig, ax = plt.subplots()

type_counts.plot(
    kind="bar",
    color="lavender",
    ax=ax
)

ax.set_xlabel("Content Type")
ax.set_ylabel("Number of Titles")
ax.set_title("Movies vs TV Shows")

st.pyplot(fig)


# -----------------------------
# Rating Distribution
# -----------------------------
st.subheader("Rating Distribution")

rating_counts = filtered_df["rating"].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))

rating_counts.plot(
    kind="bar",
    color="lavender",
    ax=ax
)

ax.set_xlabel("Rating")
ax.set_ylabel("Number of Titles")
ax.tick_params(axis="x", rotation=45)

st.pyplot(fig)


# -----------------------------
# Release Year Distribution
# -----------------------------
st.subheader("Release Year Distribution")

fig, ax = plt.subplots(figsize=(10, 5))

filtered_df["release_year"].plot(
    kind="hist",
    bins=30,
    color="lavender",
    edgecolor="black",
    ax=ax
)

ax.set_xlabel("Release Year")
ax.set_ylabel("Number of Titles")

st.pyplot(fig)


# -----------------------------
# Content Added by Year
# -----------------------------
st.subheader("Netflix Content Added by Year")

filtered_df["year_added"] = filtered_df["date_added"].dt.year

yearly_additions = (
    filtered_df["year_added"]
    .value_counts()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(12, 5))

yearly_additions.plot(
    kind="line",
    color="mediumpurple",
    marker="o",
    ax=ax
)

ax.set_xlabel("Year Added")
ax.set_ylabel("Number of Titles")

st.pyplot(fig)