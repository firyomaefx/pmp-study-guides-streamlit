import streamlit as st
from data.knowledge_areas import KNOWLEDGE_AREAS
from data.study_guides import STUDY_GUIDES
from data.questions import QUESTIONS
from data.flashcards import FLASHCARDS
from utils.state import get_progress_summary

st.set_page_config(page_title="📊 My Progress", page_icon="📊", layout="centered")

st.title("📊 My Progress")
st.caption("Track your PMP preparation journey")

# Get summary
progress = get_progress_summary()

# Overall stats
st.subheader("Overall Progress")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Guides", f"{progress['guides_read']}/{progress['guides_total']}")
with col2:
    st.metric("Questions", progress['questions_answered'])
with col3:
    st.metric("Flashcards Known", progress['flashcards_known'])
with col4:
    quiz_count = len(st.session_state.get('quiz_results', []))
    st.metric("Quizzes Taken", quiz_count)

st.markdown("---")

# Study Guides Progress
st.subheader("📖 Study Guides")

for ka in KNOWLEDGE_AREAS:
    ka_id = ka['id']
    guide = STUDY_GUIDES.get(ka_id, {})
    processes = guide.get('processes', [])
    total = len(processes)
    read = len(st.session_state.guides_read.get(ka_id, []))
    pct = read / total if total > 0 else 0
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.progress(pct, text=f"{ka['name']}")
    with col2:
        st.markdown(f"**{read}/{total}**")

st.markdown("---")

# Quiz History
quiz_results = st.session_state.get('quiz_results', [])
if quiz_results:
    st.subheader("📝 Quiz History")
    
    for i, result in enumerate(quiz_results[-5:]):  # Show last 5
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown(f"Quiz {i+1}")
        with col2:
            st.markdown(f"{result['score']}%")
        with col3:
            if result['score'] >= 65:
                st.success("PASS")
            else:
                st.error("FAIL")

st.markdown("---")

# Mock Exam History
exam_results = st.session_state.get('mock_exam_results', [])
if exam_results:
    st.subheader("🏆 Mock Exam History")
    
    for result in exam_results:
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown(result.get('name', 'Unknown Exam'))
        with col2:
            st.markdown(f"{result['score']}%")
        with col3:
            if result.get('passed', False):
                st.success("PASS")
            else:
                st.error("FAIL")

st.markdown("---")

# Reset progress
st.subheader("⚠️ Danger Zone")
if st.button("🗑️ Reset All Progress", use_container_width=True):
    st.session_state.guides_read = {}
    st.session_state.questions_answered = []
    st.session_state.questions_flagged = []
    st.session_state.quiz_results = []
    st.session_state.flashcards_known = []
    st.session_state.flashcards_review = []
    st.session_state.mock_exam_results = []
    
    from utils.state import save_progress
    save_progress()
    st.rerun()
