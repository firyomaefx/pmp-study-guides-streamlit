import streamlit as st
from data.knowledge_areas import KNOWLEDGE_AREAS
from data.study_guides import STUDY_GUIDES
from utils.state import mark_section_read, is_section_read, get_ka_progress, save_progress

st.set_page_config(page_title="📖 Study Guides", page_icon="📖", layout="centered")

st.title("📖 Study Guides")
st.caption("Master all 10 Knowledge Areas — one process at a time")

# Knowledge Area selector
ka_names = [ka['name'] for ka in KNOWLEDGE_AREAS]
selected = st.selectbox("Select Knowledge Area", ka_names)

# Find selected KA
selected_ka = next(ka for ka in KNOWLEDGE_AREAS if ka['name'] == selected)
ka_id = selected_ka['id']
guide = STUDY_GUIDES.get(ka_id, {})

# Progress bar for this KA
processes = guide.get('processes', [])
total = len(processes)
read, _, pct = get_ka_progress(ka_id, total)

st.progress(pct, text=f"Progress: {read}/{total} processes studied")
st.markdown("---")

# Display processes
for i, process in enumerate(processes):
    process_id = process['id']
    already_read = is_section_read(ka_id, process_id)
    
    with st.expander(f"{process_id}: {process['name']}", expanded=(i==0)):
        # Description
        st.markdown(f"**Process Group:** {process['process_group']}")
        st.markdown(process['description'])
        
        # Mark as read button
        col1, col2 = st.columns([1, 3])
        with col1:
            if already_read:
                st.success("✓ Read")
            else:
                if st.button("✓ Mark Read", key=f"read_{ka_id}_{process_id}"):
                    mark_section_read(ka_id, process_id)
                    st.rerun()
        
        st.markdown("---")
        
        # ITTOs
        col_in, col_tt, col_out = st.columns(3)
        
        with col_in:
            st.markdown("**📥 Inputs**")
            for item in process.get('inputs', []):
                st.markdown(f"• {item}")
        
        with col_tt:
            st.markdown("**🔧 Tools & Techniques**")
            for item in process.get('tools_techniques', []):
                st.markdown(f"• {item}")
        
        with col_out:
            st.markdown("**📤 Outputs**")
            for item in process.get('outputs', []):
                st.markdown(f"• {item}")
        
        # Exam traps
        traps = process.get('exam_traps', [])
        if traps:
            st.markdown("---")
            st.markdown("**⚠️ Exam Traps**")
            for trap in traps:
                st.markdown(f"• {trap}")
        
        # Agile considerations
        agile = process.get('agile_considerations', [])
        if agile:
            st.markdown("---")
            st.markdown("**🔄 Agile Considerations**")
            for note in agile:
                st.markdown(f"• {note}")

# Key Formulas section
formulas = guide.get('key_formulas', [])
if formulas:
    st.markdown("---")
    st.subheader("📐 Key Formulas")
    
    for formula_group in formulas:
        st.markdown(f"**{formula_group['name']}**")
        for formula in formula_group.get('formulas', []):
            # Try to render as LaTeX if it looks like a formula
            if any(op in formula for op in ['=', '+', '-', '*', '/', 'Σ', '√']):
                # Extract the equation part
                if '=' in formula:
                    parts = formula.split('=', 1)
                    st.markdown(f"**{parts[0].strip()}**")
                    st.latex(parts[1].strip())
                else:
                    st.markdown(f"• {formula}")
            else:
                st.markdown(f"• {formula}")

# Exam tips
tips = guide.get('exam_tips', [])
if tips:
    st.markdown("---")
    st.subheader("💡 Exam Tips")
    for tip in tips:
        st.info(tip)
