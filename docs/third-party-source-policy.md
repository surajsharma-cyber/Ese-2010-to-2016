# Third-party source policy and retrieval register

Updated: 18 November 2026

## Scope

Only UPSC ESE Civil Engineering technical objective/prelims papers for 2010–2016 are in scope: Paper I and Paper II. Exclude General Studies/Engineering Aptitude, conventional/descriptive papers, GATE and every other discipline.

## User-authorized source policy

The project may use a reputable third-party provider's identified ESE Civil question-paper PDF and the answer key printed or supplied with that same paper as the working source of record. It is not necessary to re-authenticate every item against UPSC if the provider clearly identifies the exam, year, Civil discipline, objective/prelims stage and paper number.

Provenance must remain visible. Store separate statuses:
- `PROVIDER_SOURCE_ACCEPTED`: provider's own paper/key is being relied upon as supplied.
- `TRANSCRIPTION_CHECKED`: page-by-page transcription checked against the provider PDF.
- `PROVIDER_KEY_IMPORTED`: answer key imported as supplied by provider.
- `INDEPENDENT_ANSWER_CHECKED`: answer independently solved/cross-checked.
- `OFFICIAL_UPSC_MATCHED`: separately compared with UPSC original.
Do not relabel a provider key as an official UPSC key. If provider source has no key, use `NOT_SUPPLIED`; do not invent one.

## Third-party source leads

1. Mathematical Society — https://mathematicalsociety.org/ies-civil-engineering-previous-year-question-papers/
   - Lists Civil Prelims Paper I and II for 2010, 2011, 2013, 2014, 2015 and 2016.
   - Its 2012 section has an apparent year-label error: the rows are labelled 2010 Paper I and II.
   - The page's download-image links resolved to a generic JPEG image in the browser, not to a retrievable paper PDF. Thus it is a catalogue lead, not a retrieved source file.
2. My UPSC Syllabus — https://myupscsyllabus.in/download/upsc-civil-engineering-previous-question-papers
   - Lists ESE CE download entries for 2010–2016.
   - The entries point to year-specific Google Drive folders. Browser retrieval of those folders returned cache-miss errors; no file contents were extracted in this run.
3. UPSC archive — https://www.upsc.gov.in/examinations/previous-question-papers/archives
   - Retain as a corroborating source when available, but do not block the workflow solely on official-source retrieval.

## Retrieval and admission rule

A third-party source is eligible once its actual PDF/file is retrieved and its cover/header or provider metadata identifies year, ESE/IES, Civil Engineering, objective/prelims, and Paper I or II. Then inspect every page, transcribe all question text/options/figures and printed numbering, preserve order, and record page provenance. Use the answer key supplied by that provider as a provider key. If a page is missing, unreadable, mislabelled or internally inconsistent, quarantine only the affected records.

The Mathematical Society page is not yet a usable paper source because its download buttons currently resolve to a generic JPEG. The My UPSC Syllabus year folders are promising but were not retrievable through the browser cache. No question data should be fabricated from catalogue rows.
