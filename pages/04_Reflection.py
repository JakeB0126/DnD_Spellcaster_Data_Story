import streamlit as st

import shared

shared.apply_theme()

st.header("Reflection")

st.subheader("How Did My Design Decisions Work for User Feedback and How Did They Fall Short?")
st.write("""
Feedback was positive on organization, storytelling, and interactivity, especially the radial and sunburst charts. The D&D color palette helped the visuals feel authentic.

The main critique was coverage: more graphs and clearer labels would improve first-glance comprehension.
""")

st.subheader("Failed Attempts at Visualization: How Did I Change Tactics to Improve Outcomes?")
st.write("""
Early attempts to show all 12 classes were cluttered, so I narrowed the focus to six spellcasters. Radial bars required multiple layout tweaks for readability.

Switching to Plotly added interactivity that made exploration easier and more engaging.
""")

st.subheader("Where Might I Revise in Another Round of Iteration?")
st.write("""
If I had another round of iteration, I would:
1. Expand spell analysis beyond the top three, possibly by level or theme.
2. Try alternative formats like heatmaps or network graphs.
3. Tighten labels and tooltips for faster reading.
4. Explore multiclass characters if data allows.
""")

st.subheader("Are There Any Stories My Current Work Occludes, Marginalizes, or Minimizes?")
st.write("""
Yes, there are limits that shape the story:
- **Smaller spell dataset:** Fewer data points limit higher-level spell insights.
- **Non-spellcasting classes omitted:** Fighters, Rogues, and others are absent for clarity.
- **Paywalled content bias:** Free options may be overrepresented.

Future work could expand class coverage, compare free vs paid content, and explore player demographics.
""")

st.subheader("What Did I Like Best About Learning How to Create Data Narratives?")
st.write("""
I enjoyed experimenting with radial and sunburst charts, and aligning visuals with the official D&D palette. Combining interactivity with storytelling was especially rewarding.
""")

st.subheader("References")
st.write("""
AutumnArchfey. (2023, February 20). Dungeons and Dragons Races Lineup [Digital art].
    DeviantArt. https://www.deviantart.com/autumnarchfey/art/Dungeons-and-Dragons-Races-Lineup-954300538

Bonnin, M. (2022). DnD characters [Data set]. Kaggle.
    Retrieved from https://www.kaggle.com/datasets/maximebonnin/dnd-characters-test

Booker, B. M. (2021, June 18). Common terms new Dungeons & Dragons players should learn.
    D&D Beyond. Retrieved from https://www.dndbeyond.com/posts/1026-common-terms-new-dungeons-dragons-players-should

Herena, E. L. (2022). D&D 5e Spells [Digital art]. ArtStation. Retrieved from https://www.artstation.com/artwork/LeDzkP

Mancarci, B. O. (2020). dnddata [Data set]. GitHub. Retrieved from https://github.com/oganm/dnddata

Varela, R. (2024, August 20). DND Classes [Pixel art]. Lospec. Retrieved from https://lospec.com/gallery/rpvarela/dnd-classes
""")
