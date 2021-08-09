import json
import os

from task_interfaces import TaskInterface, SubscriptionLevels, TaskTypes


class Task(TaskInterface):
    """
    Verifies shell scripts follow best practices.
    """

    name = "ShellCheck"
    slug = "shellcheck"
    pass_summary = ""
    pass_text = ""
    fail_summary = "All files not formatted correctly."
    fail_text = ""
    subscription_level = SubscriptionLevels.FREE
    actions = None
    type = TaskTypes.CODE_FORMAT


    command = "shellcheck"
    file_filters = ".*.sh$"

    def execute(self, github_body, settings) -> bool:
        pass
