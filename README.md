# 🤖 LLM Agent Research System: Let the Bots Do the Work

## Project Overview

[cite_start]This is a four-stage, sequential **Large Language Model (LLM) agent system** built to automate the research process[cite: 6, 58]. [cite_start]The system's primary goal is to handle the tedious parts of information gathering, validation, and processing, giving users a single, fact-checked context for QnA[cite: 6, 21, 63].

[cite_start]We defined custom **LLM Agents**—models optimized for specific tasks using external tools and well-written prompt routines[cite: 10, 11].

***

## ⚙️ The Four-Stage Pipeline (The System's Flow)

[cite_start]The system is structured as a pipeline where the output of one agent becomes the input for the next [cite: 28, 57] .

### 1. Scraper Model (Llama 3.2-1b)
* [cite_start]**Job:** Finds and selects relevant information for a given topic[cite: 31].
* [cite_start]**Tools Used:** Utilizes functions that wrap **Wikipedia Search** and **BeautifulSoup scraping** tools[cite: 32, 33].
* [cite_start]**Output:** Selects **5 most relevant links** from a Wikipedia page to be converted into documents, plus the main document for the keyword[cite: 34, 60, 65, 66].

### 2. Summarization Model (Llama 3.2-1b)
* [cite_start]**Job:** Takes the 6 documents from the scraper and generates a single, concise summary text[cite: 38, 61].
* [cite_start]**Model Note:** Llama 3.2-1b was used here for its decision-making ability[cite: 42].
* [cite_start]**Output:** One summarized text, ready for fact-checking[cite: 41, 68].

### 3. Fact Check Model (Llama 3.3-70b)
* **Job:** The crucial validation step. [cite_start]This agent checks the summary against up-to-date, external resources[cite: 44, 46, 62].
* [cite_start]**Tools Used:** Uses a direct "tool" for **internet search** via an API call[cite: 45].
* [cite_start]**Model Note:** We used the large and complex **Llama 3.3-70b** (released Dec 2024 [cite: 50][cite_start]) because this task demands the most accurate and current data[cite: 49].
* [cite_start]**Output:** The fully fact-checked text, which serves as the final **context**[cite: 49, 70].

### 4. QnA/Chat Model
* [cite_start]**Job:** Ingests the final, fact-checked text and uses it as **context** to provide interactive, accurate answers to the user's questions[cite: 63, 73].
* [cite_start]**Tools Used:** Expected to use tools like Azure Cognitive Search or similar scraping mechanisms for interactive lookup[cite: 53].

***

## 🧪 Example Workflow

[cite_start]When you input a topic like "**Powerlifting**"[cite: 77]:

1.  [cite_start]**Scraper** finds the main Wikipedia page and extracts related topics like `Barbell`, `Weightlifting`, and `International_Powerlifting_Federation`[cite: 78, 81].
2.  [cite_start]**Summarization Model** combines these into a single narrative[cite: 82, 84].
3.  [cite_start]**Fact Check Model** runs verification: `Fact checking completed`[cite: 88, 89].
4.  **QnA Model** uses the finalized text to answer user queries:
    * [cite_start]**You:** *What are the 3 excersises in powerlifting* [cite: 92]
    * [cite_start]**Assistant:** *The 3 excersises in powerlifting are squat, bench press, and deadlift.* [cite: 93]

***
