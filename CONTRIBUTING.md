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

## Phase 4. Federal Circuit selection

A major opinion of the United States Court of Appeals for the Federal Circuit, in this library, means every precedential opinion and every precedential order in the scope below, plus a notable nonprecedential opinion or order. Notable means at least one test is met. Record that test in the document metadata. The same definition is in `config/cafc-major.yml`. This section states the rule. It does not add opinions.

Scope is a Federal Circuit decision in a patent appeal from the United States Patent and Trademark Office (USPTO). That includes Patent Trial and Appeal Board (PTAB) trials, ex parte appeals, and reexamination. Scope also includes a precedential petition order directed to the USPTO, for example In re Motorola Solutions, No. 25-134. Trademark appeals are out of scope.

Precedential. Include every precedential opinion in scope, and every precedential order in scope.

Notable nonprecedential. Include a nonprecedential opinion or order if any test is met, and record which test.

- N1. It is cited in a later precedential Federal Circuit opinion. The evidence is that citing opinion.
- N2. It is cited in a PTAB precedential or informative decision, or in a USPTO memo or notice. The evidence is that decision, memo, or notice.
- N3. It reverses or vacates the Board, in whole or part, on one of the issues below, confirmed by a reviewer. The evidence is the slip disposition, the issue, and the reviewer confirmation.
  - 35 U.S.C. § 315(b) time bar
  - 35 U.S.C. § 315(e) or § 325(e) estoppel
  - 35 U.S.C. § 314 or § 324 institution or discretionary denial
  - 35 U.S.C. § 325(d)
  - real party in interest
  - Administrative Procedure Act (APA) or due process notice
  - claim construction standard
  - motion to amend
  - reexamination substantial new question of patentability, or reexamination estoppel
- N4. It is on a manual list. Each entry needs a written reason, and that reason is the evidence.

Excluded, unless the document is on the N4 list: Rule 36 judgments, errata, and nonprecedential orders.

Source of truth for precedential status, release date, and origin is the court's own opinions and orders list, at <https://www.cafc.uscourts.gov/home/case-information/opinions-orders/>. That list starts in October 2004, which is the earliest coverage. The court states that opinions and select orders from October 1, 2004, to the present are posted there. An opinion from before October 2004 comes in only through N4.

Text source is the official court portable document format (PDF) file. A third-party or scraped collection, including the CAFC-Revisions data, is secondary. It may be used only after that collection's audit gates pass.

The library stores these opinions at `docs/courts/` with `document_type: courts`. The validator treats one of those documents as a federal-court-opinion record when `court_or_board` is the United States Court of Appeals for the Federal Circuit. `docs/omitted.json` holds exclusions with reasons. Its `federal_circuit_exclusions` array starts empty.

## Adding a file

1. Create `docs/<type>/<slug>/`.
2. Save the official file as `original.pdf`, `original.html`, or `original.xml`.
3. Write `index.md` with the front matter used by the phase-1 entries: `title`, `citation`, `court_or_board`, `date`, `docket_or_appeal_number`, `precedential_status`, `designation_date`, `de_designation_date`, `topic_tags`, `source_url`, `retrieved_on`, `sha256`, and `cited_by_stories`. Story URLs are `https://postgrantproceeding.com/insights/<slug>`. A Federal Circuit document is a federal-court-opinion record. Its `precedential_status` is `precedential` or `nonprecedential`. When it is nonprecedential, also set `selection_test` to `N1`, `N2`, `N3`, or `N4`, and set `selection_evidence` to the citing case or memo, or to the written reason for `N4`.
4. Add a schema.org JSON-LD block with `@context`, `@type`, `identifier`, `datePublished`, `publisher`, `url`, and `isBasedOn`.
5. Regenerate `index.json`, `index.csv`, `llms.txt`, and `sitemap.xml` so they match the files.
6. Run `python scripts/validate_library.py`. The GitHub Action runs the same check.
