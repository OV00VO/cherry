import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* X is a parasitic infection transmitted by the bite of infected female "
        f"Anopheles mosquitoes.\n"
        f"* A blood smear sample is collected, mixed with a reagent and examined in "
        f"the microscope. Visual criteria are used to detect mold on cherry leaves.\n"
        f"* Interesting facts here, "
        f"x "
        f"x "
        f"x "
        f"x\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains xxxx out of +x thousand images taken from "
        f"x"
        f"x")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file]x(https://github.com/Code-Institute-Solutions/WalkthroughProject01/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"infected with mold and uninfected with mold in a visually way.\n"
        f"* 2 - The client is interested in telling whether a given cell contains a mold on the cherry leaves or not. "
        )
