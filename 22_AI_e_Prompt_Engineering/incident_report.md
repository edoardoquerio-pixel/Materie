# Incident Report – 2026-07-16

## Situation

The company's container-based infrastructure (nginx + Spring Boot + PostgreSQL) was experiencing a general failure beginning at **09:11:58**. The system was no longer accessible externally.

## Key Points (5‑point summary)

* **09:11:58 – app-db** failed to write to WAL (no space left on device) → PostgreSQL database shut down.

* **09:12:03 – app-backend** Spring Boot failed to start (caused by a Java connection error to the database).

* **09:12:04 – nginx** failed to connect to the backend (172.18.0.5:8080) → GET requests failed, users cannot access the site.

* **Resolution**: Cleaned the database disk space, started PostgreSQL, started Spring Boot, and gradually adjusted nginx health checks.

* **Prevention**: Perform monitoring of disk space in a timely manner, automate log cleanup, set up alerts for disk usage, establish soft limits for WAL size, and implement integrity checks.

## To Be Completed (remaining tasks)

- Document anomalous behavior observed in logs.
- Follow up on any additional resolution work in progress.
- Prepare reports or notifications for users or ICT administrators.
- Notify two people (technical staff + users) as indicated in the Task.

## Additional Minimal Revision Needed

- Include the relevant container IDs.
- Add startup/shutdown timestamps for each container.
- Document complete error messages (or snippets).
- Identify that the root cause was lack of space for WAL writing.
- Share the report with appropriate stakeholders.

**Missing Doc**: Include full alert history and logs for analysis.