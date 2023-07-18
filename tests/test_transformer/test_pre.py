import pytest

from llmnet.transformer.pre import (clean_split, remove_line_breaks,
                                    remove_space_after_split_operator,
                                    remove_space_before_split_operator,
                                    remove_whitespaces,
                                    split_text_after_split_operator,
                                    strip_text)


def test_combine_sentences():
    pass


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
