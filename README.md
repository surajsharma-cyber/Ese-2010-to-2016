# ESE Civil Engineering Technical Prelims PYQ Portal (2010–2016)

A static, browser-based practice portal for UPSC Engineering Services Examination (ESE) Civil Engineering **Technical Prelims objective-paper** questions from 2010 through 2016.

## Strict scope

Included:
- Civil Engineering technical objective/preliminary paper questions.
- Examination years 2010, 2011, 2012, 2013, 2014, 2015 and 2016.

Excluded:
- Conventional/descriptive papers.
- General Studies and non-technical papers.
- Papers for Mechanical, Electrical, Electronics and other disciplines.
- Questions that cannot be attributed to a source paper and year with adequate confidence.

## Source-integrity policy

1. Preserve question wording, options, numbering, diagrams, units, symbols and paper/year labels.
2. Do not invent questions, options, diagrams, years or answer keys.
3. Record the source document and page/question reference for every imported question.
4. Record answer-key provenance separately from the question source.
5. Mark answers as `VERIFIED`, `PROVISIONAL`, `DISPUTED` or `UNVERIFIED`; never present an unverified key as authoritative.
6. Preserve original paper order. Any topic classification is additional metadata and must not reorder the source sequence by default.
7. If a scan is unclear or a transcription cannot be confirmed, hold the record from publication until resolved.

## Current data status

The initial repository contains the portal shell and an empty data file. No question records or answer keys have been imported. This is deliberate: source content must be verified before publication.

## Run locally

Open `index.html` in a modern browser. No build process or server is required for the initial static shell.

## GitHub Pages

1. Open repository **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select branch `main` and folder `/ (root)`.
4. Save, then wait for GitHub Pages to complete deployment.
5. The site is not considered published until the Pages deployment reports success.

## Data schema

See `data/questions.json`. Each future question record should include at minimum:
- Stable ID.
- Year and paper identifier.
- Original question number and sequence index.
- Exact question text and options.
- Diagram/media reference, if any.
- Subject/topic tags (secondary metadata).
- Source citation (document title, URL or archival reference, page).
- Answer and answer-key source, if available.
- Verification status and verification notes.

## Disclaimer

This is an independent educational project and is not affiliated with or endorsed by UPSC.

## Source inventory

See [SOURCES.md](SOURCES.md) for the official UPSC source register, confirmed 2016 Civil Engineering Objective Paper I and II links, and the pending retrieval status for 2010–2015.

## Current verification progress

The portal displays direct official UPSC links for the 2016 Civil Engineering objective papers and links to `SOURCES.md` and `data/verification.json`. A sample comparison of 2016 Paper I questions 7–12 and 19–24 found 9 complete text-and-option matches, 2 third-party option mismatches, and 1 question requiring diagram/option verification. This is not a full-paper audit. The 2016 answer-key scans found on a secondary host remain provisional; no official key has been authenticated. No questions have been admitted to the practice bank yet.

The year-wise candidate source links are also maintained in [`data/source_inventory.json`](data/source_inventory.json). Secondary listing pages are not treated as verified PDFs until the actual files are inspected against primary sources.
