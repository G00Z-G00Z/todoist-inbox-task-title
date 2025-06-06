#!/usr/bin/env -S uv run --script
"""This script scraps my inbox from todoist and copies the todoist inbox titles and details to my clipboard

This script essentially works for exporting todoist tasks from inbox to clipboard

Usefull links:
- Todoist API: https://developer.todoist.com/api/v1/
- Python SDK: https://doist.github.io/todoist-api-python/
"""

import os
from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
import pyperclip as clip
from todoist_api_python.models import Task

# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "dotenv>=0.9.9",
#     "httpx",
#     "pydantic",
#     "pyperclip>=1.9.0",
#     "todoist-api-python>=3.1.0",
# ]
# ///


def setup_api() -> TodoistAPI:
    load_dotenv()

    API_TOKEN = os.environ["TODOIST_API_TOKEN"]

    assert API_TOKEN, "The api token must be set up in .env file"

    API = TodoistAPI(API_TOKEN)

    return API


def task_to_str(task: Task) -> str:
    """Transform tasks to a text

    Args:
        task: Task from todoist

    Returns:
        str
    """

    text = task.content

    if task.description:
        text += f": {task.description}"

    return text


def main() -> None:
    api = setup_api()

    tasks = api.filter_tasks(query=r"#Inbox")

    text = ""

    for task_list in tasks:
        # Put all the text of the tasks into a text fie
        text += "\n".join([task_to_str(task) for task in task_list])

    clip.copy(text)
    print(text, end="\n\n")
    print("The text was copied to your clipboard")


if __name__ == "__main__":
    main()
