import streamlit as st
from data.flashcards import FLASHCARDS
from utils.state import save_progress

st.set_page_config(page_title="🗂️ Flashcards", page_icon="🗂️", layout="centered")

st.title("🗂️ Flashcards")
st.caption(f"{len(FLASHCARDS)} cards to master")

# Initialize flashcard state
if 'fc_index' not in st.session_state:
    st.session_state.fc_index = 0
if 'fc_show_back' not in st.session_state:
    st.session_state.fc_show_back = False
if 'fc_filtered' not in st.session_state:
    st.session_state.fc_filtered = FLASHCARDS.copy()
if 'fc_shuffled' not in st.session_state:
    st.session_state.fc_shuffled = False

def reset_flashcards():
    st.session_state.fc_index = 0
    st.session_state.fc_show_back = False
    st.session_state.fc_shuffled = False
    st.rerun()

def next_card():
    st.session_state.fc_index = (st.session_state.fc_index + 1) % len(st.session_state.fc_filtered)
    st.session_state.fc_show_back = False
    st.rerun()

def prev_card():
    st.session_state.fc_index = (st.session_state.fc_index - 1) % len(st.session_state.fc_filtered)
    st.session_state.fc_show_back = False
    st.rerun()

def flip_card():
    st.session_state.fc_show_back = not st.session_state.fc_show_back
    st.rerun()

def mark_known():
    card = st.session_state.fc_filtered[st.session_state.fc_index]
    card_id = card.get('id', str(st.session_state.fc_index))
    if card_id not in st.session_state.flashcards_known:
        st.session_state.flashcards_known.append(card_id)
        if card_id in st.session_state.flashcards_review:
            st.session_state.flashcards_review.remove(card_id)
        save_progress()
    next_card()

def mark_review():
    card = st.session_state.fc_filtered[st.session_state.fc_index]
    card_id = card.get('id', str(st.session_state.fc_index))
    if card_id not in st.session_state.flashcards_review:
        st.session_state.flashcards_review.append(card_id)
        if card_id in st.session_state.flashcards_known:
            st.session_state.flashcards_known.remove(card_id)
        save_progress()
    next_card()

def shuffle_cards():
    import random
    st.session_state.fc_filtered = random.sample(st.session_state.fc_filtered, len(st.session_state.fc_filtered))
    st.session_state.fc_shuffled = True
    st.session_state.fc_index = 0
    st.session_state.fc_show_back = False
    st.rerun()

# Category filter
categories = list(set(f.get('category', 'General') for f in FLASHCARDS))
selected_cats = st.multiselect("Filter by category", categories, default=categories)

# Apply filter
filtered = [f for f in FLASHCARDS if f.get('category', 'General') in selected_cats]
if filtered != st.session_state.fc_filtered:
    st.session_state.fc_filtered = filtered
    st.session_state.fc_index = 0
    st.session_state.fc_show_back = False

# Progress stats
known_count = len(st.session_state.flashcards_known)
review_count = len(st.session_state.flashcards_review)
total_count = len(FLASHCARDS)

st.markdown(f"**Progress:** {known_count} known | {review_count} needs review | {total_count} total")

if st.session_state.fc_filtered:
    # Card display
    card = st.session_state.fc_filtered[st.session_state.fc_index]
    card_num = st.session_state.fc_index + 1
    total_display = len(st.session_state.fc_filtered)
    
    st.progress(card_num / total_display, text=f"Card {card_num}/{total_display}")
    
    # Card container
    with st.container():
        st.markdown(f"**Category:** {card.get('category', 'General')}")
        
        if not st.session_state.fc_show_back:
            # Front of card
            st.markdown("## 🎴 Front")
            st.markdown(f"### {card.get('front', 'No front text')}")
            
            if st.button("🔃 Flip Card", use_container_width=True, type="primary"):
                flip_card()
        else:
            # Back of card
            st.markdown("## 📖 Back")
            st.markdown(f"### {card.get('back', 'No back text')}")
            
            if card.get('formula'):
                st.latex(card['formula'])
            
            # Mark buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Known", use_container_width=True, type="primary"):
                    mark_known()
            with col2:
                if st.button("🔴 Needs Review", use_container_width=True):
                    mark_review()
    
    # Navigation
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅️ Previous", use_container_width=True):
            prev_card()
    with col2:
        if st.button("🔃 Flip", use_container_width=True):
            flip_card()
    with col3:
        if st.button("Next ➡️", use_container_width=True):
            next_card()
    
    # Shuffle
    if st.button("🔀 Shuffle Cards", use_container_width=True):
        shuffle_cards()

else:
    st.warning("No flashcards match the selected filters.")

if st.button("🔄 Reset Progress", use_container_width=True):
    st.session_state.flashcards_known = []
    st.session_state.flashcards_review = []
    save_progress()
    reset_flashcards()
