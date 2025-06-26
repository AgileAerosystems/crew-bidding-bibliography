#!/usr/bin/env pwsh
# Pre-commit: 1) auto-sort bibliography.bib, 2) stage if changed,
# 3) enforce Pillar keyword lint.

$ErrorActionPreference = "Stop"

# ----- 1. Auto-sort -----
python scripts/sort_bib.py
if ($LASTEXITCODE -ne 0) {
    Write-Error "`n❌ BibTeX parse error – commit aborted.`n"
    exit 1
}

# If sort changed the file, re-add it to the index
git diff --quiet bib/bibliography.bib
if ($LASTEXITCODE -ne 0) {
    git add bib/bibliography.bib
    Write-Host "✅ bibliography.bib sorted & re-staged."
}

# ----- 2. Pillar keyword lint -----
$bibFiles = git diff --cached --name-only | Where-Object { $_ -like '*.bib' }
$missing = @()

foreach ($file in $bibFiles) {
    $addedBlocks = git diff --cached $file | Select-String -Pattern '^\+\s*@'
    foreach ($line in $addedBlocks) {
        $context = git blame -L ($line.LineNumber),($line.LineNumber+8) $file
        if ($context -notmatch 'keywords\s*=\s*{T[1-8]\b') {
            $missing += "$file @ line $($line.LineNumber)"
        }
    }
}

if ($missing.Count -gt 0) {
    Write-Host "`n❌  Commit aborted – each new entry needs keywords = {T#, ...}`n" -ForegroundColor Red
    $missing | ForEach-Object { Write-Host " • $_" -ForegroundColor Yellow }
    exit 1
}

exit 0
