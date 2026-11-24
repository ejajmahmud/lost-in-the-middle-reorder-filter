"""CLI for Lost-in-the-Middle Reorder Filter."""
import argparse
from .core import PrimacyRecencyReorderer, ContextItem

def main():
    parser = argparse.ArgumentParser(description="Lost-in-the-Middle Reorder Filter CLI")
    parser.add_argument("--demo", action="store_true", help="Run reordering demo")
    args = parser.parse_args()

    items = [ContextItem(f"doc-{i}", f"Content of doc {i}", float(i)) for i in range(1, 6)]
    reordered = PrimacyRecencyReorderer.reorder(items)

    print("Reordered for Primacy & Recency Placement:")
    for pos, it in enumerate(reordered):
        print(f"  Pos {pos+1}: {it.item_id} (Score: {it.score})")

if __name__ == "__main__":
    main()
