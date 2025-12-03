# Structured Outputs

This folder demonstrates how to generate **Structured Outputs** from LLMs using LangChain and Pydantic.

## Overview

LLMs typically output text, but for many applications, we need structured data (like JSON). This example shows how to enforce structured outputs using:
1.  **Pydantic Models**: Defining classes with type hints and descriptions.
2.  **TypedDict**: Using Python's `TypedDict` for type hinting.
3.  **JSON Schema**: Providing a raw JSON schema to the LLM.

## Code Structure

- `types.ipynb`: A Jupyter Notebook containing examples of:
    - Defining a `Country` Pydantic model.
    - Defining a `Joke` TypedDict.
    - Using a raw JSON schema for a joke.
    - Invoking `llm.with_structured_output()` to get structured responses.

## Examples

### Pydantic
```python
class Country(BaseModel):
    name: str = Field(description="name of the country")
    language: str = Field(description="language of the country")
    capital: str = Field(description="Capital of the country")

structured_llm = llm.with_structured_output(Country)
```

### TypedDict
```python
class Joke(TypedDict):
    setup: Annotated[str, ..., "The setup of the joke"]
    punchline: Annotated[str, ..., "The punchline of the joke"]
    rating: Annotated[Optional[int], None, "How funny the joke is, from 1 to 10"]

structured_llm = llm.with_structured_output(Joke)
```

## How to Run

Open `types.ipynb` in Jupyter Notebook or VS Code to run the cells.
