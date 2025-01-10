from agents.scraping.scrapingAgent import flow as sf
from agents.summarization.summerAgent import model as sm
from agents.summarization.summerAgent import get_data as gd
from agents.chat.chatAgent import chat
from agents.factcheck.factAgent import fact_model as fm

if __name__ == '__main__':

    # Agent 1 scraping
    print("Enter the desired research topic:")
    keyword = input()
    sf(keyword)

    # Agent 2 Document ingestion
    summary = sm(keyword, gd())

    # Agent 3 Fact Checker
    print("Fact checking in progress...")
    fm(summary)
    print("Fact checking complete.")

    # Agent 4 Chat with user
    chat(summary)
