# Credits to Code Institute: All code below is either; 
# re-modeled, re-structed or re-created to fit this project.
import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect mildew on the cherry leaf and it have clear marks/signs, "
        f"typically on small parts of the leaf, that can differentiate them from an uninfected leaf. \n\n"
        f"* An Image Montage shows that typically a mildew leaf has powdery mildew across it. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )
