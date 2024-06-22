import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_mildew_visualizer import page_mildew_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

app = MultiPage(app_name="Cherry Leave Mold Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.app_page("Quick Project Summary", page_summary_body)
app.app_page("Cherry Leaves Mildew Visualiser", page_mildew_visualizer_body)
app.app_page("Cherry Leaves Mildew Detection", page_mildew_detector_body)
app.app_page("Project Hypothesis", page_project_hypothesis_body)
app.app_page("ML Performance Metrics", page_ml_performance_metrics)

app.run()  # Run the app
