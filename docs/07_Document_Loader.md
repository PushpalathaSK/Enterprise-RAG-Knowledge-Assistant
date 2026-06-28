# Module 2 - Document Loader

## Objective

The Document Loader is responsible for reading documents from different sources and converting them into a standardized format that the RAG pipeline can process.

---

## Current Scope

- Read PDF documents
- Preserve metadata
- Return structured document objects

---

## Future Scope

- DOCX
- TXT
- HTML
- Markdown
- Websites
- SharePoint
- Google Drive

---

## Input

One or more PDF files

---

## Output

LangChain Document objects

---

## Why This Module?

Large Language Models cannot directly understand PDF files.

We first extract the document content before processing it further.

---

## Libraries

- langchain-community
- PyPDFLoader

---

## Next Module

Text Chunking