import streamlit as st
from data.questions import QUESTIONS
from utils.state import save_progress

st.set_page_config(page_title="❓ Question Bank", page_icon="❓", layout="centered")

st.title("❓ Question Bank")
st.caption(f"Practice with {len(QUESTIONS)} PMP exam questions")

# Filters
st.sidebar.header("🔍 Filters")
domains = list(set(q.get('domain', 'unknown') for q in QUESTIONS))
kas = list(set(q.get('knowledge_area', 'unknown') for q in QUESTIONS))
difficulties = list(set(q.get('difficulty', 'unknown') for q in QUESTIONS))

selected_domain = st.sidebar.selectbox("Domain", ["All"] + domains)
selected_ka = st.sidebar.selectbox("Knowledge Area", ["All"] + kas)
selected_diff = st.sidebar.selectbox("Difficulty", ["All"] + difficulties)

# Filter questions
filtered = QUESTIONS.copy()
if selected_domain != "All":
    filtered = [q for q in filtered if q.get('domain') == selected_domain]
if selected_ka != "All":
    filtered = [q for q in filtered if q.get('knowledge_area') == selected_ka]
if selected_diff != "All":
    filtered = [q for q in filtered if q.get('difficulty') == selected_diff]

st.markdown(f"**Showing {len(filtered)} questions**")
st.markdown("---")

# Display questions
for i, q in enumerate(filtered):
    with st.container():
        # Header
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown(f"**{q['id']}** | {q['knowledge_area'].replace('-', ' ').title()}")
        with col2:
            st.markdown(f"Difficulty: `{q['difficulty'].upper()}`")
        with col3:
            st.markdown(f"Domain: `{q['domain'].upper()}`")
        
        # Scenario
        if q.get('scenario'):
            st.info(q['scenario'])
        
        # Question
        st.markdown(f"**{q['question']}**")
        
        # Options
        options = q.get('options', [])
        option_labels = [f"{opt['id']}. {opt['text']}" for opt in options]
        
        # Use a unique key for each question
        answer_key = f"answer_{q['id']}"
        
        if answer_key not in st.session_state:
            st.session_state[answer_key] = None
        
        selected = st.radio(
            "Select your answer:",
            option_labels,
            key=answer_key,
            index=None
        )
        
        # Check answer
        if selected:
            selected_id = selected.split('.')[0]
            correct_id = q['correct_answer']
            
            if selected_id == correct_id:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect. Correct answer: **{correct_id}**")
            
            # Show explanation
            with st.expander("📖 View Explanation"):
                st.markdown(q['explanation'])
                st.caption(f"References: {', '.join(q.get('references', []))}")
        
        st.markdown("---")
