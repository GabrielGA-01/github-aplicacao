import os
import streamlit as st
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component("streamlit_react_counter", url = "http://localhost:5173")
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "../frontend/build")
    print(build_dir)
    _component_func = components.declare_component("streamlit_react_counter", path=build_dir)

def react_counter(count = 0, key = None):
    return _component_func(count=count, key=key, default=0)
