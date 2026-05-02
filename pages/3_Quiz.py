import streamlit as st
from data.questions import QUESTIONS
from utils.scoring import calculate_score, domain_breakdown
from utils.state import save_progress

st.set_page_config(page_title="📝 Quiz", page_icon="📝", layout="centered")

st.title("📝 Quiz Mode")
st.caption("10 random questions — test your knowledge!")

# Initialize quiz state
if 'quiz_active' not in st.session_state:
    st.session_state.quiz_active = False
if 'quiz_questions' not in st.session_state:
    st.session_state.quiz_questions = []
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False

def start_quiz():
    import random
    # Filter by difficulty if selected
    filtered = QUESTIONS.copy()
    if st.session_state.get('quiz_diff') and st.session_state.quiz_diff != "All":
        filtered = [q for q in filtered if q.get('difficulty') == st.session_state.quiz_diff]
    
    # Select 10 random questions
    count = min(10, len(filtered))
    st.session_state.quiz_questions = random.sample(filtered, count)
    st.session_state.quiz_answers = {}
    st.session_state.quiz_submitted = False
    st.session_state.quiz_active = True
    st.rerun()

def submit_quiz():
    st.session_state.quiz_submitted = True
    
    # Calculate score
    correct = sum(1 for ans in st.session_state.quiz_answers.values() if ans.get('correct', False))
    total = len(st.session_state.quiz_questions)
    score = calculate_score(correct, total)
    
    # Save result
    st.session_state.quiz_results.append({
        'score': score,
        'correct': correct,
        'total': total,
        'difficulty': st.session_state.get('quiz_diff', 'All')
    })
    save_progress()
    st.rerun()

def reset_quiz():
    st.session_state.quiz_active = False
    st.session_state.quiz_questions = []
    st.session_state.quiz_answers = {}
    st.session_state.quiz_submitted = False
    st.rerun()

# Quiz setup
if not st.session_state.quiz_active:
    st.subheader("Start New Quiz")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.selectbox(
            "Difficulty",
            ["All", "easy", "medium", "hard"],
            key="quiz_diff"
        )
    
    st.markdown("**Rules:**")
    st.markdown("• 10 questions")
    st.markdown("• Select the best answer for each")
    st.markdown("• Submit when ready")
    st.markdown("• Review your results")
    
    if st.button("🚀 Start Quiz", use_container_width=True):
        start_quiz()

# Active quiz
else:
    if not st.session_state.quiz_submitted:
        st.subheader(f"Question {len(st.session_state.quiz_answers) + 1} of {len(st.session_state.quiz_questions)}")
        
        # Show current question
        current_idx = len(st.session_state.quiz_answers)
        if current_idx < len(st.session_state.quiz_questions):
            q = st.session_state.quiz_questions[current_idx]
            
            st.progress((current_idx) / len(st.session_state.quiz_questions))
            
            if q.get('scenario'):
                st.info(q['scenario'])
            
            st.markdown(f"**{q['question']}**")
            
            # Options
            options = q.get('options', [])
            for opt in options:
                if st.button(f"{opt['id']}. {opt['text']}", key=f"q_{q['id']}_{opt['id']}", use_container_width=True):
                    st.session_state.quiz_answers[q['id']] = {
                        'selected': opt['id'],
                        'correct': opt['id'] == q['correct_answer'],
                        'domain': q.get('domain', 'unknown')
                    }
                    st.rerun()
        else:
            # All answered, show submit
            st.success("All questions answered!")
            if st.button("📊 Submit Quiz", use_container_width=True, type="primary"):
                submit_quiz()
    
    else:
        # Results
        correct = sum(1 for ans in st.session_state.quiz_answers.values() if ans.get('correct', False))
        total = len(st.session_state.quiz_questions)
        score = calculate_score(correct, total)
        
        # Score display
        if score >= 65:
            st.success(f"🎉 PASSED! Score: {score}% ({correct}/{total})")
        else:
            st.error(f"❌ Needs Improvement. Score: {score}% ({correct}/{total})")
        
        # Domain breakdown
        answers_list = [
            {'domain': ans['domain'], 'correct': ans['correct']}
            for ans in st.session_state.quiz_answers.values()
        ]
        breakdown = domain_breakdown(answers_list)
        
        if breakdown:
            st.subheader("Domain Breakdown")
            for domain, stats in breakdown.items():
                st.markdown(f"**{domain.upper()}:** {stats['correct']}/{stats['total']} ({stats['pct']}%)")
        
        # Review answers
        st.subheader("Review Answers")
        for q in st.session_state.quiz_questions:
            ans = st.session_state.quiz_answers.get(q['id'], {})
            with st.expander(f"{q['id']} — {'✅' if ans.get('correct') else '❌'}"):
                st.markdown(f"**Question:** {q['question']}")
                st.markdown(f"Your answer: **{ans.get('selected', 'N/A')}**")
                st.markdown(f"Correct answer: **{q['correct_answer']}**")
                st.markdown(f"**Explanation:** {q['explanation']}")
        
        if st.button("🔄 Take Another Quiz", use_container_width=True):
            reset_quiz()
