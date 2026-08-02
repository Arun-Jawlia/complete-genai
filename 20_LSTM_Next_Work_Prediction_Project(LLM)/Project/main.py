# pylint: disable=all

import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Next Word Prediction",
    page_icon="✨",
    layout="wide",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#eef2ff,#ffffff);
}

.title {
    text-align:center;
    font-size:42px;
    font-weight:700;
    color:#4F46E5;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:30px;
}

.stButton>button{
    width:100%;
    background:#4F46E5;
    color:white;
    border-radius:12px;
    height:3em;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#3730A3;
}

.result-box{
    background:white;
    padding:20px;
    border-radius:15px;
    color: black;
    border-left:6px solid #4F46E5;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
    font-size:20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_resources():
    model = load_model("./models/next_word_model.h5")

    with open("./models/tokenizer.pkl", "rb") as file:
        tokenizer = pickle.load(file)

    return model, tokenizer


model, tokenizer = load_resources()

reverse_index = {
    idx: word
    for word, idx in tokenizer.word_index.items()
}

max_len = 44

# -----------------------------
# Title
# -----------------------------
st.markdown("<div class='title'>✨ Next Word Prediction</div>",
            unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>Generate text using a Deep Learning language model</div>",
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    num_words = st.slider(
        "Words to Generate",
        min_value=1,
        max_value=20,
        value=10,
    )

    st.info(
        """
        **How to use**

        1. Enter a starting sentence.
        2. Choose the number of words.
        3. Click **Generate**.
        """
    )

# -----------------------------
# Prediction Function
# -----------------------------
def generate_text(seed_text, num_words=10):

    text = seed_text

    for _ in range(num_words):
        seq = tokenizer.texts_to_sequences([text])[0]

        padded = pad_sequences(
            [seq],
            maxlen=max_len,
            padding="pre",
        )

        preds = model.predict(padded, verbose=0)

        pos = np.argmax(preds)

        next_word = reverse_index.get(pos, "")

        text += " " + next_word

    return text


# -----------------------------
# Input
# -----------------------------
seed = st.text_input(
    "📝 Enter Starting Text",
    placeholder="Example: Once upon a time",
)

col1, col2 = st.columns([1, 3])

with col1:
    generate = st.button("🚀 Generate Text")

with col2:
    st.write("")

# -----------------------------
# Output
# -----------------------------
if generate:

    if not seed.strip():
        st.warning("Please enter some starting text.")
    else:

        with st.spinner("Generating text..."):

            result = generate_text(seed, num_words)

        st.success("Prediction Complete!")

        st.markdown("### 📖 Generated Text")

        st.markdown(
            f"""
            <div class="result-box">
            {result}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.download_button(
            "📥 Download Result",
            result,
            file_name="generated_text.txt",
        )