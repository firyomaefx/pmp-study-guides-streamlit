import streamlit as st
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data.knowledge_areas import KNOWLEDGE_AREAS
from data.study_guides import STUDY_GUIDES
from utils.state import init_session_state, get_progress_summary

# Page config
st.set_page_config(
    page_title="📚 PMP Study Guides",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize state
init_session_state()

# Custom CSS for mobile-friendly styling
st.markdown("""
<style>
    .main-header {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #1E293B !important;
        margin-bottom: 0.5rem !important;
    }
    .sub-header {
        font-size: 1.1rem !important;
        color: #64748B !important;
        margin-bottom: 2rem !important;
    }
    .metric-card {
        background: #F8FAFC;
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid #E2E8F0;
    }
    .ka-card {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid #E2E8F0;
        margin-bottom: 0.75rem;
    }
    .ka-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1E293B;
    }
    .ka-desc {
        font-size: 0.85rem;
        color: #64748B;
        margin-top: 0.25rem;
    }
    .progress-text {
        font-size: 0.8rem;
        color: #2563EB;
        font-weight: 500;
    }
    /* Make buttons larger for mobile */
    .stButton>button {
        min-height: 44px;
        font-size: 1rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📚 PMP Study Guides")
st.sidebar.markdown("---")

# Main content
st.markdown('<div class="main-header">📚 PMP Study Guides</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Your mobile-first PMP exam preparation companion</div>', unsafe_allow_html=True)

# Progress summary
progress = get_progress_summary()

# Key metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Guides", f"{progress['guides_read']}/{progress['guides_total']}")
with col2:
    st.metric("Questions", progress['questions_answered'])
with col3:
    st.metric("Flashcards", progress['flashcards_known'])

st.markdown("---")

# Quick access cards
st.subheader("🎯 Quick Access")

for ka in KNOWLEDGE_AREAS:
    ka_id = ka['id']
    guide = STUDY_GUIDES.get(ka_id, {})
    total_sections = len(guide.get('processes', []))
    read_sections = st.session_state.get(f"ka_{ka_id}_read", [])
    progress_pct = len(read_sections) / total_sections if total_sections > 0 else 0
    
    with st.container():
        st.markdown(f"""
        <div class="ka-card">
            <div class="ka-title">{ka['name']}</div>
            <div class="ka-desc">{ka['description'][:100]}...</div>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.progress(progress_pct, text=f"{len(read_sections)}/{total_sections} sections")
        with col_b:
            if st.button("Study", key=f"btn_{ka_id}", use_container_width=True):
                st.switch_page("pages/1_Study_Guides.py")

st.markdown("---")

# Footer
st.caption("Built with ❤️ for PMP candidates | PMBOK 6th & 7th Editions")
