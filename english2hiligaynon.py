"""A simple (baby-talk) translation of English words to Hiligaynon words.

Methods:
    hiligaynon_of(english_text)
"""
# For a serious study of Hiligaynon, see the Hiligaynon Dictionary by Cecile L. Motus
# published by the University of Hawaii Press, Honolulu 1971
# or see: https://scholarspace.manoa.hawaii.edu/server/api/core/bitstreams/ca6c4041-0aa8-41c0-9fe3-ea61ce2b1631/content

# Create the dictionary
hiligaynon = {
    # Sections: Noun, Pronoun, Verb, Adjective, Adverb, Preposition, Conjunction, and Interjection
    # Part 1: Pronouns
    "I": "Ako",
    "I am": "Ako",
    "you": "kamo",
    "he": "siya",
    "she": "siya",
    "we": "kami",
    "they": "sila",
    "me": "ako",
    "mine": "nakon",
    "him": "sa kanya",
    "her": "kanya",
    "us": "kami",
    "them": "sa kanila",
    "my": "ko",
    "your": "iyong",
    "of his": "ng kanyang",
    "our": "ang aming",
    "their": "ang kanilang",
    
    "yours": "inyo",
    "his": "niya",
    "hers": "niya",
    "ours": "naton",
    "theirs": "nila",
    
    # Particles
    "the": "ang",
    "of": "sang",
    "to": "sa",
    "to _NAME": "kay",
    "_NAME": "Si",
    "of _NAME": "ni _NAME",
    "_NAMES": "nanday",
    "of _NAMES": "kanday",
    
    # Nouns
    # "mine": "minahan",
}

_constants = {
    "_NAME": "", # of person, pet or dear thing
    "_PLACE": "",
}
def hiligaynon_of(english_text):
    """Get the Hiligaynon word for an English word.
    
    Return the value of the key in the dictionary if it exists, otherwise return the key
    """
    hiligaynon_text = ""
    for each_word in english_text:
        if each_word in hiligaynon:
            hiligaynon_text += hiligaynon_of(hiligaynon[each_word])
        else:
            hiligaynon_text += each_word
    
    return hiligaynon_text.capitalize()

if __name__ == "__main__":
    english_text = input("Enter an English word: ")
    print("In Hiligaynon is: ", hiligaynon_of(english_text))