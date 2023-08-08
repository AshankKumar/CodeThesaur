from openai_function_call import OpenAISchema
from pydantic import Field

class githubProject(OpenAISchema):
    "Correctly extracted information from a github project"
    projectName: str = Field(..., description="Project's full name")
    url: str = Field(..., description="Project's url")
    author: str = Field(..., description="Project's author")
    description: str = Field(..., description="A short summary describing the project")

data = {
    "results": [
        {
            "url": "https://github.com/theskumar/python-dotenv",
            "title": "GitHub - theskumar/python-dotenv: Reads key-value pairs from a .env file and can set them as environment variables. It helps in developing applications following the 12-factor principles.",
            "publishedDate": "2023-01-21",
            "author": "Theskumar",
            "score": 0.22716157138347626,
            "id": "dL3l_a4kszaoXGr8HQcJfQ"
        },
        {
            "url": "https://github.com/mattseymour/python-env",
            "title": "GitHub - mattseymour/python-env: Read .env file (key->value) setting values as environment variables",
            "publishedDate": "2023-01-01",
            "author": "Mattseymour",
            "score": 0.22165727615356445,
            "id": "kwGgQhc5GhfjXZwEIB4y8A"
        },
        {
            "url": "https://github.com/matthiask/speckenv",
            "title": "GitHub - matthiask/speckenv: Load environment from .env. Includes some optional Django goodies.",
            "publishedDate": "2023-01-01",
            "author": "Matthiask",
            "score": 0.21084490418434143,
            "id": "UdB031wH_kucP472lxDhDw"
        },
        {
            "url": "https://github.com/grauwoelfchen/flask-dotenv",
            "title": "GitHub - grauwoelfchen/flask-dotenv: The .env file support for Flask Config",
            "publishedDate": "2019-04-30",
            "author": "Grauwoelfchen",
            "score": 0.2098427712917328,
            "id": "3zFhcKkgTDlF3W9IR4RRHg"
        },
        {
            "url": "https://github.com/tonyseek/python-envcfg",
            "title": "GitHub - tonyseek/python-envcfg: For 12-factor apps - retrieve config from envvars.",
            "publishedDate": "2023-01-04",
            "author": "Tonyseek",
            "score": 0.20901700854301453,
            "id": "KO3gx8LuKOQfzzropX8bMw"
        },
        {
            "url": "https://github.com/HBNetwork/python-decouple",
            "title": "GitHub - HBNetwork/python-decouple: Strict separation of config from code.",
            "publishedDate": "2023-01-09",
            "author": "HBNetwork",
            "score": 0.206697478890419,
            "id": "sBKccjy5V8sX20dncz5USw"
        },
        {
            "url": "https://github.com/alexmojaki/dryenv",
            "title": "GitHub - alexmojaki/dryenv: Simple DRY configuration with environment variables and pydantic",
            "publishedDate": "2023-01-01",
            "author": "Alexmojaki",
            "score": 0.20606809854507446,
            "id": "oOnxBRCVK-fub8SJyZYHCA"
        },
        {
            "url": "https://github.com/DataDog/envier",
            "title": "GitHub - DataDog/envier: Python application configuration from the environment",
            "publishedDate": "2022-08-17",
            "author": "DataDog",
            "score": 0.20576900243759155,
            "id": "g5FF1Q4oYbFS154aPflcSg"
        },
        {
            "url": "https://github.com/ahoward/senv",
            "title": "GitHub - ahoward/senv: the 12-factor environment tool your mother told you to use",
            "publishedDate": "2023-01-01",
            "author": "Ahoward",
            "score": 0.20369938015937805,
            "id": "AxvT7JBL0Yr9kZt-77i6jw"
        },
        {
            "url": "https://github.com/carljm/fern",
            "title": "GitHub - carljm/fern: Yet another env config parser.",
            "publishedDate": "2023-01-01",
            "author": "Carljm",
            "score": 0.2029780149459839,
            "id": "8WFpEMn3c_8tH-OJioLWdg"
        }
    ]
}