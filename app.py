
import os
import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
from google import genai
from career_matcher import calculate_career_matches

# -------------------- CONFIGURATION --------------------

st.set_page_config(
    page_title="AI Career Guidance Platform",
    page_icon="🎯",
    layout="wide"
)

load_dotenv()

st.title("🎯 AI Career Guidance Platform")
st.write(
    "Discover suitable career paths, identify skill gaps, "
    "and build your personalized learning roadmap with AI."
)

api_key = os.getenv("GEMINI_API_KEY")

# -------------------- SIDEBAR --------------------

with st.sidebar:
    st.header("About This Platform")
    st.write(
        "This platform combines rule-based career matching "
        "with Google Gemini AI to provide personalized career guidance."
    )

    st.divider()
    st.caption("Built with Python, Streamlit, and Gemini AI")


# -------------------- PROFILE INPUT --------------------

st.header("👤 Your Career Profile")

with st.form("career_profile_form"):

    name = st.text_input("Your Name")

    education = st.selectbox(
        "Current Education",
        [
            "Intermediate",
            "Diploma",
            "B.Tech / B.E.",
            "B.Sc",
            "BCA",
            "B.Com",
            "BBA",
            "M.Tech / M.E.",
            "M.Sc",
            "MCA",
            "Other"
        ]
    )

    branch = st.text_input(
        "Branch / Specialization",
        placeholder="Example: Artificial Intelligence and Machine Learning"
    )

    skills = st.multiselect(
        "Skills You Currently Have",
        [
            "Python",
            "C Programming",
            "Java",
            "SQL",
            "Data Analysis",
            "Machine Learning",
            "Deep Learning",
            "Web Development",
            "HTML",
            "CSS",
            "JavaScript",
            "Excel",
            "Communication",
            "Problem Solving",
            "Statistics",
            "Networking",
            "Cybersecurity"
        ]
    )

    interests = st.multiselect(
        "Your Interests",
        [
            "Artificial Intelligence",
            "Data Science",
            "Software Development",
            "Data Analytics",
            "Cybersecurity",
            "Web Development",
            "Cloud Computing",
            "Research",
            "Business"
        ]
    )

    goal = st.selectbox(
        "Your Career Goal",
        [
            "Get a job",
            "Get an internship",
            "Prepare for placements",
            "Build advanced technical skills",
            "Pursue higher studies",
            "Explore career options"
        ]
    )

    experience = st.selectbox(
        "Experience Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    submitted = st.form_submit_button(
        "🚀 Generate My Career Plan",
        type="primary",
        use_container_width=True
    )


# -------------------- PROCESS PROFILE --------------------

if submitted:

    if not name.strip():
        st.error("Please enter your name.")

    elif not interests:
        st.error("Please select at least one interest.")

    elif not api_key:
        st.error(
            "GEMINI_API_KEY was not found. Check your .env file "
            "and make sure the key is named GEMINI_API_KEY."
        )

    else:
        try:
            with st.spinner("Analyzing your profile and generating your career plan..."):

                # Rule-based career matching
                matches = calculate_career_matches(
                    skills,
                    interests
                )

                st.session_state["career_matches"] = matches
                st.session_state["profile_name"] = name.strip()

                # Gemini AI client
                client = genai.Client(api_key=api_key)

                prompt = f"""
You are an experienced AI career mentor.

Create a practical, personalized career guidance report using this profile.

Name: {name}
Education: {education}
Branch: {branch if branch.strip() else "Not specified"}
Current skills: {", ".join(skills) if skills else "Beginner with no selected skills"}
Interests: {", ".join(interests)}
Career goal: {goal}
Experience level: {experience}

Prepare the report using these sections:

1. PROFILE ANALYSIS
Summarize the person's current strengths and areas to improve.

2. TOP 3 CAREER OPTIONS
For each option, explain:
- Why it may suit this profile
- Typical entry-level job roles
- Important skills to learn
- How to begin as a beginner

3. PERSONALIZED SIX-MONTH LEARNING ROADMAP
Create a month-by-month plan with topics, practice activities, and measurable outcomes.

4. PROJECT RECOMMENDATIONS
Suggest three practical projects in increasing difficulty.
Explain the objective, technologies, and what each project demonstrates.

5. INTERVIEW PREPARATION
Give five relevant interview questions with concise sample answers.

6. NEXT SEVEN DAYS
Create a realistic day-by-day action plan.

7. RESUME AND PORTFOLIO
Suggest resume sections, GitHub portfolio improvements, and ways to demonstrate skills.

8. FINAL RECOMMENDATIONS
Give clear next steps suitable for this person's education and experience.

Be encouraging, realistic, specific, and beginner-friendly.
Avoid guaranteeing jobs, salaries, or placements.
Use clear headings and bullet points.
"""

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                st.session_state["career_plan"] = response.text

        except Exception as e:
            st.error("Unable to generate the career plan.")
            st.exception(e)


# -------------------- CAREER MATCHING DASHBOARD --------------------

if "career_matches" in st.session_state:

    st.divider()
    st.header("📊 Career Matching Dashboard")

    st.write(
        f"Career matches for **{st.session_state['profile_name']}**"
    )

    matches = st.session_state["career_matches"]

    if matches:

        top_career = matches[0]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Top Career Match",
                top_career["career"]
            )

        with col2:
            st.metric(
                "Overall Match Score",
                f'{top_career["match_score"]}%'
            )

        with col3:
            st.metric(
                "Careers Compared",
                len(matches)
            )

        st.caption(
            "Match scores are rule-based estimates using your selected "
            "skills and interests. They are not probabilities of getting a job."
        )

        chart_data = pd.DataFrame(matches)

        fig = px.bar(
            chart_data,
            x="career",
            y="match_score",
            color="match_score",
            range_y=[0, 100],
            text="match_score",
            title="Career Suitability Comparison",
            labels={
                "career": "Career Path",
                "match_score": "Match Score (%)"
            }
        )

        fig.update_traces(
            texttemplate="%{text}%",
            textposition="outside"
        )

        fig.update_layout(
            yaxis_title="Match Score (%)",
            xaxis_title="Career Path",
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Career-by-Career Analysis")

        for index, career in enumerate(matches, start=1):

            with st.expander(
                f'{index}. {career["career"]} — {career["match_score"]}% match'
            ):

                col1, col2 = st.columns(2)

                with col1:
                    st.write("**Skill Match**")
                    st.progress(
                        max(0, min(100, int(career["skill_score"]))) / 100
                    )
                    st.write(f'{career["skill_score"]}%')

                with col2:
                    st.write("**Interest Match**")
                    st.progress(
                        max(0, min(100, int(career["interest_score"]))) / 100
                    )
                    st.write(f'{career["interest_score"]}%')

                missing_skills = career.get("missing_skills", [])

                st.write("**Skills to Develop**")

                if missing_skills:
                    st.write(", ".join(missing_skills))
                else:
                    st.success(
                        "No missing skills identified by this matching model."
                    )


# -------------------- GEMINI CAREER REPORT --------------------

if "career_plan" in st.session_state:

    st.divider()
    st.header("🤖 Your Personalized AI Career Plan")

    st.markdown(st.session_state["career_plan"])

    st.download_button(
        label="📥 Download Career Plan",
        data=st.session_state["career_plan"],
        file_name="my_ai_career_plan.txt",
        mime="text/plain",
        use_container_width=True
    )


# -------------------- FOOTER --------------------

st.divider()

st.caption(
    "AI Career Guidance Platform | Python • Streamlit • Gemini AI • Plotly"
)
