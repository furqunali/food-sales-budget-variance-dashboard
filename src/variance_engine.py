"""Reusable, deterministic budget-versus-actual variance calculations."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Variance:
    budget: float
    actual: float

    @property
    def amount(self) -> float:
        return self.actual - self.budget

    @property
    def percentage(self) -> float:
        if self.budget == 0:
            return 0.0 if self.actual == 0 else float("inf")
        return self.amount / self.budget * 100


def calculate(budget: float, actual: float) -> Variance:
    """Return a validated variance record."""
    budget, actual = float(budget), float(actual)
    return Variance(budget=budget, actual=actual)
