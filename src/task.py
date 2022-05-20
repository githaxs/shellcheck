import json
import os

from task_interfaces import StaticAnalysisTask, SubscriptionLevels


class Task(StaticAnalysisTask):
    """
    Verifies shell scripts follow best practices.
    """

    name = "ShellCheck"
    subscription_level = SubscriptionLevels.STARTUP
    source_script_path = "%s/task.sh" % os.path.dirname(__file__)