def double_word(word):
  dw = word * 2
  return dw + str(len(dw))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

def initials(phrase):
    words = phrase.upper
    result = ""
    for word in words:
        result += ___
    return ___

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS