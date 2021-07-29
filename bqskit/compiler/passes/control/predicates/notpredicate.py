"""This module implements the NotPredicate class."""
from __future__ import annotations

import logging
from typing import Any

from bqskit.compiler.passes.control.predicate import PassPredicate
from bqskit.ir.circuit import Circuit

_logger = logging.getLogger(__name__)


class NotPredicate(PassPredicate):
    """
    The NotPredicate class.

    The NotPredicate takes a predicate and always returns the opposite truth
    value.
    """

    def __init__(self, predicate: PassPredicate) -> None:
        """
        Construct a NotPredicate.

        Args:
            predicate (PassPredicate): The predicate to invert.
        """

        if not isinstance(predicate, PassPredicate):
            raise TypeError('Expected PassPredicate, got %s.' % type(predicate))

        self.predicate = predicate

    def get_truth_value(self, circuit: Circuit, data: dict[str, Any]) -> bool:
        """Call this predicate, see PassPredicate for more info."""
        return not self.predicate(circuit, data)