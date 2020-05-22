Longest Prefix Match

Given an array of prefixes determine the loggest prefix matches for each of the phone numbers. Out is an array of prefixes corresponding to the longest matches for each input phone number.

prefixes = [prefix, prefix. prefix, ect]
prefix example +1223 +1455 +2456 can be up to 15 digits
numbers = [number, number, number, ect.]
number example +123456678, can be up to 15 digits


the match function should return an array of prefixes, one for each input number, with an empty strng when no prefixes match a number





SMS Splitting
Given an input string of any length, output SMS-compliant segments with suffixes

SMS is 60 characters or less
Do not generate segments if the input fits in a single message
a segment suffix looks like "(1/5)" fir the first of five segments
Segment content and suffix must both fit in the segment

def segments (message)



return array of segments