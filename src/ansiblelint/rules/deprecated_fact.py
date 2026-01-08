"""Rule to detect deprecated ansible_<fact> names."""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ansiblelint.constants import INJECT_FACTS_AS_VARS_FACT_EXCEPTIONS
from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from ansiblelint.file_utils import Lintable  # noqa: F401
    from ansiblelint.utils import Task


class DeprecatedFactType(AnsibleLintRule):
    """Detect usage of deprecated ansible_<fact> names."""

    id = "deprecated-inject-fact-as-vars"
    description = "Deprecated ansible_<fact> used."
    severity = "MEDIUM"
    tags = ["deprecation"]

    def matchtask(
        self,
        task: Task,
        file: Optional["Lintable"] = None,  # noqa: F821
    ) -> bool | str:
        """Return a message if a deprecated fact is found."""
        for word in str(task).split():
            if (
                word.startswith("ansible_")
                and word not in INJECT_FACTS_AS_VARS_FACT_EXCEPTIONS
            ):
                return f"Deprecated fact name '{word}' used."
        return False