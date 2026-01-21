Projrct Overview

This project implements a fault-tolerant data ingestion pipeline that validates, cleans, deduplicates, and persists CSV data while ensuring safe re-runs and data quality visibility.

Problem Statement

Raw CSV data often contains invalid records, duplicates, and inconsistent formats. Naive pipelines overwrite outputs on failure, leading to silent data corruption and unreliable downstream analytics.

High level Architecture

Input CSV
  ↓
Validation & Cleaning
  ↓
Rejection Handling
  ↓
Deduplication
  ↓
Temp Output
  ↓
Atomic Promotion
  ↓
Final Output + Reports



Pipeline Flow (Step by Step)

Reads raw CSV from configured input path

Separates invalid records with explicit error reasons

Cleans recoverable data issues

Deduplicates records using in-memory sets

Writes output to a temporary file

Atomically promotes temp output to final destination

Generates data quality and rejection reports



Failure Handling and Safe Re-runs

The pipeline never writes directly to the final output. All processing occurs in a temporary file, which is atomically promoted only after successful completion. If a failure occurs at any stage, the previous valid output remains intact, making re-runs idempotent and safe.






Data Quality & Metrics

Total records processed

Cleaned records

Rejected records

Final deduplicated records

Rejection reason breakdown




Teck Stack 

Python

CSV module

Logging

JSON reports

Git



How To run

Copy the repository 

python -m src.pipeline
