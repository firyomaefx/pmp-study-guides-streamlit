import streamlit as st
from data.mock_exams import MOCK_EXAMS
from utils.scoring import calculate_score, is_passing, domain_breakdown
from utils.state import save_progress

st.set_page_config(page_title="🏆 Mock Exams", page_icon="🏆", layout="centered")

st.title("🏆 Mock Exams")
st.caption("3 full practice exams — simulate the real test")

# Initialize exam state
if 'exam_active' not in st.session_state:
    st.session_state.exam_active = False
if 'exam_questions' not in st.session_state:
    st.session_state.exam_questions = []
if 'exam_answers' not in st.session_state:
    st.session_state.exam_answers = {}
if 'exam_submitted' not in st.session_state:
    st.session_state.exam_submitted = False
if 'exam_current_q' not in st.session_state:
    st.session_state.exam_current_q = 0

def start_exam(exam_idx):
    exam = MOCK_EXAMS[exam_idx]
    st.session_state.exam_questions = exam.get('questions', [])
    st.session_state.exam_answers = {}
    st.session_state.exam_submitted = False
    st.session_state.exam_current_q = 0
    st.session_state.exam_active = True
    st.session_state.exam_name = exam.get('name', f"Mock Exam {exam_idx + 1}")
    st.rerun()

def submit_exam():
    st.session_state.exam_submitted = True
    
    correct = sum(1 for ans in st.session_state.exam_answers.values() if ans.get('correct', False))
    total = len(st.session_state.exam_questions)
    score = calculate_score(correct, total)
    
    st.session_state.mock_exam_results.append({
        'name': st.session_state.get('exam_name', 'Unknown'),
        'score': score,
        'correct': correct,
        'total': total,
        'passed': is_passing(score)
    })
    save_progress()
    st.rerun()

def reset_exam():
    st.session_state.exam_active = False
    st.session_state.exam_questions = []
    st.session_state.exam_answers = {}
    st.session_state.exam_submitted = False
    st.session_state.exam_current_q = 0
    st.rerun()

# Exam selection
if not st.session_state.exam_active:
    st.subheader("Choose Your Exam")
    
    for i, exam in enumerate(MOCK_EXAMS):
        with st.container():
            st.markdown(f"**{exam.get('name', f'Mock Exam {i+1}')}**")
            st.markdown(f"{exam.get('description', '')}")
            st.markdown(f"Questions: {len(exam.get('questions', []))} | Time: 120 minutes | Pass: 65%")
            
            if st.button(f"Start {exam.get('name', f'Exam {i+1}')}", key=f"start_exam_{i}", use_container_width=True):
                start_exam(i)
            st.markdown("---")

# Active exam
else:
    if not st.session_state.exam_submitted:
        # Header
        st.subheader(st.session_state.get('exam_name', 'Mock Exam'))
        
        total_q = len(st.session_state.exam_questions)
        answered = len(st.session_state.exam_answers)
        
        # Progress
        st.progress(answered / total_q, text=f"Answered: {answered}/{total_q}")
        
        # Question navigator
        st.caption("Jump to question:")
        cols = st.columns(min(5, total_q))
        for i in range(total_q):
            q_id = st.session_state.exam_questions[i].get('id', str(i))
            is_answered = q_id in st.session_state.exam_answers
            is_current = i == st.session_state.exam_current_q
            
            with cols[i % 5]:
                btn_type = "primary" if is_current else "secondary" if is_answered else None
                if st.button(f"{i+1}", key=f"nav_{i}", type=btn_type, use_container_width=True):
                    st.session_state.exam_current_q = i
                    st.rerun()
        
        st.markdown("---")
        
        # Current question
        q_idx = st.session_state.exam_current_q
        if q_idx < total_q:
            q = st.session_state.exam_questions[q_idx]
            
            st.markdown(f"**Question {q_idx + 1} of {total_q}**")
            
            if q.get('scenario'):
                st.info(q['scenario'])
            
            st.markdown(f"**{q['question']}**")
            
            # Options
            options = q.get('options', [])
            q_id = q.get('id', str(q_idx))
            
            # Check if already answered
            current_answer = st.session_state.exam_answers.get(q_id, {}).get('selected', None)
            
            for opt in options:
                is_selected = current_answer == opt['id']
                btn_type = "primary" if is_selected else "secondary"
                
                if st.button(f"{opt['id']}. {opt['text']}", key=f"exam_{q_id}_{opt['id']}", type=btn_type, use_container_width=True):
                    st.session_state.exam_answers[q_id] = {
                        'selected': opt['id'],
                        'correct': opt['id'] == q['correct_answer'],
                        'domain': q.get('domain', 'unknown')
                    }
                    # Auto-advance to next question
                    if q_idx + 1 < total_q:
                        st.session_state.exam_current_q = q_idx + 1
                    st.rerun()
            
            # Flag button
            col1, col2 = st.columns([1, 3])
            with col1:
                is_flagged = q_id in st.session_state.questions_flagged
                if st.button("🚩 Flag" if not is_flagged else "🚩 Flagged", key=f"flag_{q_id}"):
                    if is_flagged:
                        st.session_state.questions_flagged.remove(q_id)
                    else:
                        st.session_state.questions_flagged.append(q_id)
                    save_progress()
                    st.rerun()
        
        # Submit button
        if answered == total_q:
            st.success("All questions answered!")
        
        if st.button("📊 Submit Exam", use_container_width=True, type="primary"):
            submit_exam()
    
    else:
        # Results
        correct = sum(1 for ans in st.session_state.exam_answers.values() if ans.get('correct', False))
        total = len(st.session_state.exam_questions)
        score = calculate_score(correct, total)
        passed = is_passing(score)
        
        # Result banner
        if passed:
            st.success(f"🎉 PASSED! Score: {score}% ({correct}/{total})")
        else:
            st.error(f"❌ Did Not Pass. Score: {score}% ({correct}/{total})")
            st.info("Passing score is 65%")
        
        # Domain breakdown
        answers_list = [
            {'domain': ans['domain'], 'correct': ans['correct']}
            for ans in st.session_state.exam_answers.values()
        ]
        breakdown = domain_breakdown(answers_list)
        
        if breakdown:
            st.subheader("Domain Performance")
            for domain, stats in breakdown.items():
                color = "🟢" if stats['pct'] >= 65 else "🔴"
                st.markdown(f"{color} **{domain.upper()}:** {stats['correct']}/{stats['total']} ({stats['pct']}%)")
        
        # Review
        st.subheader("Question Review")
        for i, q in enumerate(st.session_state.exam_questions):
            q_id = q.get('id', str(i))
            ans = st.session_state.exam_answers.get(q_id, {})
            is_correct = ans.get('correct', False)
            
            with st.expander(f"Q{i+1}: {'✅' if is_correct else '❌'} {q['question'][:50]}..."):
                st.markdown(f"**Question:** {q['question']}")
                st.markdown(f"Your answer: **{ans.get('selected', 'N/A')}**")
                st.markdown(f"Correct: **{q['correct_answer']}**")
                st.markdown(f"**Explanation:** {q.get('explanation', 'No explanation')}")
        
        if st.button("🔄 Take Another Exam", use_container_width=True):
            reset_exam()
