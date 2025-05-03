"""A simple (baby-talk) translation of English words to Hiligaynon words.

Methods:
    hiligaynon_of(english_text)
"""
# For a serious study of Hiligaynon, see the Hiligaynon Dictionary by Cecile L. Motus
# published by the University of Hawaii Press, Honolulu 1971
# or see: https://scholarspace.manoa.hawaii.edu/server/api/core/bitstreams/ca6c4041-0aa8-41c0-9fe3-ea61ce2b1631/content

# Create the dictionary
hiligaynon_dict = {
    # Sections: Noun, Pronoun, Verb, Adjective, Adverb, Preposition, Conjunction, and Interjection
    
    # Pronouns - First Person Singular
    "i": "ako", # Nominative
    "of me": "nakon", # Genitive
    "to me": "sa akon", # Dative
    "me": "ako", # Accusative
    "from me": "gikan sa akon", # Ablative
    "with me": "upod sa akon", # Ablative
    "my": "ko", # Posessive
    "of mine": "nakon",
    "am": "amo",
    
    # Pronouns - First Person Plural
    "we": "kita",
    "of us": "kita",
    "to us": "sa aton",
    "us": "kita",
    "from us": "gikan sa aton",
    "our": "ang aton",
    "of our": "sang aton",

    # Pronouns - Second Person Singular
    "you": "ikaw", # Nominative
    "your": "iyong", # Genitive
    "of you": "nimo", # Genitive
    "to you": "sa imo", # Dative
    "_VERB you" : "ka", # Accusative
    "from you": "gikan sa imo", # Ablative
    "yours": "nimo", # Posessive

    # Pronouns - Second Person Plural
    "you all": "kamo", # Nominative
    "of you all": "ninyo", # Genitive
    "to you all": "sa inyo", # Dative
    "you people": "kamo", # Accusative
    "from you all": "gikan sa inyo", # Ablative
    "all yours": "inyo", # Posessive
    
    # Pronouns - Third Person Singular
    # Masculine
    "he": "siya",
    "his": "niya",
    "of him": "niya",
    "to him": "sa iya",
    "him": "siya",
    "from him": "gikan sa iya",
    # Feminine
    "she": "siya",
    "hers": "niya",
    "mine": "nakon",
    "her": "kanya",
    
    # Pronouns - Third Person Plural
    "they": "sila", # Nominative
    "them": "sila", # Accusative
    "their": "ang ila", # Possessive
    "theirs": "ila", # Possessive
    "of them": "nila", # Genitive
    "to them": "sa ila", # Dative
    "from them": "gikan sa ila", # Ablative
    "with them": "upod sa ila", # Ablative
    "of their": "sang ila", # Genitive
    "to their": "sa ila", # Dative
    "from their": "gikan sa ila nga", # Ablative
    "with their": "upod sa ila nga", # Ablative
    
    "ours": "naton", # Possessive
    "of ours": "sang aton", # Genitive
    "to ours": "sa aton", # Dative
    "from ours": "gikan sa aton", # Ablative
    "with ours": "upod sa aton", # Ablative
    
    # Particles
    "the": "ang",
    "of": "sang",
    "to": "sa",
    "to _NAME": "kay",
    "_NAME": "Si",
    "of _NAME": "ni _NAME",
    "_NAMES": "nanday",
    "of _NAMES": "kanday",
    
    # Verbs
    "are not": "indi",
    "am not": "indi ko",
    "is not": "indi",
    "not": "indi",
    "be": "mangin",
    "be not": "indi mangin",
    
    # Basic Actions
    "eat": "kaon",
    "drink": "inum",
    "sleep": "tulog",
    "walk": "lakat",
    "run": "dalagan",
    "sit": "lingkod",
    "stand": "tindog",

    # Nouns
    # Family Members
    "father": "amay",
    "mother": "nanay",
    "brother": "utod nga lalaki",
    "sister": "utod nga babayi",
    "grandfather": "lolo",
    "grandmother": "lola",
    "aunt": "tiya",
    "uncle": "tiyo",
    "cousin": "paka-isa",
    "son": "bata nga lalaki",
    "daughter": "bata nga babayi",
    "child": "bata",
    "children": "mga bata",
    "kids": "mga bata",

    # People
    "boy": "bata nga lalaki",
    "chef": "chef",
    "doctor": "doktor",
    "firefighter": "firefighter",
    "friend": "kaibigan",
    "girl": "bata nga babayi",
    "king": "hari",
    "man": "lalaki",
    "nurse": "nurse",
    "people": "katawhan",
    "person": "persona",
    "police": "pulis",
    "president": "presidente",
    "prince": "prinsipe",
    "princess": "prinsesa",
    "queen": "reyna",
    "student": "estudyante",
    "teacher": "guro",
    "woman": "babaye",
    "worker": "manug-ubra",
    
    # Food
    "food": "pagkaon",
    "viand": "sud-an",
    "rice": "bugas",
    "dried fish": "uga",
    "porridge": "lugaw",
    
    # Vegetables
    "vegetable": "utan",
    "squash": "kalabasa",
    "eggplant": "talong",
    "taro": "gabi",
    "tomato": "kamatis",

    # Fruits
    "fruit": "prutas",
    
    # Colors
    "color": "kolor",
    "black": "itum",
    "blue": "blue",
    "brown": "brown",
    "grey": "abu",
    "green": "green",
    "orange": "orange",
    "pink": "pink",
    "purple": "purple",
    "red": "pula",
    "white": "puti",
    "yellow": "yellow",
    
    # Sizes
    "size": "kadakuon",
    "sizes": "sizes",
    "small": "gamay",
    "large": "daku",
    "big": "daku",
    "tiny": "gaming",
    "tiny little": "kali",
    "small little": "kabi",
    "large little": "lagi",
    
    # Tastes
    "taste": "taste",
    "sour": "sour",
    "sweet": "sweet",
    "bitter": "bitter",
    "salty": "salty",
    
    # Qualities
    "quality": "kalidad",
    "handsome": "gwapo",
    "pretty": "gwapa",
    "fat": "tambuk",
    "thin": "niwang",
    
    # Animals
    "animal": "sapat",
    "dog": "idu",
    "cat": "kuring",
    "mouse": "ilaga",
    "rabbit": "rabbit",
    "bird": "pispis",
    "fish": "isda",
    "snake": "man-ug",
    "lizard": "tiki",
    "frog": "paka",
    "turtle": "ba-u",
    
    # Things
    "thing": "bagay",
    "things": "mga bagay",
    # Common Objects
    "house": "balay",
    "door": "pwertahan",
    "window": "bintana",
    "table": "lamesa",
    "chair": "silya",
    "bed": "katre",
    "book": "libro",

    
    # Weathers
    "weather": "klima",
    "rainy": "maulanon",
    "sunny": "maadlawon",
    "cloudy": "mapanganod",
    "stormy": "magal-um",
    
    # Seasons
    "season": "season",
    "spring": "spring",
    "summer": "tag-init",
    "autumn": "taglagas",
    "winter": "tag-ululan",
    
    # Indications
    "this": "ini",
    "that": "ina",
    "these": "ini sila",
    "those": "ina sila",
    "these things": "ini nga mga bagay",
    "those things": "ina nga mga bagay",

    # Common Greetings
    "hello": "kumusta",
    "good morning": "maayong aga",
    "good afternoon": "maayong udto",
    "good evening": "maayong gab-i",
    "goodbye": "ba-bye",
    "thank you": "salamat",
    "please": "palihog",

}

