__version__ = "0.0.1"

from llmnet.llms.chatgpt import llmbot, set_openai_key
from llmnet.observer.tracker import track
from llmnet.process.multi import process_prompts

if __name__ == "__main__":

    set_openai_key()

    example_prompts = [
        "What are you?",
        "How many countries are there in the world?",
        "Write a python function that prints hello world",
    ]

    print(
        process_prompts(
            worker=llmbot,
            set_prompts=example_prompts,
            model="gpt-3.5-turbo",
            temperature=0.7,
        )
    )
