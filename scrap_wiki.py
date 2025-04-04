import wikipediaapi

# Set language and proper user-agent
wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='F1RAGBot/1.0 (contact: nick.uk.28@gmail.com)'
)

pages = {
    "Overview of Formula One": "Formula One",
    "History of Formula One": "History of Formula One",
    "Driver Records": "List of Formula One driver records",
    "Race Records": "List of Formula One race records",
    "Season Summaries": "List of Formula One seasons",
    "Grand Prix Details": "List of Formula One Grands Prix",
    "Regulations and Rules": "Formula One regulations",
    "Constructors and Teams": "List of Formula One constructors"
}

output_file = "f1_knowledge.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for section_title, page_name in pages.items():
        page = wiki.page(page_name)
        if not page.exists():
            print(f"[❌] Page not found: {page_name}")
            continue

        print(f"[✅] Extracting: {page_name}")
        f.write(f"\n\n==== {section_title} ====\n\n")
        f.write(page.summary + "\n")
        f.write(page.text + "\n")

print(f"\n✅ Done! Data saved to {output_file}")
