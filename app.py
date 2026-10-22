
import streamlit as st
from main import prepare_action, execute_action

st.set_page_config(
    page_title="Approval-Based AI Agent",
    page_icon="🤖"
)

st.title("🤖 AI Approval-Based Agent")
st.write(
    "Generate a letter using AI, review it, "
    "and approve or reject it."
)

request = st.text_area(
    "Describe the letter you need",
    placeholder=(
        "Example: Prepare a two-day leave request "
        "for a family function."
    )
)

if "draft" not in st.session_state:
    st.session_state.draft = None

if "decision" not in st.session_state:
    st.session_state.decision = None

if st.button("Generate AI Draft"):
    if request.strip():
        try:
            with st.spinner("AI is generating your letter..."):
                st.session_state.draft = prepare_action(
                    request.strip()
                )
            st.session_state.decision = None
        except Exception:
            st.error(
                "The AI request failed. Check your API key, "
                "model access, and internet connection."
            )
    else:
        st.warning("Please enter your request.")

if st.session_state.draft is not None:
    st.subheader("Review the AI-Generated Letter")

    edited_draft = st.text_area(
        "Edit the letter before deciding:",
        value=st.session_state.draft,
        height=350,
        key="edited_draft"
    )

    st.info(
        "Check names, dates, and other details "
        "before approving."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Approve", use_container_width=True):
            st.session_state.decision = "approved"

    with col2:
        if st.button("Reject", use_container_width=True):
            st.session_state.decision = "rejected"

    if st.session_state.decision == "approved":
        execute_action(edited_draft)

        st.success("Approved! Your letter is ready.")

        st.download_button(
            "Download Approved Letter",
            data=edited_draft,
            file_name="approved_leave_request.txt",
            mime="text/plain"
        )

    elif st.session_state.decision == "rejected":
        st.error("Rejected. No action was executed.")
