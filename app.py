import streamlit as st

st.set_page_config(
    page_title="Company Smart Interview Coach",
    page_icon="🎯",
    layout="wide"
)

# Sample Interview Question Bank
question_bank = {
    "Python Developer": [
        "What is Python? Explain its main features.",
        "What is the difference between a list and a tuple?",
        "What are Python functions? Explain with an example.",
        "What is object-oriented programming in Python?",
        "What is the difference between == and is in Python?"
    ],

    "Java Developer": [
        "What is Java? Explain its main features.",
        "What is the difference between JDK, JRE, and JVM?",
        "What is inheritance in Java?",
        "What is the difference between an abstract class and an interface?",
        "Explain exception handling in Java."
    ],

    "Data Analyst": [
        "What is data analysis?",
        "What is the difference between SQL and Excel?",
        "What is the difference between WHERE and HAVING in SQL?",
        "What is data visualization?",
        "How do you handle missing data in a dataset?"
    ],

    "Software Engineer": [
        "What is the software development life cycle?",
        "What is the difference between frontend and backend?",
        "What is a database?",
        "Explain the concept of debugging.",
        "What is version control? Explain Git."
    ]
}

# Application Title
st.title("🎯 Company-Smart Mock Interview Coach")

st.write(
    "Practice interviews and improve your placement preparation."
)

st.divider()

# Student Details
st.header("Student Details")

name = st.text_input("Enter your name")

company = st.selectbox(
    "Select Target Company",
    ["TCS", "Infosys", "Wipro", "Accenture"]
)

role = st.selectbox(
    "Select Job Role",
    [
        "Python Developer",
        "Java Developer",
        "Data Analyst",
        "Software Engineer"
    ]
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

st.divider()

# Start Interview
if st.button("Start Mock Interview"):

    if name.strip() == "":
        st.warning("Please enter your name.")

    else:
        st.session_state.started = True
        st.session_state.name = name
        st.session_state.company = company
        st.session_state.role = role
        st.session_state.difficulty = difficulty
        st.session_state.question_index = 0
        st.session_state.answers = []

        st.rerun()

# Interview Section
if st.session_state.get("started", False):

    questions = question_bank[st.session_state.role]

    st.header("🤖 Interviewer Agent")

    st.write("Student:", st.session_state.name)
    st.write("Company:", st.session_state.company)
    st.write("Role:", st.session_state.role)
    st.write("Difficulty:", st.session_state.difficulty)

    index = st.session_state.question_index

    # Ask questions one by one
    if index < len(questions):

        st.progress(index / len(questions))

        st.subheader(
            f"Question {index + 1} of {len(questions)}"
        )

        st.info(questions[index])

        answer = st.text_area(
            "Type your answer here:",
            key=f"answer_{index}",
            height=150
        )

        if st.button("Submit Answer"):

            if answer.strip() == "":
                st.warning("Please enter your answer.")

            else:
                st.session_state.answers.append({
                    "question": questions[index],
                    "answer": answer
                })

                st.session_state.question_index += 1

                st.rerun()

    # Interview Completed
    else:

        st.success("🎉 Interview Completed!")

        st.header("Your Interview Answers")

        for i, item in enumerate(
            st.session_state.answers
        ):

            st.subheader(f"Question {i + 1}")

            st.write(item["question"])

            st.write("Your Answer:")

            st.write(item["answer"])

            st.divider()

        st.info(
            "You have completed the mock interview. "
            "AI evaluation and personalised coaching "
            "will be added in the next step."
        )

        if st.button("Start New Interview"):

            st.session_state.started = False

            st.rerun()