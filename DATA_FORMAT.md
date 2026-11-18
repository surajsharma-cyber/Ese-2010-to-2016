# Question data format

The portal reads `data/questions.json`. The file is deliberately empty until original questions have passed source checks. The full machine-readable contract is in [`data/questions.schema.json`](data/questions.schema.json).

## Required fields per question

- `id`: stable unique identifier, e.g. `ESE-2016-CE-P1-Q001`.
- `year`: integer from 2010 through 2016.
- `paper_number`: `1` or `2`; only the two Civil technical objective papers are in scope.
- `question_number`: printed question number in the source.
- `sequence_index`: sequence position in the original paper.
- `question_text`: faithful transcription; retain units, symbols and line breaks.
- `options`: array of `{ "key": "A", "text": "..." }` objects.
- `verification_status`: VERIFIED / PROVISIONAL / DISPUTED / UNVERIFIED.
- `source`: source title, URL and printed/PDF page reference.

## Optional fields

- `diagram_url`: relative path to an original diagram asset stored in the repository.
- `subject` and `topic`: secondary classifications; do not change original order.
- `answer_key`: answer, status, source and notes. Keep this separate from question transcription status.
- `marks_positive` and `marks_negative`: use only when the marking scheme for that paper is established from a source.

## Admission rules

1. A record marked `VERIFIED` must have its question number, wording, every option, and any diagram checked against the original paper scan.
2. The source must be an identified Civil technical objective paper, not a conventional paper, General Ability Test, GATE paper or another discipline.
3. A secondary transcription may be used as a comparison aid, never as the authority when an official original is available.
4. An answer key is usable for scoring only when `answer_key.status` is `VERIFIED`. Question verification does not automatically verify its answer.
5. Never guess unclear scan text. Hold the record as `PROVISIONAL` or `DISPUTED` until resolved.
6. Keep the original question sequence using `sequence_index`; topic filters are optional overlays.

## Empty-state policy

Do not insert sample/demo questions into the live question bank. An empty array is correct until source-verified records are ready.
