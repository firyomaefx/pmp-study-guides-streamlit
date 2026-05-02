import streamlit as st
import time
from data.mock_exams import MOCK_EXAMS
from utils.scoring import calculate_score, is_passing, domain_breakdown, get_question_timing_guide
from utils.state import save_progress
from utils.timers import (
    get_exam_duration_minutes, 
    get_exam_total_questions, 
    get_passing_threshold,
    get_domain_breakdown,
    get_exam_tips,
    format_duration
)

st.set_page_config(page_title="🏆 Mock Exams", page_icon="🏆", layout="centered")

st.title("🏆 Mock Exams")
st.caption(f"Simulate the real PMP exam — {get_exam_total_questions()} questions, {format_duration(get_exam_duration_minutes())}")

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
if 'exam_start_time' not in st.session_state:
    st.session_state.exam_start_time = None
if 'exam_elapsed' not in st.session_state:
    st.session_state.exam_elapsed = 0
if 'break_1_taken' not in st.session_state:
    st.session_state.break_1_taken = False
if 'break_2_taken' not in st.session_state:
    st.session_state.break_2_taken = False
if 'break_active' not in st.session_state:
    st.session_state.break_active = False
if 'break_start_time' not in st.session_state:
    st.session_state.break_start_time = None

def start_exam(exam_idx):
    exam = MOCK_EXAMS[exam_idx]
    questions = exam.get('questions', [])
    
    # For demo, limit to 15 questions but simulate 180
    if len(questions) > 15:
        import random
        questions = random.sample(questions, 15)
    
    st.session_state.exam_questions = questions
    st.session_state.exam_answers = {}
    st.session_state.exam_submitted = False
    st.session_state.exam_current_q = 0
    st.session_state.exam_start_time = time.time()
    st.session_state.exam_elapsed = 0
    st.session_state.exam_active = True
    st.session_state.exam_name = exam.get('name', f"Mock Exam {exam_idx + 1}")
    st.session_state.break_1_taken = False
    st.session_state.break_2_taken = False
    st.session_state.break_active = False
    st.session_state.break_start_time = None
    st.rerun()

def start_break():
    st.session_state.break_active = True
    st.session_state.break_start_time = time.time()
    st.rerun()

def end_break():
    # Add break duration to exam elapsed (paused during break)
    break_duration = int(time.time() - st.session_state.break_start_time)
    # Adjust exam_start_time forward by break duration so timer doesn't count it
    st.session_state.exam_start_time += break_duration
    st.session_state.break_active = False
    st.session_state.break_start_time = None
    st.rerun()

def submit_exam():
    st.session_state.exam_submitted = True
    
    correct = sum(1 for ans in st.session_state.exam_answers.values() if ans.get('correct', False))
    total = len(st.session_state.exam_answers)
    score = calculate_score(correct, total)
    threshold = get_passing_threshold()
    
    st.session_state.mock_exam_results.append({
        'name': st.session_state.get('exam_name', 'Unknown'),
        'score': score,
        'correct': correct,
        'total': total,
        'passed': is_passing(score, threshold),
        'elapsed_minutes': st.session_state.exam_elapsed // 60
    })
    save_progress()
    st.rerun()

def reset_exam():
    st.session_state.exam_active = False
    st.session_state.exam_questions = []
    st.session_state.exam_answers = {}
    st.session_state.exam_submitted = False
    st.session_state.exam_current_q = 0
    st.session_state.exam_start_time = None
    st.session_state.exam_elapsed = 0
    st.session_state.break_1_taken = False
    st.session_state.break_2_taken = False
    st.session_state.break_active = False
    st.session_state.break_start_time = None
    st.rerun()

# Exam selection
if not st.session_state.exam_active:
    st.subheader("Official PMP Exam Format")
    
    # Show exam format info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Questions", get_exam_total_questions())
    with col2:
        st.metric("Duration", format_duration(get_exam_duration_minutes()))
    with col3:
        st.metric("Passing Score", f"{get_passing_threshold()}%")
    
    st.markdown("---")
    
    # Domain breakdown
    st.subheader("📊 Domain Weightings")
    domains = get_domain_breakdown()
    current = domains['current']
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"**People**\n{current['people']['pct']}% ({current['people']['questions']} questions)")
    with col2:
        st.info(f"**Process**\n{current['process']['pct']}% ({current['process']['questions']} questions)")
    with col3:
        st.warning(f"**Business Environment**\n{current['business_environment']['pct']}% ({current['business_environment']['questions']} questions)")
    
    st.caption("⚠️ New weightings coming July 2026: People 33% | Process 41% | Business Environment 26%")
    
    st.markdown("---")
    
    # Exam tips
    with st.expander("💡 Exam Tips"):
        for tip in get_exam_tips():
            st.markdown(f"• {tip}")
    
    st.markdown("---")
    st.subheader("Choose Your Mock Exam")
    
    for i, exam in enumerate(MOCK_EXAMS):
        with st.container():
            st.markdown(f"**{exam.get('name', f'Mock Exam {i+1}')}**")
            st.markdown(f"{exam.get('description', '')}")
            st.markdown(f"Questions: {len(exam.get('questions', []))} | Time: {format_duration(get_exam_duration_minutes())} | Pass: {get_passing_threshold()}%")
            
            if st.button(f"Start {exam.get('name', f'Exam {i+1}')}", key=f"start_exam_{i}", use_container_width=True):
                start_exam(i)
            st.markdown("---")

