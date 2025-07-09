import streamlit as st

# Initialize session state
if 'scores' not in st.session_state:
    st.session_state.scores = {
        'CID1_E': 0, 'CID1_M': 0,
        'CID2_R': 0, 'CID2_D': 0,
        'CID3_T': 0, 'CID3_A': 0,
        'CID4_F': 0, 'CID4_P': 0,
        'CID5_C': 0, 'CID5_F': 0,
        'CID6_L': 0, 'CID6_N': 0,
        'CID7_Re': 0, 'CID7_Dt': 0,
    }
    st.session_state.index = 0
    st.session_state.finished = False

# Sample test questions (we'll expand this later)
questions = [
    {
        "question": "How do you feel when someone sends you a long voice note?",
        "options": {
            "Excited! I love hearing people explain in detail.": {"CID3_A": 2},
            "Fine, I’ll usually listen and maybe skim.": {"CID3_A": 1},
            "Annoyed — I wish they’d text instead.": {"CID3_T": 2},
            "I often skip them entirely.": {"CID3_T": 3}
        }
    },
    {
        "question": "Do you overthink the tone or wording of messages you receive?",
        "options": {
            "Yes, I analyze every word.": {"CID7_Re": 3},
            "Sometimes, especially with certain people.": {"CID7_Re": 2},
            "Not really, I usually get the tone right.": {"CID7_Dt": 1},
            "Never, I take everything at face value.": {"CID7_Dt": 3}
        }
    }
]

# Display current question
if not st.session_state.finished:
    q = questions[st.session_state.index]
    st.write(f"**Q{st.session_state.index + 1}:** {q['question']}")
    choice = st.radio("Choose one:", list(q["options"].keys()))

    if st.button("Next"):
        for key, value in q["options"][choice].items():
            st.session_state.scores[key] += value
        st.session_state.index += 1
        if st.session_state.index >= len(questions):
            st.session_state.finished = True
        st.experimental_rerun()

# Show results after final question
else:
    st.header("Your Personality Test Result")
    result = ""
    for cid in range(1, 7 + 1):
        a = "E" if cid == 1 else "R" if cid == 2 else "T" if cid == 3 else "F" if cid == 4 else "C" if cid == 5 else "L" if cid == 6 else "Re"
        b = "M" if cid == 1 else "D" if cid == 2 else "A" if cid == 3 else "P" if cid == 4 else "F" if cid == 5 else "N" if cid == 6 else "Dt"
        pole_a = f"CID{cid}_{a}"
        pole_b = f"CID{cid}_{b}"
        score_a = st.session_state.scores[pole_a]
        score_b = st.session_state.scores[pole_b]
        selected = a if score_a >= score_b else b
        st.write(f"CID{cid}: **{selected}** ({a}: {score_a} | {b}: {score_b})")
        result += selected
    st.subheader(f"✨ Your CID Code: `{result}`")

