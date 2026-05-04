# 🧠 LeetCode Personal Data Extractor

> A production-grade pipeline that extracts all your LeetCode accepted submissions, organizes them into language-aware files, exports structured data, and automatically pushes everything to GitHub — built to run on **Databricks** or locally in **VS Code**.

---

## 📁 Output Structure

```
leetcode_solutions/
  ├── two-sum/
  │     └── two-sum.py
  ├── customers-who-never-order/
  │     └── customers-who-never-order.sql
  ├── valid-phone-numbers/
  │     └── valid-phone-numbers.sh
  └── ...
leetcode_export.json       ← full raw data (all fields)
leetcode_export.csv        ← flat, analysis-ready table
export_log.csv             ← transaction log with timestamps
```

Each solution file includes a full header with problem metadata:

```python
# ============================================================
# Problem    : Two Sum
# URL        : https://leetcode.com/problems/two-sum/
# Difficulty : Easy
# Category   : Algorithms
# Tags       : Array, Hash Table
#
# Acceptance : 52.3%
# Likes      : 68658  |  Dislikes: 2901
#
# Language   : python3
# Runtime    : 45 ms  (beats 87.3%)
# Memory     : 17.2 MB  (beats 65.1%)
# Submitted  : 2024-11-01 10:22:00 UTC
# Exported   : 2025-01-15 08:00:00 UTC
#
# Hints: Consider using a hash map.
# ============================================================

class Solution:
    def twoSum(self, nums, target):
        ...
```

---

## ⚙️ Pipeline Stages

| Step | Description |
|------|-------------|
| **0** | Configuration — cookies, paths, GitHub settings |
| **1** | Imports, helpers, language → extension map |
| **2** | GraphQL query definitions |
| **3** | Fetch all your submissions (paginated) |
| **4** | Deduplicate — keep best accepted per problem |
| **5** | **Incremental check** — skip already-exported folders |
| **6** | Enrich new problems with full details from API |
| **7** | Export: one folder per problem, correct file extension |
| **8** | Append to JSON, CSV, and transaction log |
| **9** | Push new files to GitHub via REST API |
| **10** | Pipeline summary |

---

## 🚀 Getting Started

### 1. Get your LeetCode session cookies

1. Log in to [leetcode.com](https://leetcode.com)
2. Open DevTools (`F12`) → **Application** → **Cookies** → `leetcode.com`
3. Copy the values of `LEETCODE_SESSION` and `csrftoken`

### 2. Configure Step 0 in the notebook

```python
LEETCODE_SESSION  = "your_session_cookie"
CSRF_TOKEN        = "your_csrftoken"
USERNAME          = "your_username"

OUTPUT_ROOT       = "leetcode_solutions"
GIT_REPO_URL      = "https://github.com/YourUsername/YourRepo.git"
GIT_BRANCH        = "main"
```

### 3. Get a GitHub Personal Access Token

1. Go to GitHub → **Settings** → **Developer Settings** → **Personal Access Tokens** → Fine-grained
2. Scope it to your LeetCode repo
3. Grant **Contents: read & write**
4. Paste it into `GITHUB_TOKEN` in Step 8

### 4. Run all cells

The pipeline runs top to bottom. On subsequent runs, it automatically skips problems already exported — only new solutions are processed and pushed.

---

## 🔁 Incremental Logic

The pipeline is **safe to re-run at any time**. It works like this:

```
On each run:
  ┌─────────────────────────────────────────────┐
  │  Scan leetcode_solutions/ for existing folders │
  │  Compare against your current solved list      │
  │  Only fetch + export the NEW problems          │
  │  Append new rows to CSV and log                │
  │  Push only new files to GitHub                 │
  └─────────────────────────────────────────────┘
```

No duplicates. No overwrites. No wasted API calls.

---

## 🗂️ Supported Languages

| LeetCode Language | File Extension |
|-------------------|---------------|
| Python / Python3 / Pandas | `.py` |
| MySQL / PostgreSQL / Oracle / MS SQL | `.sql` |
| Bash / Shell | `.sh` |
| JavaScript | `.js` |
| TypeScript | `.ts` |
| Java | `.java` |
| C / C++ / C# | `.c` / `.cpp` / `.cs` |
| Go / Golang | `.go` |
| Rust | `.rs` |
| Kotlin | `.kt` |
| Swift | `.swift` |
| Ruby | `.rb` |
| Scala | `.scala` |
| PHP | `.php` |
| R | `.r` |
| Dart | `.dart` |
| Other | `.txt` |

---

## 📊 Exported Data Fields

| Field | Description |
|-------|-------------|
| `title` | Problem name |
| `slug` | URL-safe name |
| `url` | Direct link to problem |
| `difficulty` | Easy / Medium / Hard |
| `category` | Algorithms / Database / Shell |
| `topic_tags` | e.g. Array, Dynamic Programming |
| `acceptance_rate` | Global acceptance % |
| `likes` / `dislikes` | Community rating |
| `total_accepted` | Global accepted count |
| `hints` | Official hints |
| `language` | Language used |
| `code` | Your solution (JSON only) |
| `runtime` / `memory` | Your performance |
| `runtime_percentile` / `memory_percentile` | Beats % |
| `submitted_at` | Submission timestamp |
| `exported_at` | Export timestamp (UTC) |

---

## 🌐 Running on Databricks

This pipeline is designed to run on **Databricks**. The GitHub push step uses the **GitHub REST API** directly (not the git CLI), which avoids the `dubious ownership` error that occurs in the Databricks workspace environment.

```
No subprocess. No git CLI. No permission issues.
Just HTTPS calls to the GitHub Contents API.
```

Make sure your `GITHUB_TOKEN` has write access to the target repository.

---

## 🛠️ Requirements

```
requests
pandas
pathlib (built-in)
json, csv, time, base64, subprocess (built-in)
```

Install if needed:
```bash
pip install requests pandas
```

---

## 📝 Transaction Log

Every export run appends to `export_log.csv`:

```
timestamp_utc,slug,title,language,difficulty,file_path,status
2025-01-15 08:00:00 UTC,two-sum,Two Sum,python3,Easy,leetcode_solutions/two-sum/two-sum.py,exported
2025-01-15 08:00:01 UTC,reverse-integer,Reverse Integer,python3,Medium,...,exported
```

---

## 👤 Author

**Mena Shafik**
[GitHub](https://github.com/MenaShafik) · [LeetCode](https://leetcode.com/menashafik)
