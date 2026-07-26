from config.interview_questions import (
    TECHNICAL_QUESTIONS,
    HR_QUESTIONS,
    PROJECT_QUESTIONS,
    CODING_QUESTIONS,
)


class InterviewQuestionGenerator:

    def generate_questions(self, skills):
        technical = []

        if skills:
            for skill in skills:
                skill = skill.lower().strip()

                if skill in TECHNICAL_QUESTIONS:
                    technical.extend(TECHNICAL_QUESTIONS[skill])

        # Remove duplicate questions
        technical = list(dict.fromkeys(technical))

        # If no matching skill found
        if not technical:
            technical = [
                "Explain Object Oriented Programming.",
                "Difference between Compiler and Interpreter.",
                "Explain Git and GitHub."
            ]

        return {
            "technical": technical[:5],
            "hr": HR_QUESTIONS,
            "project": PROJECT_QUESTIONS,
            "coding": CODING_QUESTIONS
        }