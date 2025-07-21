from rag_chain import build_qa_chain
from rephraser import rephrase_query

def main():
    print("\n🤖 VimBot: Ask about '7 Habits of Effective Text Editing' (type 'exit' to quit)\n")
    qa_chain, vectorstore = build_qa_chain()

    while True:
        query = input("You: ")
        if query.strip().lower() in ["exit", "quit"]:
            break

        reframed = rephrase_query(query)
        if reframed == "UNRELATED":
            print("VimBot: Sorry, that question doesn't relate to the document.\n")
            continue

        response = qa_chain({"query": reframed})
        print(f"\n🔄 Reframed Query: {reframed}")
        print(f"\n📚 Source Chunk:\n{response['source_documents'][0].page_content.strip()}\n")
        print(f"🤖 VimBot: {response['result']}\n")

if __name__ == "__main__":
    main()

