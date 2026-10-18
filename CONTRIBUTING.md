# Selection and how to add a document

Add a public-record United States government work, or leave it out. Phase 1 is every primary source cited by the 30 insight stories on postgrantproceeding.com. Later phases use the same directories. Do not move or rename `metadata.json`, `metadata.csv`, or the `batch-2026-10-14` release assets. The site's decision-library links point at those release URLs.

## In scope

- United States Code and Code of Federal Regulations sections, from govinfo or the eCFR.
- MPEP sections and appendices from uspto.gov. Record the revision the page actually prints. Do not invent a month or day. If a section heading carries its own marker, such as `[R-10.2019]`, record that too.
- PTAB, Director, Precedential Opinion Panel, and Appeals Review Panel decisions from uspto.gov.
- Federal court opinions from the issuing court's site or supremecourt.gov.
- Federal Register documents from govinfo, and USPTO notices, when they are the official rule or designation record for a document already in scope.

## Out of scope

- Client material, firm work product, and law-firm articles.
- Party filings, including a request for Director Review posted as a party paper.
- Statistical compilations, data-portal pulls, and commercial or trade-press reports.
- A name on the exclusion list in `scripts/validate_library.py`, outside the two unedited official records named below. Those names are stored as code points. Do not write them into prose, front matter, or notes. The scan skips only the official PDF and the verbatim transcription under `## Text` for `docs/ptab/ipr2025-01582-paper-11` and `docs/ptab/ipr2025-00464-paper-12`. Front matter of those entries, and every other file, is still scanned.

The validator removes only these repository URL prefixes before it scans, and it does not ignore the same letters in ordinary prose:

- `https://github.com/ssukduang-cpu/pgp-documents`
- `https://raw.githubusercontent.com/ssukduang-cpu/pgp-documents`
- `github.com/ssukduang-cpu/pgp-documents`

## Designation

Take precedential status, informative status, a section limit, the designation date, and the de-designation date from the current USPTO precedential and informative decisions list, or from a USPTO notice when the notice is the designation record. If the list limits a designation to a section, record that limit. Do not treat a decision as designated for the whole paper when the list says otherwise. If the decision PDF and the list print different dates, keep the entry, set `confirmation_status` to `Not yet confirmed`, and say which source printed which date. Do not pick a date that neither source prints.

## Phase 2

Fill the existing statute, regulation, and PTAB directories with:

- 35 U.S.C. §§ 301–307, 311–319, and 321–329
- 37 C.F.R. Part 42 and §§ 1.501–1.570
- Every PTAB precedential and informative decision, with designation and de-designation dates from the USPTO list or a USPTO notice

## Phase 3

Add the full MPEP, one section per directory, in sync with the revision current on uspto.gov. Keep each section's own revision marker.

## Phase 4 — Federal Circuit selection

Add a precedential Federal Circuit opinion when all of the following are true:

1. The opinion interprets an America Invents Act trial statute, 35 U.S.C. §§ 311–329, or it decides assignor estoppel in an inter partes review, printed-publication status, the time bar, estoppel, or patent eligibility insofar as that holding ends an AIA trial.
2. A designated PTAB decision, or a later written selection memo in this repository, cites the opinion.

Add a nonprecedential order only when an insight story cites it. Do not add an opinion because a party is well known.

## Adding a file

1. Create `docs/<type>/<slug>/`.
2. Save the official file as `original.pdf`, `original.html`, or `original.xml`.
3. Write `index.md` with the front matter used by the phase-1 entries: `title`, `citation`, `court_or_board`, `date`, `docket_or_appeal_number`, `precedential_status`, `designation_date`, `de_designation_date`, `topic_tags`, `source_url`, `retrieved_on`, `sha256`, and `cited_by_stories`. Story URLs are `https://postgrantproceeding.com/insights/<slug>`.
4. Add a schema.org JSON-LD block with `@context`, `@type`, `identifier`, `datePublished`, `publisher`, `url`, and `isBasedOn`.
5. Regenerate `index.json`, `index.csv`, `llms.txt`, and `sitemap.xml` so they match the files.
6. Run `python scripts/validate_library.py`. The GitHub Action runs the same check.
