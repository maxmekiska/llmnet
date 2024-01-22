import re
from typing import List


def combine_sentences(
    sentences: List[str],
    token_word_ratio: float,
    token_limit: float,
    min_sentences_count: int,
):
    total_tokens = 0.0
    combined_sentences = []
    current_sentence = ""

    for sentence in sentences:
        tokens = len(sentence.split()) / token_word_ratio  # Estimate number of tokens

        if len(current_sentence.split(".")) >= min_sentences_count:
            if total_tokens + tokens > token_limit:
                combined_sentences.append(current_sentence.strip())
                total_tokens = 0.0
                current_sentence = ""

        current_sentence += " " + sentence.strip()
        total_tokens += tokens

    if current_sentence.strip():
        combined_sentences.append(current_sentence.strip())

    return combined_sentences


def remove_space_before_split_operator(text: str) -> str:
    result = re.sub(r"\s*([.!?;])", r"\1", text)
    return result


def remove_whitespaces(text: str) -> str:
    result = re.sub(r"\s+", " ", text)
    return result


def remove_space_after_split_operator(text: str) -> str:
    result = re.sub(r"([.!?;])(?!\s)", r"\1 ", text)
    return result


def strip_text(text: str) -> str:
    result = text.strip()
    return result


def remove_line_breaks(text: str) -> str:
    result = text.replace("\n", " ")
    return result


def split_text_after_split_operator(text: str) -> List[str]:
    result = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=[.!?;])\s", text)
    return result


def clean_split(text: str) -> List[str]:
    step = remove_space_before_split_operator(text)
    step = remove_whitespaces(step)
    step = remove_space_after_split_operator(step)
    step = strip_text(step)
    step = remove_line_breaks(step)
    result = split_text_after_split_operator(step)
    return result
