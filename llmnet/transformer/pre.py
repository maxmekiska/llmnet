import re
from typing import List


def combine_sentences(
    sentences: List[str],
    token_word_ratio: float,
    token_limit: int,
    min_sentences_count: int,
):
    total_tokens = 0
    combined_sentences = []
    current_sentence = ""

    for sentence in sentences:
        tokens = len(sentence.split()) / token_word_ratio  # Estimate number of tokens

        if len(current_sentence.split(".")) >= min_sentences_count:
            if total_tokens + tokens > token_limit:
                combined_sentences.append(current_sentence.strip())
                total_tokens = 0
                current_sentence = ""

        current_sentence += " " + sentence.strip()
        total_tokens += tokens

    if current_sentence.strip():
        combined_sentences.append(current_sentence.strip())

    return combined_sentences


def clean_split_text(text):
    cleaned_text = re.sub(r"\s+", " ", text)

    cleaned_text = re.sub(r"([.,!?;])(?!\s)", r"\1 ", cleaned_text)

    cleaned_text = cleaned_text.strip()

    cleaned_text = cleaned_text.replace("\n", " ")

    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=[.!?;])\s", cleaned_text)

    return sentences
