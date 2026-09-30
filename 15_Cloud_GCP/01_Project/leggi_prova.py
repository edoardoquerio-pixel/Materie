"""Legge prova.txt da Google Cloud Storage e ne stampa il contenuto."""

from google.cloud import storage


def main():
    # Usa le credenziali predefinite di Google Cloud (ADC).
    client = storage.Client()
    bucket = client.bucket("its-ict-querio-docs")
    blob = bucket.blob("prova.txt")

    contenuto = blob.download_as_text(encoding="utf-8")
    print(contenuto, end="")


if __name__ == "__main__":
    main()
