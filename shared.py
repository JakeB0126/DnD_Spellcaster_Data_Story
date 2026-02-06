import streamlit as st

DATA_BIG_ZIP = "over_one_mil_chars.zip"
DATA_SMALL_CSV = "cleaned_data_DnD_smaller.csv"

SELECTED_CLASSES = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"]

CLASS_COLORS = {
    "Bard": "#AB6DAC",
    "Cleric": "#91A1B2",
    "Druid": "#7A853B",
    "Sorcerer": "#992E2E",
    "Warlock": "#7B469B",
    "Wizard": "#2A50A1",
}

IMAGE_FILES = [
    "Bard_DS.png",
    "Cleric_DS.png",
    "Druid_DS.png",
    "Sorcerer_DS.png",
    "Warlock_DS.png",
    "Wizard_DS.png",
    "DnD_Races.png",
    "Magic_Missile.png",
]


def apply_theme():
    st.markdown(
        """
    <style>
    /* Background for entire app */
    .stApp {
        background-color: #001f3f; /* Midnight Blue */
        color: #ffffff; /* White text */
    }

    /* Custom Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Almendra+SC&display=swap');

    /* Title and Header */
    .stApp h1, .stApp h2 {
        font-family: 'Cinzel', serif;
        color: #5dade2; /* Glacial Blue for main title */
        text-shadow: 2px 2px 5px rgba(173, 216, 230, 0.6); /* Give it that Ice Glow effect. */
    }

    /* Subheaders */
    .stApp h3 {
        font-family: 'Cinzel', serif;
        color: #b3cde0; /* Icy silver */
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.5); /* MORE GLOW */
    }

    /* Paragraphs */
    .stApp p {
        font-family: 'Almendra SC', serif;
        font-size: 18px;
        line-height: 1.5; /* better readability */
        color: #ffffff; /* more white text */
    }

    /* Style for code blocks */
    .stApp code {
        background-color: #102a43; /* Darker Blue */
        color: #a3e4d7; /* Pale Aqua */
        font-family: 'Courier New', monospace;
        padding: 6px 8px;
        border-radius: 4px;
        box-shadow: 0px 0px 8px rgba(163, 228, 215, 0.5);
    }
    </style>
""",
        unsafe_allow_html=True,
    )
