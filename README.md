# ESE Civil Engineering Technical Prelims PYQ Portal (2010–2016)

A dependency-free static web application for practising UPSC Engineering Services Examination Civil Engineering technical objective papers from 2010–2016.

## Included scope

- Civil Engineering technical objective Paper I and Paper II only.
- Years 2010–2016.

## Excluded

- Conventional/descriptive papers.
- General Ability Test, General Studies and other non-technical papers.
- GATE questions and all other engineering disciplines.
- Unattributed or unverifiable questions.

## Run locally

Because the application loads JSON with `fetch()`, serve the repository over HTTP rather than opening `index.html` as a `file://` URL.

For example, with Python installed:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

No build step, package manager or third-party JavaScript dependency is required.

## Features

- Year, paper, subject and text filters.
- Sequential practice with question navigation.
- Answer reveal only after the user selects an option.
- Timed test mode (60 seconds per question, auto-submit).
- Bookmarks stored in the current browser.
- Session history and performance summary stored in the current browser.
- Answer-key-aware scoring: records with unverified answer keys are not marked correct or incorrect.
- Source inventory and verification-ledger links.
- Responsive layout for desktop and mobile.

Browser bookmarks and performance history are local to that browser/device. They are not synchronised to GitHub or another device.

## GitHub Pages deployment

The repository contains a root-level `index.html` and `.nojekyll`. To publish:

1. Open repository **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select `main` and `/(root)`, then Save.
4. Wait for the Pages deployment to complete. GitHub notes that publication can take several minutes.
5. Use the **Visit site** link in Settings → Pages to confirm the live address.

The expected project-site URL is:

`https://surajsharma-cyber.github.io/Ese-2010-to-2016/`

This URL must not be treated as live until GitHub Pages reports a successful deployment.

## Question data and source integrity

The application loads `data/questions.json`. Its format is specified in [DATA_FORMAT.md](DATA_FORMAT.md) and [data/questions.schema.json](data/questions.schema.json).

- Preserve exact wording, options, numbering, diagrams, units and year/paper labels.
- Preserve original paper order through `sequence_index`.
- Keep question-transcription verification separate from answer-key verification.
- Use only `answer_key.status = VERIFIED` for correctness scoring.
- Do not import third-party content merely because its title or year looks plausible.
- Keep unclear or disputed records out of the verified question bank.

## Current content status

The application shell and core browser interactions are implemented. **The live question dataset is still empty.** The source audit has sampled 18 questions from 2016 Civil Paper I: 13 third-party text-and-option matches, 3 confirmed third-party option mismatches, and 2 held for numeral/diagram checks. 102 Paper I questions remain unsampled. The repository tracks all 14 in-scope papers in `data/paper_audit_status.json`. The remaining 102 Paper I questions and all 120 Paper II questions have not been audited. No answer key is currently authenticated as an official verified key. The portal therefore opens in a clear empty state rather than presenting fabricated content.

See [SOURCES.md](SOURCES.md), [data/source_inventory.json](data/source_inventory.json) and [data/verification.json](data/verification.json) for the detailed record.

## Disclaimer

Independent educational project; not affiliated with or endorsed by UPSC. Source papers and scans remain subject to their original rights and terms.
