from typing import NamedTuple, Dict, List
from collections import namedtuple


class LogItem(NamedTuple):
    """Value of metrics"""
    step: int
    value: float  # later, we want to support numpy arrays etc

class MainLogger:
    """Main logger"""
    def __init__(self):
        self.log_history: Dict[str, List[LogItem]] = {}
        self.groups: Dict[str, List[str]] = {}
        self.current_step: int = -1

    def update(self, logs: dict, i: int or None = None) -> None:
        """Update logs"""
        if i == None:
            self.current_step += 1
            i = self.current_step
        else:
            self.current_step = i

        for k, v in logs.items():
            if k not in self.log_history:
                self.log_history[k] = []
            self.log_history[k].append(LogItem(step=i, value=v))

    def grouped_log_history(self) -> Dict[str, Dict[str, List[LogItem]]]:
        return {group_name: {name: self.log_history[name] for name in names}
                for group_name, names in self.groups.items()}

    def reset(self) -> None:
        self.log_history = {}
        self.groups = {}
        self.current_step = -1
