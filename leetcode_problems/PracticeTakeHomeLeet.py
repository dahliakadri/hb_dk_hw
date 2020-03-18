# 100 --> 'one hundred'
# 345223 --> 'three hundred forty five thousand two hundred twenty three'
# 140000 -> 'one hundred forty thousand'

#turn into string 
#string_num = str(num)
#count the length of the number
#if len > 3 lastword of first set of 3 = thousand
#if len < 3 
# if len == 1:
# return WORDS[string_num]


WORDS =  {
  0: 'zero',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
}

def convert_num_to_string(num):
    if num < 19:
        return get_teens_and_below(num)
    if num > 19 and num < 100:
        return get_words_below_100_above_teen(num)

def get_words_below_100_above_teen(num):
    string_num = str(num)
    word_1 = WORDS[int(string_num[0] + '0')]
    if string_num[1] == 0:
        return word_1
    else:
        word_2 = WORDS[int(string_num[1])]
        return word_1 + ' ' + word_2

def get_teens_and_below(num):
    return WORDS[num]

print(convert_num_to_string(0))