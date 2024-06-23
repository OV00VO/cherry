# Credits to Code Institute: All code below is either; 
# re-modeled, re-structed or re-created to fit this project.
import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"This visual criteria are used to detect mildew on cherry leaves:\n\n"
        f"Cherry leaf spot shows as purple spots turning brown or gray, "
        f"with possible white fungus in the center on top of leaves. \n\n"
        f"Powdery mildew shows as white patches on the underside of leaves, "
        f"which may become distorted.\n"
        f"Look for these signs on young leaves and in the inner canopy.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains of in total 4208 images\n with a 50 percent split of infected and uninfected leaves."
        )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file] Cherry Leave Mold Detection Analysis https://github.com/OV00VO/cherry/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"infected with mildew and uninfected with mildew, in a visually way.\n"
        f"* 2 - The client is interested in telling whether a given leaf contains mildew on the cherry leaf or not. "
        )
