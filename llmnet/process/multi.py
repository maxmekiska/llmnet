import multiprocessing
from typing import Callable, List

from llmnet.observer.tracker import track


def process_single_prompt(set_prompt: str, llmbot: Callable, args, kwargs) -> str:
    track.info(f"Processing text: {set_prompt}")
    result = llmbot(set_prompt=set_prompt, *args, **kwargs)
    track.info(f"Completed processing for text: {set_prompt}")
    return result


def process_prompts(
    set_prompts: List[str],
    llmbot: Callable,
    max_concurrent_worker: int,
    *args,
    **kwargs,
) -> List[str]:
    with multiprocessing.Pool(processes=max_concurrent_worker) as pool:
        track.info(
            f"Processing {len(set_prompts)} prompts with {max_concurrent_worker} concurrent workers"
        )
        arg_tuples = [(prompt, llmbot, args, kwargs) for prompt in set_prompts]
        results = pool.starmap(process_single_prompt, arg_tuples)

    return results
