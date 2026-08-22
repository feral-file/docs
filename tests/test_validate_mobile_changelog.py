import unittest

from scripts.validate_mobile_changelog import validate_mobile_changelog


class MobileChangelogValidationTest(unittest.TestCase):
    def test_accepts_the_canonical_entry_shape(self):
        errors = validate_mobile_changelog(
            """# Change logs

## Aug 22 2026

### Feral File Mobile App 1.5.5 — Clear release identity

Short canonical notes.

---

## Jul 16 2026

### Feral File Mobile App 1.3.4 — Previous release

Legacy notes may be longer than the current store limit.
"""
        )

        self.assertEqual(errors, [])

    def test_rejects_an_entry_without_a_date_section(self):
        errors = validate_mobile_changelog(
            """# Change logs

### Feral File Mobile App 2.0.0 — Orphaned

The app would not parse this entry.
"""
        )

        self.assertTrue(any("date section" in error for error in errors))

    def test_rejects_a_non_date_h2_section(self):
        errors = validate_mobile_changelog(
            """# Change logs

## Release Notes

### Feral File Mobile App 2.0.0 — Not actually dated

The app release parser would reject this entry.
"""
        )

        self.assertTrue(any("valid date section" in error for error in errors))

    def test_accepts_a_grandfathered_yearless_historical_date(self):
        errors = validate_mobile_changelog(
            """# Change logs

## Aug 22

### Feral File Mobile App 0.66.8 — Historical release

This predates the dated mobile changelog contract.
"""
        )

        self.assertEqual(errors, [])

    def test_rejects_duplicate_or_out_of_order_versions(self):
        errors = validate_mobile_changelog(
            """## Aug 22 2026
### Feral File Mobile App 1.5.5
First.
## Aug 21 2026
### Feral File Mobile App 1.6.0
Out of order.
## Aug 20 2026
### Feral File Mobile App 1.5.5
Duplicate.
"""
        )

        self.assertTrue(any("newest to oldest" in error for error in errors))
        self.assertTrue(any("Duplicate" in error for error in errors))

    def test_rejects_an_empty_or_overlong_latest_entry(self):
        empty_errors = validate_mobile_changelog(
            """## Aug 22 2026
### Feral File Mobile App 2.0.0
---
"""
        )
        long_errors = validate_mobile_changelog(
            """## Aug 22 2026
### Feral File Mobile App 2.0.0
{}
---
""".format("x" * 501)
        )

        self.assertTrue(any("empty" in error for error in empty_errors))
        self.assertTrue(any("500" in error for error in long_errors))


if __name__ == "__main__":
    unittest.main()
