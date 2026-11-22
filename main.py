#!/usr/bin/env python3
"""Write the competition entry: one short plan for turning $100 into the
most money in 30 days, as an AI agent working alone.

The entry is a fixed string, so the program is fully deterministic: it
writes the same bytes on every run. Standard library only, no network.
"""

import os

ENTRY = (
    "Day 1: find 200 slow Shopify stores via BuiltWith's free tier, "
    "email each a $49 checkout-speed audit, paid by Stripe link, "
    "delivered in 24h. Days 2-30: deliver, upsell a $199 fix. "
    "Likely 10 sales = $490. Edge: stores already pay for speed; "
    "nobody audits them one by one."
)


def main() -> None:
    # Gate check: the entry must be 1-280 Unicode code points, not only
    # whitespace. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is only whitespace"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
