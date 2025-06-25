# Contributing Guide

1. **Keywords:** Start every BibTeX `keywords` field with a Pillar ID (`T1`–`T8`).  
2. **Links Only:** Do **not** attach PDFs; cite with `doi` or `url`.  
3. **Commit Style:** Use conventional commit prefixes (`feat:`, `docs:`, `ci:` …).  
4. **Docs:** Pillar & tag definitions live in `docs/TAXONOMY.md`.

---

## 🛠️ Contributor Quick-Start Cheatsheet

> Follow these three one-time setup steps on every new clone **before** you add or edit papers.

| Step | Command ⬇ | What it does |
|------|-----------|--------------|
| **1. Enable local hooks** | ```powershell<br>git config core.hooksPath .githooks<br>``` | Activates the pre-commit script that enforces `keywords = {T#, …}`. |
| **2. Create a Python virtual env *(optional but tidy)* ** | ```powershell<br>python -m venv .venv<br>.venv\Scripts\Activate<br>``` | Keeps dependencies isolated. |
| **3. Install tooling** | ```powershell<br>pip install bibtexparser requests<br>``` | Lets you run the link checker or `group_by_pillar.py` locally. |

### ➕ Adding a Paper (5-step micro-flow)

1. **Get BibTeX** from Google Scholar » Cite » BibTeX.  
2. **Paste** into `bib/bibliography.bib` at the end of the file.  
3. **Add** a `keywords` line that starts with one Pillar ID (`T1`–`T8`), e.g.  
   ```bibtex
   keywords = {T4, benchmark, dataset}
```
4. Run git add bib/bibliography.bib

5. Commit → git commit -m "feat: add <AuthorYYYYShortTitle>"
    If the commit aborts, read the red message—your keywords line is missing or malformed.

### 📄 Commit Message Conventions

| Prefix | Use for … | Example |
|--------|-----------|---------|
| `feat:` | new paper entries | `feat: add Gamache1998PBSAirCanada` |
| `docs:` | updates to README, TAXONOMY, cheatsheet | `docs: clarify tagging rules` |
| `ci:`   | workflow or hook changes | `ci: cache pandoc layer` |
| `chore:`| routine repo upkeep | `chore: tidy bib formatting` |


🧐 Need help?
Keyword / Pillar questions → open a Discussion or check docs/TAXONOMY.md.

Broken link → create an Issue with the BibTeX key; CI will also flag it.

First PR jitters → just open the PR; maintainers will guide you through changes.

Happy contributing! 🚀


---

**How it fits**

* Adds the hook path command so newcomers get the Pillar-lint protection.  
* Includes optional virtual-env + `pip` install lines for local tooling.  
* Defines the “five-step micro-flow” to add a paper—no guesswork.  
* Lists conventional commit prefixes so the history stays readable.

Once you commit and push, the cheatsheet will appear in **contributing.md** and render in GitHub’s sidebar for every future collaborator.

