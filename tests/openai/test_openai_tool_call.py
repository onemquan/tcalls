from tcalls.openai_tool_call import get_openai_tool_schema


def search(query: str, engine: str = "google") -> str:
    """Search query from a online web."""
    return f"query: {query}\nresult: Large language models, also known as LLMs."


def func_test(a: int, b: float, c: str, d: dict, e: bool = False) -> str:
    """This is an example func_test.

    Args:
        a (int): The first parameter.
        b (float): The 2 parameter.
        c (:obj:`str`, optional): The 3 parameter.
        d: The 4 parameter.
        e: The 5 parameter.

    Returns:
        The return value.

    """
    return "return_func_test"


def get_weather(city: str) -> str:
    """Get the current weather temperature for a giving city."""
    return f"The {city} current weather temperature is 35 °C"


if __name__ == "__main__":
    print(get_openai_tool_schema(search))
    print(get_openai_tool_schema(func_test))
    print(get_openai_tool_schema(get_weather))
