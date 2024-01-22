import pytest

from .pre import (clean_split, combine_sentences,
                                    remove_line_breaks,
                                    remove_space_after_split_operator,
                                    remove_space_before_split_operator,
                                    remove_whitespaces,
                                    split_text_after_split_operator,
                                    strip_text)

sentences = [
    "The sky is blue today.",
    "I love eating sushi everyday.",
    "She plays the piano beautifully.",
    "The dog chased its tail.",
    "He ran through the park.",
    "The sun sets in the evening.",
    "I enjoy reading mystery novels.",
    "They went on a long journey.",
    "The cat jumped over me.",
    "She sings in the choir.",
    "The car drove down quickly.",
    "I like to swim underwater.",
    "He built a sandcastle yesterday.",
    "The rain poured heavily outside.",
    "She wrote a letter yesterday.",
    "The bird flew away quickly.",
]

optimal_batch_expected = [
    "The sky is blue today. I love eating sushi everyday. She plays the piano beautifully. The dog chased its tail.",
    "He ran through the park. The sun sets in the evening. I enjoy reading mystery novels. They went on a long journey.",
    "The cat jumped over me. She sings in the choir. The car drove down quickly. I like to swim underwater.",
    "He built a sandcastle yesterday. The rain poured heavily outside. She wrote a letter yesterday. The bird flew away quickly.",
]


def test_combine_sentences():
    optimal_batch = combine_sentences(
        sentences=sentences,
        token_word_ratio=0.75,
        token_limit=30,
        min_sentences_count=3,
    )
    assert optimal_batch == optimal_batch_expected


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Hello . World", "Hello. World"),
        ("This is a test !", "This is a test!"),
        ("Hello ; my name is John", "Hello; my name is John"),
        ("No spaces before . or !", "No spaces before. or!"),
        ("Multiple . . . . .", "Multiple....."),
    ],
)
def test_remove_space_before_split_operator(input_text, expected_output):
    assert remove_space_before_split_operator(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Hello     World", "Hello World"),
        ("This   is   a   test", "This is a test"),
        ("NoSpaces", "NoSpaces"),
        ("Multiple       spaces", "Multiple spaces"),
    ],
)
def test_remove_whitespaces(input_text, expected_output):
    assert remove_whitespaces(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Hello. World", "Hello. World"),
        ("This is a test!", "This is a test! "),
        ("Hello;my name is John", "Hello; my name is John"),
    ],
)
def test_remove_space_after_split_operator(input_text, expected_output):
    assert remove_space_after_split_operator(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("   Hello   ", "Hello"),
        ("   Leading and trailing spaces   ", "Leading and trailing spaces"),
        ("NoSpaces", "NoSpaces"),
        ("   ", ""),
        ("Single", "Single"),
    ],
)
def test_strip_text(input_text, expected_output):
    assert strip_text(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Hello\nWorld", "Hello World"),
        ("This\nis\na\ntest", "This is a test"),
        ("No line breaks", "No line breaks"),
        ("\n\n\n\n", "    "),
        ("Single", "Single"),
    ],
)
def test_remove_line_breaks(input_text, expected_output):
    assert remove_line_breaks(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Hello. World", ["Hello.", "World"]),
        ("This is a test!", ["This is a test!"]),
        ("Hello; my name is John", ["Hello;", "my name is John"]),
        ("No splits here", ["No splits here"]),
    ],
)
def test_split_text_after_split_operator(input_text, expected_output):
    assert split_text_after_split_operator(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Hello . World", ["Hello.", "World"]),
        ("This is a test !", ["This is a test!"]),
        ("Hello ; my name is John", ["Hello;", "my name is John"]),
        ("No spaces before . or !", ["No spaces before.", "or!"]),
    ],
)
def test_clean_split(input_text, expected_output):
    assert clean_split(input_text) == expected_output
