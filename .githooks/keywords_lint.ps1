#!/usr/bin/env pwsh
<#
  keywords_lint.ps1  –  pre-commit hook
  - Scans staged *.bib changes.
  - If any newly-added BibTeX entry lacks a Pillar tag (T1–T8) in its
    keywords field, aborts the commit with an error message.
#>

# Get all staged *.bib files
$bibFiles = git diff --cached --name-only | Where-Object { $_ -like '*.bib' }
if (-not $bibFiles) { exit 0 }   # nothing to check

$missing = @()

foreach ($file in $bibFiles) {
    # Grab only the added lines (+) around each new entry header "@"
    $addedBlocks = git diff --cached $file |
                   Select-String -Pattern '^\+\s*@' -Context 0,8   # first 8 lines of each entry

    foreach ($block in $addedBlocks.Context.PostContext) {
        if ($block -notmatch 'keywords\s*=\s*{T[1-8]\b') {
            $missing += "$file → entry starting at line $($block.LineNumber)"
        }
    }
}

if ($missing.Count -gt 0) {
    Write-Host "`n❌  Commit aborted. Each new BibTeX entry needs" `
               "a Pillar tag (T1–T8) in its keywords field.`n" -ForegroundColor Red
    $missing | ForEach-Object { Write-Host " • $_" -ForegroundColor Yellow }
    exit 1
}

exit 0
