import streamlit as st

import shared

shared.apply_theme()

# -----------------------------------------------------------
# INTRODUCTION
# -----------------------------------------------------------

st.title("The Spellcaster's Compendium: A Data-Driven Look at D&D's Main Magic-Wielders")

st.write("""
Welcome, seeker of arcane knowledge. This archive captures how players build spellcasters in Dungeons & Dragons, where magic comes from study, faith, or pacts.

Even with endless choice, patterns emerge. By examining real player data, we can see how tradition, optimization, and storytelling shape spellcaster creation.

Whether you are crafting your first spellcaster or simply curious, this compendium highlights the trends that define these magical classes.
""")

st.subheader("The Quest for Data: A Research Journey")

st.write("""
Like any great adventure, this story began with a search for knowledge. The main dataset came from Kaggle, built from over 1.2 million D&D Beyond entries.
To capture richer details, I found a second dataset through Reddit. After cleaning duplicates, it narrowed from 10,000+ entries to about 7,000 usable records.
""")

st.subheader("The Evolution of the Story: Narrowing the Scope")

st.write("""
Originally, this study aimed to analyze all twelve classes and player geography. The data itself made that scope less useful, so the story narrowed to what it could support.

**Key Challenges:**
""")

st.write("""
1. **The Geography Dilemma:** At first, a geographic breakdown sounded exciting, but the dataset primarily covered only a handful of countries, which 
made for limited insights.
2. **The Twelve-Class Chaos:** Attempting to visualize all 12 classes quickly turned the data into an unreadable conglomeration of numbers and charts.
""")

st.write("""
Thus, the focus became the six spellcasting classes: Bard, Cleric, Druid, Sorcerer, Warlock, and Wizard. This kept the story cohesive and enabled deeper categories,
like spell choice, that reveal what makes each class distinct.
""")

# -----------------------------------------------------------
# IMAGE GRID
# -----------------------------------------------------------

st.header("D&D Spellcasting Classes")

# Row 1
col1, col2, col3 = st.columns(3)
with col1:
    st.image(shared.IMAGE_FILES[0], caption="", use_container_width=True)
with col2:
    st.image(shared.IMAGE_FILES[1], caption="", use_container_width=True)
with col3:
    st.image(shared.IMAGE_FILES[2], caption="", use_container_width=True)

# Row 2
col4, col5, col6 = st.columns(3)
with col4:
    st.image(shared.IMAGE_FILES[3], caption="", use_container_width=True)
with col5:
    st.image(shared.IMAGE_FILES[4], caption="", use_container_width=True)
with col6:
    st.image(shared.IMAGE_FILES[5], caption="", use_container_width=True)

st.subheader("Unveiling the Magic: Why Data Visualization Matters")

st.write("""
In a game as limitless as D&D, every player has their own take on a Warlock or Wizard. Visualizing the data helps reveal:
""")

st.write("""
- **Patterns in player choices:** Which spellcasters consistently favor specific races and backgrounds?
- **Thematic contrasts:** How well do players tend to follow the general idea of their class?
- **Unexpected trends:** Are there any metrics that defy expectations, challenging common assumptions?
""")

st.write("""
With over a million character entries, these visuals turn raw numbers into clear, accessible insights.
""")

st.subheader("The Dark Side of the Arcane: Potential Pitfalls")

st.write("""
Even a Wish spell cannot change one truth: data reflects who chose to record it. These datasets offer insight, but carry biases:
""")

st.write("""
- **Paywalled content bias:** Free options may be overrepresented.
- **Online-only source:** Paper-and-pencil players are largely excluded.
- **Zero values and outliers:** Removing zeros and capping gold can shift averages.
""")

st.write("""
These limits do not invalidate the data, but they do shape how we interpret it.
""")

st.write("""
### Preparing the Dataset for Analysis: General Transformations
To prepare the data for visualization, I:
- Removed duplicate entries from the smaller dataset.
- Filtered to six spellcasting classes.
- Counted class totals for direct comparison.
- Applied a custom D&D-inspired color palette.

These steps keep the analysis focused and readable.
""")
