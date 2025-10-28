# European-NLP

[European Chapter of the Association for Computational Linguistics](https://eacl.org/)

Current focus is exclusively on French, German and Russian.

**Core Objective: Enhance Multilingual AI Robustness and Applicability**

| Dimension | Motivation Description | Key Linguistic Challenges Addressed |
| :--- | :--- | :--- |
| **Technical Innovation** | Address High-Complexity Language Challenges: Develop more refined NLP models tailored to the unique morphological complexity (Russian case system, French verb conjugations) and syntactic structures (German compounding, Russian free word order). | Improving **lexical analysis** and **syntactic parsing** accuracy under high inflection, compounding, and flexible word order. |
| **Application Value** | Fulfill European and Strategic Market Needs: German and French are core EU economic languages requiring high-quality solutions for **FinTech, LegalTech, and business automation**. Russian holds significant **geopolitical and information security** strategic value. | Directly serving the **localization**, **cross-border collaboration**, and **information analysis** markets in Europe and Eurasia. |
| **Model Generality** | Drive Multilingual Model Generalization: Use these distinct languages as rigorous benchmarks to test and refine the **cross-lingual transfer efficiency** and **generalization capabilities** of multilingual models (e.g., mBERT, XLM-R). | Assessing model **fairness** and **robustness** when handling complex structures found in languages beyond the dominant resource pool. |

## Codes

Example models for three languages ​​were called separately.

| Language | Source | Example Model ID |
| :--- | :--- | :--- |
| **Français** | [TALN](https://www.atala.org/-Conference-TALN-RECITAL) | `dbddv01/gpt2-french-small` |
| **Deutsch** | [GSCL Konferenz](https://www.gscl.org/events/) | `LSX-UniWue/LLaMmlein_1B` |
| **Русский** | [A paper...](https://habr.com/ru/articles/669674/) | `cointegrated/rubert-tiny2` |

## Text-to-Speech

Pre-install: `pip install gtts`
