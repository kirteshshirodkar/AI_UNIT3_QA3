import re

def library_chatbot(user_input):
    user_input = user_input.lower()

    # Rule 1: Library Hours
    if re.search(r"(open|opening|timing|hours)", user_input):
        return "📚 The library is open from 9:00 AM to 6:00 PM, Monday to Friday."

    # Rule 2: Book Availability
    elif re.search(r"(book|available|availability)", user_input):
        return "📖 You can check book availability at the library counter or through the library catalog."

    # Rule 3: Membership Information
    elif re.search(r"(membership|member|join)", user_input):
        return "📝 Students can register for library membership by submitting a valid ID card."

    # Rule 4: Book Issue Rules
    elif re.search(r"(issue|borrow|take)", user_input):
        return "📘 A student can issue up to 3 books for a period of 14 days."

    # Rule 5: Book Return Rules
    elif re.search(r"(return|due|submit)", user_input):
        return "📕 Books must be returned within 14 days from the date of issue."

    # Rule 6: Late Fine Information
    elif re.search(r"(fine|late|penalty)", user_input):
        return "💰 Late return fine is ₹2 per day per book."

    # Rule 7: Librarian Contact
    elif re.search(r"(librarian|contact|help)", user_input):
        return "☎️ You can contact the librarian at library@college.edu."

    # Rule 8: Exit
    elif re.search(r"(exit|quit|bye)", user_input):
        return "👋 Thank you for using the Library Chatbot. Have a great day!"

    # Default Rule
    else:
        return "❓ Sorry, I didn't understand your query. Please ask about library services."

def main():
    print("📚 Welcome to the Library Chatbot")
    print("Type 'bye' to exit\n")

    while True:
        user_input = input("You: ")
        response = library_chatbot(user_input)
        print("Bot:", response)

        if re.search(r"(exit|quit|bye)", user_input.lower()):
            break

if __name__ == "__main__":
    main()
