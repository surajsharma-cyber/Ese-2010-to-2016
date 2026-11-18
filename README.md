# ESE Civil Engineering Technical Prelims PYQ Portal (2010–2016)

A dependency-free static web application for practising UPSC Engineering Services Examination Civil Engineering technical objective papers from 2010–2016.

## Included scope

- Civil Engineering technical objective Paper II only.
- Years 2010–2016.

## Excluded

- Conventional/descriptive papers.
- General Ability Test / General Studies, Paper I and other non-technical papers.
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
- Keep question transcription, provider provenance and answer-key status separate.
- Third-party provider papers and their supplied keys may be used as the working source of record when the provider identifies the correct ESE year, Civil discipline, objective stage and paper number. Label them `PROVIDER_SOURCE_ACCEPTED` / `PROVIDER_KEY_IMPORTED`; never call them official UPSC material.
- `INDEPENDENT_ANSWER_CHECKED` and `OFFICIAL_UPSC_MATCHED` are additional statuses, not prerequisites for using a clearly identified provider paper.
- Quarantine missing, unreadable, mislabelled or internally inconsistent records.

## Current content status

The application shell and core browser interactions are implemented for Paper II only. **The live question dataset is still empty.** The source register is restricted to Civil Engineering technical objective Paper II. ExamElite lists 2015 ESE Civil Papers I and II (120 questions each); its 2010–2013 generic Civil entries are not identified as ESE and are not accepted as ESE papers. Third-party source policy now permits a clearly identified provider paper and its supplied answer key to be used as the working source of record, with provenance labels rather than requiring an official UPSC match first. Mathematical Society lists the target years but its current download buttons resolve to a generic JPEG; My UPSC Syllabus lists 2010–2016 Drive folders but browser retrieval returned cache misses. See `docs/third-party-source-policy.md` and `data/source_inventory.json`. The portal therefore opens in a clear empty state rather than presenting fabricated content.

See [SOURCES.md](SOURCES.md), [data/source_inventory.json](data/source_inventory.json) and [data/verification.json](data/verification.json) for the detailed record.

## Disclaimer

Independent educational project; not affiliated with or endorsed by UPSC. Source papers and scans remain subject to their original rights and terms.


## Third-party source progress

The source inventory now contains direct Civil Technical Paper II links for 2010–2016 from Engineers Forum / IESect and other providers. The IES Academy ESE-2015 Civil Objective Paper II Set D key has been imported separately at `data/provider_answer_keys/2015_P2_set_D.json` with provider provenance; 115 answer choices and five provider dashes are recorded. This is not an official UPSC key and has not been independently checked. The question bank remains empty until the actual paper PDFs can be retrieved and inspected. Do not treat source links or an answer-key file as completed question transcription.
