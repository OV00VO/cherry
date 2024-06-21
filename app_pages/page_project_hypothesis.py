import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect mold on the cherry leaves and they have clear marks/signs, "
        f"typically on small parts of the leave, that can differentiate them from an uninfected leave. \n\n"
        f"* An Image Montage shows that typically a mold leave has mold across it. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )
