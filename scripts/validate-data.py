#!/usr/bin/env python3
"""Validate the static ESE Civil question bank before publishing."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "data/questions.json").read_text(encoding="utf-8"))
assert data.get("scope") == "technical_objective_prelims_only"
assert data.get("years") == list(range(2010, 2017))
questions = data.get("questions")
assert isinstance(questions, list)
seen = set()
for i, q in enumerate(questions, 1):
    required = ("id", "year", "paper_number", "question_number", "sequence_index",
                "question_text", "options", "verification_status", "source")
    missing = [key for key in required if key not in q]
    assert not missing, f"Question record {i} missing: {missing}"
    assert q["id"] not in seen, f"Duplicate question id: {q['id']}"
    seen.add(q["id"])
    assert 2010 <= int(q["year"]) <= 2016, f"Out-of-scope year in {q['id']}"
    assert q["paper_number"] in (1, 2), f"Out-of-scope paper in {q['id']}"
    assert q["verification_status"] == "VERIFIED", (
        f"Unverified record must not enter live bank: {q['id']}"
    )
    assert isinstance(q["question_text"], str) and q["question_text"].strip()
    assert isinstance(q["options"], list) and len(q["options"]) >= 2
    for option in q["options"]:
        assert option.get("key") and isinstance(option.get("text"), str)
    source = q["source"]
    assert source.get("title") and source.get("url") and source.get("page") is not None
    answer_key = q.get("answer_key")
    if answer_key:
        assert answer_key.get("status") in ("VERIFIED", "PROVISIONAL", "DISPUTED", "UNVERIFIED")
print(f"Validated {len(questions)} verified question records.")

# Confirm that the audit ledger covers every in-scope year/paper pair.
ledger = json.loads((root / "data/paper_audit_status.json").read_text(encoding="utf-8"))
assert ledger["totals"]["papers_in_scope"] == 14
assert len(ledger["papers"]) == 14
for year in range(2010, 2017):
    for paper in (1, 2):
        key = f"{year}_P{paper}"
        assert key in ledger["papers"], f"Missing audit status: {key}"
        record = ledger["papers"][key]
        assert record["year"] == year and record["paper_number"] == paper
        assert record["answer_key_status"] == "NOT_AUTHENTICATED" or record["answer_key_status"] == "VERIFIED"
print("Validated audit status for all 14 in-scope papers.")