_constants = {
    "_NAME": "", # of person, pet or dear thing
    "_PLACE": "",
}
def hiligaynon_of(english_text):
    """Get the Hiligaynon word for an English word.
    
    Return the value of the key in the dictionary if it exists, otherwise return the key
    """
    # Initialize the Hiligaynon text container
    hiligaynon_text = ""
    # Remove non-alpha characters
    english_text = ''.join([i for i in english_text if i.isalpha() or i.isspace()])
    print(english_text)
    english_text = english_text.lower()
    # TODO: change the algorithm below by
    # splitting the text into words first
    # initialize the found_hiligaynon_text to ""
    # then start looping through the words,
    # add the word to found_hiligaynon_text
    # if word is in the dictionary
    # assign it to found_hiligaynon_text
    # and then continue to next word
    # and check if the found_hiligaynon_text is in the dictionary
    # and if it is, assign it to the same found_hiligaynon_text
    # else return the hiligaynon_dict[found_hiligaynon_text]
    
    if english_text in hiligaynon_dict:
        hiligaynon_text = hiligaynon_dict[english_text]
    else:
        if len(english_text.split()) > 1:
            # Assign the last word to a variable
            last_word = english_text.rsplit(' ', 1)[1]
            # Translate the last word using hiligaynon_dict
            last_word = hiligaynon_dict.get(last_word, last_word)
            # Trim the english_text of the last word
            english_text = english_text.rsplit(' ', 1)[0]
            # Combine the translated last word with the rest of the text
            hiligaynon_text = f"{hiligaynon_of(english_text)} {last_word}"
        else:
            # Just return the English text for now
            hiligaynon_text = english_text
    
    return f"{hiligaynon_text[0].upper()}{hiligaynon_text[1:]}"

if __name__ == "__main__":
    english_text = input("Enter an English word: ")
    print(f"In Hiligaynon is: {hiligaynon_of(english_text)}")
