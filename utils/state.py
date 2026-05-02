import streamlit as st
import json
import os

# Session state management

def init_session_state():
    """Initialize all session state variables"""
    defaults = {
        'guides_read': {},
        'questions_answered': [],
        'questions_flagged': [],
        'quiz_results': [],
        'flashcards_known': [],
        'flashcards_review': [],
        'mock_exam_results': [],
        'current_ka': None,
        'current_quiz': None,
        'current_exam': None,
        'exam_timer': None,
        'dark_mode': False
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
    
    # Load saved progress from file
    load_progress()

def get_progress_file():
    """Get path to progress file"""
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.pmp_progress.json')

def save_progress():
    """Save current progress to JSON file"""
    progress = {
        'guides_read': st.session_state.guides_read,
        'questions_answered': st.session_state.questions_answered,
        'questions_flagged': st.session_state.questions_flagged,
        'quiz_results': st.session_state.quiz_results,
        'flashcards_known': st.session_state.flashcards_known,
        'flashcards_review': st.session_state.flashcards_review,
        'mock_exam_results': st.session_state.mock_exam_results
    }
    
    try:
        with open(get_progress_file(), 'w') as f:
            json.dump(progress, f)
    except Exception as e:
        st.error(f"Could not save progress: {e}")

def load_progress():
    """Load progress from JSON file"""
    progress_file = get_progress_file()
    if os.path.exists(progress_file):
        try:
            with open(progress_file, 'r') as f:
                progress = json.load(f)
            
            for key, value in progress.items():
                if key in st.session_state:
                    st.session_state[key] = value
        except Exception:
            pass  # If file is corrupted, start fresh

def mark_section_read(ka_id: str, process_id: str):
    """Mark a study guide section as read"""
    if ka_id not in st.session_state.guides_read:
        st.session_state.guides_read[ka_id] = []
    
    if process_id not in st.session_state.guides_read[ka_id]:
        st.session_state.guides_read[ka_id].append(process_id)
        save_progress()
        return True
    return False

def is_section_read(ka_id: str, process_id: str) -> bool:
    """Check if a section has been read"""
    return process_id in st.session_state.guides_read.get(ka_id, [])

def get_ka_progress(ka_id: str, total_processes: int) -> tuple:
    """Get progress for a knowledge area"""
    read = len(st.session_state.guides_read.get(ka_id, []))
    pct = read / total_processes if total_processes > 0 else 0
    return read, total_processes, pct

def get_progress_summary():
    """Get overall progress summary"""
    from data.knowledge_areas import KNOWLEDGE_AREAS
    from data.study_guides import STUDY_GUIDES
    
    total_guides = 0
    read_guides = 0
    
    for ka in KNOWLEDGE_AREAS:
        ka_id = ka['id']
        guide = STUDY_GUIDES.get(ka_id, {})
        processes = len(guide.get('processes', []))
        total_guides += processes
        read_guides += len(st.session_state.guides_read.get(ka_id, []))
    
    return {
        'guides_read': read_guides,
        'guides_total': total_guides,
        'questions_answered': len(st.session_state.questions_answered),
        'flashcards_known': len(st.session_state.flashcards_known)
    }
