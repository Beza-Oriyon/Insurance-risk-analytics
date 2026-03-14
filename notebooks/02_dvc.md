### Task 2: Data Version Control (DVC) – Interpretation & Business Value

**What we did**:
- Installed DVC and initialized it in the project.
- Created a local remote storage at `/tmp/dvc-storage`.
- Tracked the large `insurance_data.csv` file using `dvc add`.
- Pushed the actual data to the remote while only keeping a tiny `insurance_data.csv.dvc` pointer in Git.

**Why this matters in insurance**:
- In regulated industries like car insurance, auditors can demand: “Show me exactly the data you used for this analysis 6 months ago.”
- DVC guarantees we can always reproduce the exact same dataset and analysis — no more “the CSV was updated and now results changed” problems.
- Git stays small and fast (only code + tiny pointers), while the big 1M-row dataset lives safely in storage.

**Key takeaway**:
We now have a professional, auditable data pipeline. This is standard practice in finance/insurance and directly supports the challenge’s goal of building reproducible analytics.

**Status**: Task 2 Minimum Essentials completed ✅