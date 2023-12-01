import streamlit as st

def get_sop_answer(question):
    # Define predefined questions and their corresponding answers
    sop_answers = {
        "What is the proper way to wipe down?": "The proper way to wipe down a surface is in unidirectional lines... If you have any other questions please feel free to either ask them here, or reach out to your nearest lead or quality manager",
        # Add more predefined questions and answers as needed
    }

    # Check if the question is in the predefined questions
    if question in sop_answers:
        return sop_answers[question]
    else:
        return "I can't seem to find the answer to that in the SOP. Please immediately reach out to your lead or QC. If you cannot find them, please let me know, and I will reach out to the first available QC on site. You can also contact your manager, John Doe at 555-555-5555, your quality manager, Jane Doe at 777-777-7777, or by email at john.doe@company.com and jane.doe@company.com"

def main():
    st.title("SOP Retrieval System")

    # User input
    user_query = st.text_input("Type your question here:")
    search_button = st.button("Search")

    if search_button:
        # Perform search using predefined questions and answers
        sop_answer = get_sop_answer(user_query)

        # Display result
        st.success(sop_answer)

if __name__ == "__main__":
    main()