# Active exam
else:
    if not st.session_state.exam_submitted:
        # Check if on break
        if st.session_state.break_active:
            st.title("☕ Break Time")
            st.subheader("Take a 10-minute break to recharge")
            
            # Break timer
            break_elapsed = int(time.time() - st.session_state.break_start_time)
            break_remaining = max(0, 600 - break_elapsed)  # 10 min = 600 sec
            break_mins = break_remaining // 60
            break_secs = break_remaining % 60
            
            if break_remaining <= 0:
                st.warning("⏰ Break time is over!")
            else:
                st.info(f"⏱️ Break time remaining: {break_mins:02d}:{break_secs:02d}")
            
            st.markdown("**Recommended during break:**")
            st.markdown("• 🚶 Stand up and stretch")
            st.markdown("• 💧 Drink water")
            st.markdown("• 🚻 Use restroom")
            st.markdown("• 🧘 Take deep breaths")
            st.markdown("• 🚫 Don't review exam content")
            
            if st.button("▶️ Resume Exam", use_container_width=True, type="primary"):
                end_break()
            
            st.stop()
        
        # Timer display
        if st.session_state.exam_start_time:
            st.session_state.exam_elapsed = int(time.time() - st.session_state.exam_start_time)
        
        total_seconds = get_exam_duration_minutes() * 60
        remaining_seconds = max(0, total_seconds - st.session_state.exam_elapsed)
        
        # Format timer
        hours = remaining_seconds // 3600
        mins = (remaining_seconds % 3600) // 60
        secs = remaining_seconds % 60
        timer_text = f"⏱️ {hours:02d}:{mins:02d}:{secs:02d}"
        
        # Timer styling
        if remaining_seconds < 600:  # Less than 10 minutes
            st.error(f"### {timer_text} — HURRY!")
        elif remaining_seconds < 1800:  # Less than 30 minutes
            st.warning(f"### {timer_text}")
        else:
            st.info(f"### {timer_text}")
        
        # Auto-submit when time expires
        if remaining_seconds <= 0:
            st.error("⏰ TIME'S UP! Auto-submitting...")
            time.sleep(2)
            submit_exam()
            st.stop()
        
        # === PACING GUIDE ===
        total_q = len(st.session_state.exam_questions)
        answered = len(st.session_state.exam_answers)
        current_q = st.session_state.exam_current_q + 1  # 1-indexed
        
        # Calculate pacing
        timing = get_question_timing_guide()
        time_per_q = timing['time_per_question']  # ~76.7 seconds
        expected_time_used = current_q * time_per_q  # Expected time at this question
        actual_time_used = st.session_state.exam_elapsed
        
        # Pace status
        if actual_time_used < expected_time_used * 0.9:
            pace_status = "🟢 AHEAD"
            pace_color = "success"
        elif actual_time_used < expected_time_used * 1.1:
            pace_status = "🟡 ON TRACK"
            pace_color = "info"
        else:
            pace_status = "🔴 BEHIND"
            pace_color = "warning"
        
        # Show pacing guide
        pace_min = int(actual_time_used // 60)
        pace_secs = int(actual_time_used % 60)
        expected_min = int(expected_time_used // 60)
        expected_secs = int(expected_time_used % 60)
        
        with st.container():
            st.markdown(f"""
            <div style="background: #F0F9FF; border-left: 4px solid #0EA5E9; padding: 10px; border-radius: 4px; margin-bottom: 10px;">
                <strong>📊 Pacing Guide</strong><br>
                Q{current_q}/{total_q} | Time used: {pace_min}:{pace_secs:02d} | Expected: {expected_min}:{expected_secs:02d} | <strong>{pace_status}</strong><br>
                <small>Target: ~{time_per_q:.0f} seconds per question | {timing['total_time']} min total</small>
            </div>
            """, unsafe_allow_html=True)
        
        # Progress
        st.progress(answered / total_q, text=f"Answered: {answered}/{total_q}")
        
        # === BREAK REMINDERS ===
        # Break 1: After question 60 (or scaled for smaller exams)
        break_1_trigger = max(1, int(total_q * (60 / 180)))
        break_2_trigger = max(1, int(total_q * (120 / 180)))
        
        if current_q >= break_1_trigger and not st.session_state.break_1_taken:
            st.success(f"🛑 **Break 1:** You've answered {current_q} questions. Take a 10-minute break?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("☕ Take Break", use_container_width=True):
                    st.session_state.break_1_taken = True
                    start_break()
            with col2:
                if st.button("▶️ Continue", use_container_width=True):
                    st.session_state.break_1_taken = True  # Mark as taken even if skipped
                    st.rerun()
        
        elif current_q >= break_2_trigger and not st.session_state.break_2_taken:
            st.success(f"🛑 **Break 2:** You've answered {current_q} questions. Take your final 10-minute break?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("☕ Take Break", key="break2", use_container_width=True):
                    st.session_state.break_2_taken = True
                    start_break()
            with col2:
                if st.button("▶️ Continue", key="continue2", use_container_width=True):
                    st.session_state.break_2_taken = True
                    st.rerun()
        
        # Question navigator
        st.caption("Jump to question:")
        cols_per_row = 10
        rows = (total_q + cols_per_row - 1) // cols_per_row
        
        for row in range(rows):
            cols = st.columns(cols_per_row)
            for col_idx in range(cols_per_row):
                q_idx = row * cols_per_row + col_idx
                if q_idx < total_q:
                    q_id = st.session_state.exam_questions[q_idx].get('id', str(q_idx))
                    is_answered = q_id in st.session_state.exam_answers
                    is_flagged = q_id in st.session_state.questions_flagged
                    is_current = q_idx == st.session_state.exam_current_q
                    
                    # Color coding
                    if is_current:
                        label = f"[{q_idx+1}]"
                    elif is_flagged:
                        label = f"🚩{q_idx+1}"
                    elif is_answered:
                        label = f"✓{q_idx+1}"
                    else:
                        label = f"{q_idx+1}"
                    
                    with cols[col_idx]:
                        btn_type = "primary" if is_current else "secondary"
                        if st.button(label, key=f"nav_{q_idx}", type=btn_type, use_container_width=True):
                            st.session_state.exam_current_q = q_idx
                            st.rerun()
        
        st.markdown("---")
        
        # Current question
        q_idx = st.session_state.exam_current_q
        if q_idx < total_q:
            q = st.session_state.exam_questions[q_idx]
            
            st.markdown(f"**Question {q_idx + 1} of {total_q}** | Domain: `{q.get('domain', 'unknown').upper()}`")
            
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
            
            # Navigation buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                if q_idx > 0:
                    if st.button("⬅️ Previous", use_container_width=True):
                        st.session_state.exam_current_q = q_idx - 1
                        st.rerun()
            with col2:
                # Flag button
                is_flagged = q_id in st.session_state.questions_flagged
                if st.button("🚩 Flag" if not is_flagged else "🚩 Flagged", key=f"flag_{q_id}", use_container_width=True):
                    if is_flagged:
                        st.session_state.questions_flagged.remove(q_id)
                    else:
                        st.session_state.questions_flagged.append(q_id)
                    save_progress()
                    st.rerun()
            with col3:
                if q_idx + 1 < total_q:
                    if st.button("Next ➡️", use_container_width=True):
                        st.session_state.exam_current_q = q_idx + 1
                        st.rerun()
        
        # Submit button
        if answered == total_q:
            st.success("✅ All questions answered!")
        
        if st.button("📊 Submit Exam", use_container_width=True, type="primary"):
            submit_exam()
    
    else:
        # Results
        correct = sum(1 for ans in st.session_state.exam_answers.values() if ans.get('correct', False))
        total = len(st.session_state.exam_answers)
        score = calculate_score(correct, total)
        threshold = get_passing_threshold()
        passed = is_passing(score, threshold)
        elapsed_min = st.session_state.exam_elapsed // 60
        
        # Result banner
        if passed:
            st.success(f"🎉 PASSED! Score: {score}% ({correct}/{total})")
        else:
            st.error(f"❌ Did Not Pass. Score: {score}% ({correct}/{total})")
            st.info(f"Passing score: {threshold}%")
        
        st.metric("Time Used", f"{elapsed_min} minutes", f"of {format_duration(get_exam_duration_minutes())}")
        
        # Pacing analysis
        timing = get_question_timing_guide()
        avg_time = st.session_state.exam_elapsed / total if total > 0 else 0
        target_time = timing['time_per_question']
        
        if avg_time <= target_time * 1.1:
            st.success(f"⏱️ Pacing: Good! Average {avg_time:.0f}s/question (target: {target_time:.0f}s)")
        elif avg_time <= target_time * 1.3:
            st.warning(f"⏱️ Pacing: Slow. Average {avg_time:.0f}s/question (target: {target_time:.0f}s)")
        else:
            st.error(f"⏱️ Pacing: Too slow! Average {avg_time:.0f}s/question (target: {target_time:.0f}s)")
        
        # Domain breakdown
        answers_list = [
            {'domain': ans['domain'], 'correct': ans['correct']}
            for ans in st.session_state.exam_answers.values()
        ]
        breakdown = domain_breakdown(answers_list)
        
        if breakdown:
            st.subheader("Domain Performance")
            domains = get_domain_breakdown()
            
            for domain_key, stats in breakdown.items():
                domain_info = domains['current'].get(domain_key, {})
                target_pct = domain_info.get('pct', 0)
                actual_pct = stats['pct']
                
                if actual_pct >= target_pct:
                    status = "🟢"
                elif actual_pct >= target_pct - 10:
                    status = "🟡"
                else:
                    status = "🔴"
                
                st.markdown(f"{status} **{domain_key.upper()}:** {stats['correct']}/{stats['total']} ({actual_pct}%) — Target: {target_pct}%")
        
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
