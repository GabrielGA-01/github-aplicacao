import os
import streamlit as st
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component("streamlit_react", url="http://localhost:5173")
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "../build")
    _component_func = components.declare_component("streamlit_react", path=build_dir)

def react_counter(count=0, key=None):
    return _component_func(view="pag0", count=count, key=key, default=0)

def pagina1(key=None):
    return _component_func(view="pag1", key=key, default=0)

def pagina2(key=None):
    return _component_func(view="pag2", key=key, default=0)

def pagina3(key=None):
    return _component_func(view="pag3", key=key, default=0)