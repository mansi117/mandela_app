import os
import streamlit as st
from PIL import Image

# Dictionary of Mandela Effect examples
mandela_effect_images = {
    "coca_cola_logo": {
        "image1": "images/coca_cola_with_dash.jpg",
        "image2": "images/coca_cola_no_dash.jpg",
        "correct": "image1",
        "explanation": "The Coca-Cola logo never had a dash in between the words 'Coca' and 'Cola'."
    },
    "oreo_double_stuf": {
        "image1": "images/oreo_double_stuff.jpg",
        "image2": "images/oreo_double_stuf.jpg",
        "correct": "image2",
        "explanation": "Oreo has always spelled it 'Double Stuf' without an extra 'f' at the end."
    },
    "peace_symbol": {
        "image1": "images/peace_symbol_correct.jpg",
        "image2": "images/peace_symbol_incorrect.jpg",
        "correct": "image1",
        "explanation": "The peace symbol has a vertical line in the center, which has been part of its iconic design."
    },
    "pikachu_tail": {
        "image1": "images/pikachu_black_tail.jpg",
        "image2": "images/pikachu_no_black_tail.jpg",
        "correct": "image2",
        "explanation": "Pikachu has always had a solid yellow tail. It never had a black tip."
    },
    "starbucks_logo": {
        "image1": "images/starbucks_incorrect_logo.jpg",
        "image2": "images/starbucks_correct_logo.jpg",
        "correct": "image2",
        "explanation": "The Starbucks logo has always shown a two-tailed siren, never a single tail."
    },
    "volkswagen_logo": {
        "image1": "images/volkswagen_no_gap.jpg",
        "image2": "images/volkswagen_with_gap.jpg",
        "correct": "image2",
        "explanation": "The Volkswagen logo has always had a gap between the 'V' and 'W'."
    },
    "skechers_logo": {
        "image1": "images/skechers_correct.jpg",
        "image2": "images/sketchers_incorrect.jpg",
        "correct": "image1",
        "explanation": "The correct spelling is 'Skechers' with an 'E', not 'Sketchers'."
    },
    "kitkat_logo": {
        "image1": "images/kitkat_with_dash.jpg",
        "image2": "images/kitkat_no_dash.jpg",
        "correct": "image2",
        "explanation": "KitKat's logo has never had a dash between 'Kit' and 'Kat'."
    },
    "looney_tunes": {
        "image1": "images/looney_tunes.jpg",
        "image2": "images/looney_toons.jpg",
        "correct": "image1",
        "explanation": "The correct name is 'Looney Tunes' with a 'U', not 'Looney Toons'."
    },
    "seahorse_emoji": {
        "image1": "images/seahorse_emoji.jpg",
        "correct": "False",
        "explanation": "No, the Seahorse emoji does not exist in the current Unicode standard."
    },
    "shahenshah_dialogue": {
        "image": "images/amitabh_shahenshah.jpg",
        "option1": "Rishte mein toh hum tumhaare baap hote hai, naam hai Shahenshah.",
        "option2": "Rishte mein toh hum tumhaare baap lagte hai, naam hai Shahenshah.",
        "correct": "option",
        "explanation": "The correct dialogue is: 'Rishte mein toh hum tumhaare baap hote hai, naam hai Shahenshah.'"
    }
}

# Streamlit App Setup
st.title("Mandela Effect Quiz")
st.write("Can you identify the correct version of these famous logos, symbols, and scenes?")

# Quiz State Initialization
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = []

# List of questions
questions = list(mandela_effect_images.keys())

# Display progress bar
st.write("### Progress:")
progress = min(st.session_state.current_question / (len(questions) - 1), 1.0) if len(questions) > 1 else 1.0
st.progress(progress)

if st.session_state.current_question < len(questions):
    question = questions[st.session_state.current_question]
    data = mandela_effect_images[question]
    
    st.write(f"**Question {st.session_state.current_question + 1}: {question.replace('_', ' ').title()}**")
    
    if question == "seahorse_emoji":
        try:
            seahorse_image = Image.open(data["image1"]).resize((150, 150))
            st.image(seahorse_image, caption="Seahorse Emoji")
        except FileNotFoundError:
            st.error("Image not found for the Seahorse Emoji question.")
            
        if st.button("True", key=f"{question}_true"):
            user_choice = "True"
            is_correct = (user_choice == data["correct"])
            st.session_state.user_answers.append((question, user_choice, is_correct))
            if is_correct:
                st.session_state.score += 1
            st.session_state.current_question += 1
            
        if st.button("False", key=f"{question}_false"):
            user_choice = "False"
            is_correct = (user_choice == data["correct"])
            st.session_state.user_answers.append((question, user_choice, is_correct))
            if is_correct:
                st.session_state.score += 1
            st.session_state.current_question += 1
            
    elif question == "shahenshah_dialogue":
        st.write("Which version of this famous dialogue from the movie 'Shahenshah' is correct?")
        
        try:
            amitabh_image = Image.open(data["image"]).resize((400, 300))
            st.image(amitabh_image, caption="Amitabh Bachchan in Shahenshah")
        except FileNotFoundError:
            st.error("Image not found for Shahenshah question.")
            
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("Option 1:")
            st.write(f"_{data['option1']}_")
            if st.button("Choose Option 1", key=f"{question}_opt1"):
                user_choice = "option1"
                is_correct = (user_choice == data["correct"])
                st.session_state.user_answers.append((question, "Option 1", is_correct))
                if is_correct:
                    st.session_state.score += 1
                st.session_state.current_question += 1
                
        with col2:
            st.write("Option 2:")
            st.write(f"_{data['option2']}_")
            if st.button("Choose Option 2", key=f"{question}_opt2"):
                user_choice = "option2"
                is_correct = (user_choice == data["correct"])
                st.session_state.user_answers.append((question, "Option 2", is_correct))
                if is_correct:
                    st.session_state.score += 1
                st.session_state.current_question += 1
                
    else:
        col1, col2 = st.columns(2)
        with col1:
            try:
                img1 = Image.open(data["image1"]).resize((300, 300))
                st.image(img1, caption="Option 1")
                if st.button("Choose Option 1", key=f"{question}_1"):
                    user_choice = "image1"
                    is_correct = (user_choice == data["correct"])
                    st.session_state.user_answers.append((question, "Option 1", is_correct))
                    if is_correct:
                        st.session_state.score += 1
                    st.session_state.current_question += 1
            except FileNotFoundError:
                st.error(f"Image not found for Option 1 in the question {question}.")
                
        with col2:
            try:
                img2 = Image.open(data["image2"]).resize((300, 300))
                st.image(img2, caption="Option 2")
                if st.button("Choose Option 2", key=f"{question}_2"):
                    user_choice = "image2"
                    is_correct = (user_choice == data["correct"])
                    st.session_state.user_answers.append((question, "Option 2", is_correct))
                    if is_correct:
                        st.session_state.score += 1
                    st.session_state.current_question += 1
            except FileNotFoundError:
                st.error(f"Image not found for Option 2 in the question {question}.")
                
else:
    st.balloons()
    st.write(f"### Quiz Complete! 🎉 Your Score: {st.session_state.score}/{len(questions)}")
    
    st.write("### Detailed Feedback:")
    for question, answer, is_correct in st.session_state.user_answers:
        data = mandela_effect_images[question]
        st.write(f"**{question.replace('_', ' ').title()}**")
        st.write(f"Your answer: {answer}")
        st.write(f"{'✅ Correct!' if is_correct else '❌ Incorrect.'}")
        st.write(f"Explanation: {data['explanation']}")
        st.write("---")
