from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from randovania.games.game import ProgressiveItemTuples


def tuples() -> ProgressiveItemTuples:
    return [
        ("Progressive Suit", ("Varia Suit", "Gravity Suit")),
        ("Progressive Jump", ("Hi-Jump Boots", "Space Jump")),
    ]
