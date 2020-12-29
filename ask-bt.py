from operator import itemgetter, attrgetter
import sys
import re

def calculate_frequencies(file_contents, uninteresting_words, removable_words, recognised_phrases):
    # Start with empty clean word list
    clean_list = []

    # Remove unwanted strings
    words_removed = file_contents.lower()
    for word in removable_words:
        words_removed = words_removed.replace(word.lower(), " ")

    # Remove URL's
    words_removed = re.sub('http[s]?:\/\/([^\/\s]+\/)(.*)', '', words_removed)

    # Remove punctuation
    clean_file_contents = ""
    for character in words_removed:
        if character.isalpha() is True:
            clean_file_contents = clean_file_contents + character
        else:
            clean_file_contents = clean_file_contents + " "

    for phrase, replacement in recognised_phrases:
        occurrences = clean_file_contents.count(" " + phrase.lower() + " ")
        for i in range(0, occurrences):
            clean_list.append(replacement.lower())
        clean_file_contents = clean_file_contents.replace(" " + phrase.lower() + " ", " ")

    # Separate the text into Words
    list_file_contents = clean_file_contents.split()

    # Check for uninteresting Words in list
    for word in list_file_contents:
        if word.lower() not in uninteresting_words:
            clean_list.append(word.lower())

    # Creating frequencies dictionary
    frequencies = {}
    for word in clean_list:
        if word not in frequencies:
            frequencies[word] = 0
        frequencies[word] += 1
    return frequencies

input_file = sys.argv[1]
file = open(input_file)
file_contents = file.read()
file.close()

# Here is a list of punctuations and uninteresting words you can use to process your text
#punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "on", "in", "an", "as", "i", "me", "my", \
"we", "our", "for", "not", "m", "t", "s", "there", "able", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
"their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", \
"www", "org", "com", "ltd", "co", "ebook", "hello", "hi", "bt", "tnx", "thanks", "thank", "screenshot", "png", \
"reply", "someone", "please", "need", "via", "help", "team", "get", "issue", "having", "now", "up", "so", "workday", \
"tried", "working", "getting", "ve", "about", "issues", "out", "today", "into", "don", "then", "done", "trying", "also", \
"should", "says", "morning", "evening", "look", "see", "cannot", "use", "icon", "call", "something", "would", "seem", \
"after", "edited", "like", "received", "change", "added", "yesterday", "through", "new", "anyone", "requires", \
"share", "assist", "days", "pm", "know", "open", "message", "others", "trouble", "face", "facing", "work", "ad", "hey", "h" \
"o", "fix", "smiling", "could", "shot", "p", "x", "still", "changes", "snag", "ago", "day", "possible", "didn", "error", \
"connect", "access", "unable", "able", "take", "last", "click", "back", "along", "using", "request", "jpg", "only", "re", "again", "one" \
"good", "got", "longer", "hours", "go", "because", "o", "one", "slightly", "however", "allowed", "allow", "every", "find", "way" \
"advise", "activity", "changed", "connection", "file", "want", "same", "asking", "used", "nothing", "even", "good", "anymore", "create" \
"times", "isn", "sure", "assistance", "make", "times", "seems", "problem", "try", "f", "d", "version", "add"]

removable = [":eyes:", ":heavy_tick:", "replies", "view thread", "days ago", ":panda_dogeza:", "image.png", \
"image from iOS", "Last reply", "Hi team", "Hi BT", "Hi Bt", "Hi bt", "Hello team", ":slack:", "#ask-bt", "(edited)", "seems like", "looks like", "IT Slack Admin", "Screen Shot", "best way", "as well" \
"log in", "log into", "log onto", "log to", "logging"]

replace = [("sfdc","salesforce"), ("windows","windows10"), ("salesforce","salesforce"), ("global protect","gpvpn"), ("vpn","gpvpn"), ("gp","gpvpn"), ("globalprotect","gpvpn"),
("global connect","gpvpn"), ("service request","servicenow"), ("service ticket","servicenow"), ("ticket inc","servicenow"), ("ticket ritm","servicenow"), ("request ritm","servicenow"),
("ticket","servicenow"), ("req","servicenow"), ("ritm","servicenow"), 
("servicenow","servicenow"), ("google drive","googledrive"), ("Enterprise Connect","enterpriseconnect"),("EC","enterpriseconnect"), ("zoom meeting","zoom"), ("zoom computer","zoom"),
("my computer","laptopcomputer"), ("computer","laptopcomputer"), ("laptop","laptop-computer"), ("email","outlook"), ("outlook","outlook"), ("mailbox","outlook"), ("onenote","onenote"), (".one","onenote"),
("one note","onenote"), ("sentinel one","sentinelone"), ("sentinelone","sentinelone"), ("onedrive","onedrive"), ("one drive","onedrive"), ("user name","username"), ("username","username"),
("rsa token","rsatoken"), ("token","rsatoken"), ("support phone number", "supportphonenumber)"), ("ssh key", "sshkey"), ("ftp key", "sshkey"), ("public key", "sshkey"), ("recovery key", "bitlocker"),
("licence key", "licencekey"), ("us vcr", "vcr"), ("plug in", "plugin"), ("okta", "okta"), ("okta tile", "okta") ]

#keep_words = ["zoom", "zoom call", "global protect", "log into", "slack workspace", "Pinned by BT Comms", "computer isn’t turning on"]

result = []
for key, value in calculate_frequencies(file_contents, uninteresting, removable, replace).items():
    result.append((key, value))

sorted_results = sorted(result, key=itemgetter(1), reverse=True)

i = 0
for name, count in sorted_results:
    if i < 50:
        i = i + 1
        for n in range(0,count):
            print (name, end=",")
print ()

print(input_file)
i = 0
for name, count in sorted_results:
    if i < 50:
        i = i + 1
        print (count, name)
