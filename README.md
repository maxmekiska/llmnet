# `llmnet`

llmnet is a python library designed to facilitate collaborative work among LLMs on diverse tasks. Its primary goal is to encourage a diversity of thought across various LLM models.

llmnet comprises two main components:

1. LLM network workers
2. Consensus worker


The LLM network workers can independently and concurrently process tasks, while the consensus worker can access the various solutions and generate a final output. It's important to note that the consensus worker is optional and doesn't necessarily need to be employed.

## Example

### Prerequisite

llmnet currently supports LLM models from OpenAI and Google. The user can define the model to be used for the LLM workers, as well as the model to be used for the consensus worker.

Please make sure to set env variables called `OPENAI_API_KEY`, `GOOGLE_API_KEY` to your OpenAi and Google keys.

### How to use llmnet?

#### llm worker

You have currently three llm worker at your disposal:

1. openaillmbot
2. googlellmbot
3. randomllmbot

##### `openaillmbot`

Interface with OpenAi models.

optional parameters:

```
model         (str) = 'gpt-3.5-turbo'
max_tokens    (int) = 2024
temperature   (float) = 0.1
n             (int) = 1
stop          (Union[str, List[str]]) = None
```

##### `googlellmbot`

Interface with Google models.

optional parameters:

```
model               (str) = 'gemini-pro'
max_output_tokens   (int) = 2024
temperature         (float) = 0.1
top_p               (float) = None
top_k               (int) = None
candidate_count     (int) = 1
stop_sequences      (str) = None
```

##### `randomllmbot`

Select randomly between all available llmworkers and parameter specified.

optional parameters:

```
random_configuration  (Dict) = {}
```

example dict:

```
{
    "<worker1>":
    {
        "<parameter1>": [<possible_arguments>],
        "<parameter2>": [<possible_arguments>],
        ...
    },
    "<worker2>":
    {
        "<parameter1>": [<possible_arguments>],
        "<parameter2>": [<possible_arguments>]
        ...
    }
    ...
}
```

##### `randomopenaillmbot`

optional parameters - if not provided, defaults to `openaillmbot` default values:

```
random_configuration  (Dict) = {}
```

example dict:

```
{
    "<parameter1>": [<possible_arguments>],
    "<parameter2>": [<possible_arguments>],
    ...
}
```


##### `randomgooglellmbot`

optional parameters - if not provided, defaults to `googlellmbot` default values:

```
random_configuration  (Dict) = {}
```

example dict:

```
{
    "<parameter1>": [<possible_arguments],
    "<parameter2>": [<possible_arguments],
    ...
}
```
#### `create_network`

- creates llmworker network
- expects:
  - instruct: List[Dict[str, str]]
    - structure: `[{"objective": xxx, "context": ooo}..]`, the context key is is optional
  - worker: select any worker from the above
  - max_concurrent_worker: how many API calls are allowed in parallel
  - kwargs: any configuration for the worker selected
  - access results via getter methods:
    - get_worker_answers: collection of answers combined in one string
    - get_worker_answers_messages: collection of answers with metadata

#### `apply_consensus`

- creates consensus worker
- expects:
  - worker: select any worker from the above
  - kwargs: any configuration for the worker selected
  - set_prompt: prompt to build consensus
    - access results via getter methods:
      - get_worker_consensus: consensus result as string
      - get_worker_consensus_messages: consensus result with metadata

#### Simple independent tasks - no consensus

```python
from llmnet import LlmNetwork


instructions = []


instructions =
    [
    {"objective": "how many countries are there?"},
    {"objective": "what is AGI"},
    {"objective": "What is the purpose of biological life?"}
    ]

net = LlmNetwork()

net.create_network(
    instruct=instructions,
    worker="randomllmbot",
    max_concurrent_worker=2, # how many API calls are allowed in parallel
    random_configuration={
        "googlellmbot": {"model": ["gemini-pro"], "temperature": [0.12, 0.11]},
        "openaillmbot": {
            "model": ["gpt-3.5-turbo", "gpt-4"],
            "temperature": [0.11, 0.45, 1],
        },
    },
)

# collection of answers as a string
net.get_worker_answers

# collection of answers with metadata
net.get_worker_answer_messages
```

#### One task with same objective split between multiple workers - consensus

```python
from llmnet import LlmNetwork


instructions = []


instructions =
    [
    {"objective": "What is empiricism?", "context": "Text Part One"},
    {"objective": "What is empiricism?", "context": "Text Part Two"},
    {"objective": "What is empiricism?", "context": "Text Part Three"}
    ]

net = LlmNetwork()

net.create_network(
    instruct=instructions,
    worker="randomllmbot",
    max_concurrent_worker=2, # how many API calls are allowed in parallel
    random_configuration={
        "googlellmbot": {"model": ["gemini-pro"], "temperature": [0.12, 0.11]},
        "openaillmbot": {
            "model": ["gpt-3.5-turbo"],
            "temperature": [0.11, 0.45, 1],
        },
    },
)

# collection of answers as a string
net.get_worker_answers

# collection of answers with metadata
net.get_worker_answer_messages

# apply consensus
net.apply_consensus(
    worker="openaillmbot",
    model="gpt-3.5-turbo",
    temperature=0.7,
    set_prompt=f"Answer this objective: What is empiricism? with the following text in just one sentences: {net.get_worker_answers}",
)

# get final consensus answer as a string
net.get_worker_consensus

# get answer with metadata
net.get_worker_consensus_messages
```

#### Other example use cases

- independent objectives, choose best solution via consensus
- mixed objectives with and without context, with or without consensus
- etc.

## Appendix

Please consider looking at alternative implementations such as Map reduce by LangChain: [LangChain MapReduce Documentation](https://python.langchain.com/docs/modules/chains/document/map_reduce)
