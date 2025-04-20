# Summafy AI Platform – GenAI-Powered Document Summarization

> A production-grade, serverless AI microservices backend to extract, summarize, and store content from documents using GenAI models. Built with AWS SAM, Lambda, Step Functions, and integrated DevOps pipelines for automation, observability, and scalability.

---

## ✨ Overview

**Summafy AI Platform** processes documents uploaded to S3, extracts content, summarizes it using generative AI models (OpenAI or local models), and stores the results in Amazon RDS or a vector database. It leverages AWS native services with a modular design to enable fast iteration, flexible deployment, and easy integration into downstream apps.

---

## 🧩 Architecture

### High-Level Workflow

```mermaid
graph TD
    A[S3 Upload] --> B[Doc Ingestor Lambda]
    B --> C[Text Extraction]
    C --> D[Summarizer Service]
    D --> E[Storage Writer Lambda]
    E --> F[(RDS / Vector DB)]
