# SC Document Intelligence

AI-powered document Q&A for supply chain contracts, SOPs, and operational documents — ask questions in plain English, get precise, sourced answers.

## Why this exists

Supply chain analysts and consultants spend hours manually searching freight contracts, 3PL agreements, and SOPs for specific clauses — penalty structures, SLA thresholds, process steps. This project applies retrieval-augmented generation (RAG) to make that instant.

This is a working build, developed in public as part of a 30-day AI agents learning sprint — from a 10-year supply chain and product management background (Accenture, Swiggy/Scootsy, Ather Energy, Lynk Logistics).

## Status

🚧 **Day 1 of 30** — project scaffolding and planning complete. Build starts Day 2.

- [X] Day 2 — CLI tool with direct-context Q&A (no RAG yet)
- [X] Day 3 — Full RAG pipeline (chunking, embeddings, vector search)
- [ ] Day 4 — Web UI
- [ ] Day 5 — Deployment + source citations

## Planned tech stack

- Python
- Anthropic Claude API
- ChromaDB (vector store)
- Flask (web UI)

## Example queries this will answer

- "What is the OTIF penalty clause and how is it calculated?"
- "What is the minimum order quantity for cold chain SKUs?"
- "What does the SLA say about priority order fulfillment windows?"
- "What are the RMA steps for damaged goods?"

## Follow along

This build is documented on [LinkedIn](https://linkedin.com/in/rupeshghadai) as part of a 30-day AI agents sprint.

## Known limitations / future improvements
- Some chunks contain mostly formatting/headers with little content (due to document's visual section dividers) — a preprocessing step to strip decorative formatting would improve this
- Local embedding model (all-MiniLM-L6-v2) sometimes ranks tangentially-related chunks above the best match for indirect/paraphrased questions — retrieving top-3+ chunks compensates for this; upgrading to Voyage AI embeddings could improve ranking precision