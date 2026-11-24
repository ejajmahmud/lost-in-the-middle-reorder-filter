"""Core Primacy-Recency Reorderer implementation."""
from typing import List

class ContextItem:
    def __init__(self, item_id: str, content: str, score: float):
        self.item_id = item_id
        self.content = content
        self.score = score

class PrimacyRecencyReorderer:
    @classmethod
    def reorder(cls, items: List[ContextItem]) -> List[ContextItem]:
        if len(items) <= 2:
            return sorted(items, key=lambda x: x.score, reverse=True)

        sorted_items = sorted(items, key=lambda x: x.score, reverse=True)
        reordered = [None] * len(sorted_items)

        left = 0
        right = len(sorted_items) - 1

        for i, item in enumerate(sorted_items):
            if i % 2 == 0:
                reordered[left] = item
                left += 1
            else:
                reordered[right] = item
                right -= 1

        return reordered
