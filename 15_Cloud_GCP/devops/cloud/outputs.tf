output "sage_docs_bucket_name" {
  description = "Nome del bucket dei documenti Sage."
  value       = google_storage_bucket.sage_docs.name
}

output "sage_docs_bucket_url" {
  description = "URL gs:// del bucket dei documenti Sage."
  value       = google_storage_bucket.sage_docs.url
}
