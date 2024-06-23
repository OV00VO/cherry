# Credits to Code Institute: All code below is either; 
# re-modeled, re-structed or re-created to fit this project.
import streamlit as st
from src.data_management import load_pkl_file


def load_test_evaluation(version):
    return load_pkl_file(f'outputs/{version}/evaluation.pkl')