# Primary sources for USPTO post-grant proceedings

This repository is a public, agent-readable library of primary sources cited by the insight stories at [postgrantproceeding.com](https://postgrantproceeding.com). Phase 1 holds every statute, regulation, MPEP section, PTAB or Director decision, federal court opinion, Federal Register document, and USPTO notice those 30 stories cite, where an official text could be retrieved.

The files already listed in `metadata.json` and `metadata.csv` are GitHub Release assets from `batch-2026-10-14`. Those filenames and release URLs are unchanged. New texts live under `docs/` beside that index. Where a phase-1 decision is the same proceeding and paper as a release asset, `docs/aliases/` holds a stub and `docs/legacy-release-map.csv` records the pair.

## What is in each document

```
docs/<type>/<slug>/index.md
docs/<type>/<slug>/original.pdf | original.html | original.xml
```

`index.md` has YAML front matter, a schema.org JSON-LD block (`Legislation`, `CreativeWork`, or `Report`), and a Markdown transcription. `original.*` is the file retrieved from the official source. Its SHA-256 is in the front matter.

| Type | Path | Examples in later phases |
| --- | --- | --- |
| Statutes | `docs/statutes/35-usc-NNN/` | 35 U.S.C. §§ 301–307, 311–319, 321–329 |
| Regulations | `docs/cfr/37-cfr-N-NNN/` | 37 C.F.R. Part 42 and §§ 1.501–1.570 |
| MPEP | `docs/mpep/<slug>/` | The full manual, one section per directory |
| PTAB and Director decisions | `docs/ptab/<proceeding>-paper-<n>/` | Every precedential and informative decision, with designation and de-designation dates |
| Federal court opinions | `docs/courts/<court>-<docket>-<slug>/` | Selected Federal Circuit patent opinions |
| Federal Register | `docs/federal-register/<vol>-fr-<page>/` | Rules the stories cite |
| USPTO notices | `docs/notices/<slug>/` | Designation notices and the precedential/informative list |

`docs/omitted.json` lists cites that were left out, with the reason.

## Repo indexes

- `index.json` and `index.csv` — one row per document, including citation, designation, checksum, source URL, and the insight stories that cite it.
- `llms.txt` — [llmstxt.org](https://llmstxt.org) layout: an H1, a summary blockquote, and an H2 per document type linking each `index.md`.
- `sitemap.xml` — one `<loc>` per `index.md`.

GitHub Pages is not enabled for this repository. The sitemap and `llms.txt` therefore use `raw.githubusercontent.com` URLs for the branch named in `index.json` (`sitemap_branch`). After a maintainer merges that branch, those URLs should be pointed at the default branch. This library does not merge itself.

## Provenance

Each document was retrieved on the `retrieved_on` date from the `source_url` in its front matter. Phase 1 sources are the Office of the Law Revision Counsel text as published on govinfo (the House US Code site was returning a maintenance page), the eCFR versioner, uspto.gov (MPEP, PTAB decisions, and notices), cafc.uscourts.gov, supremecourt.gov, and govinfo Federal Register PDFs.

`uscode.house.gov` was not usable on the retrieval date. Statute text is the United States Code, 2024 Main Edition, laws enacted through January 6, 2025. The MPEP index on uspto.gov identifies the current manual as **Ninth Edition, Revision 01.2024**. It does not print a month and day for that revision. Section 2242's own heading is marked **[R-10.2019]**. Appendices L and R state that they are current as of January 31, 2024. The operative regulation text is the eCFR issue, which is later than those appendices.

The official source controls if a transcription differs. Designation status is taken from the USPTO precedential and informative decisions list retrieved with the entry, or from a USPTO notice when that notice is the designation record. A decision whose PDF and that list do not print the same date is marked `Not yet confirmed`.

## Public-domain status

Works of the United States Government are not subject to copyright protection under 17 U.S.C. § 105. The statutes, regulations, Federal Register documents, USPTO decisions, MPEP text, and federal judicial opinions in this library are United States government works. This repository does not add a copyright claim to them.

Reporter citations in the Federal Reporter are recorded because the stories use them. Those volume-and-page cites are not printed on the court's slip opinion. The slip opinion from the court's own site is the file stored here. Party filings, statistical compilations, commercial databases, and trade press are not government works of the kinds this library collects, and they are not added.

## What this library is not

It is not legal advice. It is not a client file, a firm work product, or a commentary archive. `scripts/validate_library.py` rejects an exclusion list of names, stored in that script as code points. Two official Director decisions are kept unedited, and the scan skips only their PDF and the verbatim transcription under `## Text`: `docs/ptab/ipr2025-01582-paper-11` and `docs/ptab/ipr2025-00464-paper-12`. Front matter, notes, this README, and every other file are still scanned. Repository URL prefixes are removed before the scan so the account path in a raw URL is not treated as prose.
