def isPalindrome(str):
    letters = [x for x in str]
    if len(letters) % 2 == 0:
        odd_count = 0
        for i in letters:
            if letters.count(i) % 2 != 0:
                odd_count += 1
                letters = [x for x in letters if x != i]
        return True if odd_count < 1 else False
    else:
        even_count = 0
        odd_count = 0
        for i in letters:
            if letters.count(i) % 2 == 0:
                even_count += 1
                letters = [x for x in letters if x != i]
            else:
                odd_count += 1
                letters = [x for x in letters if x != i]
        return True if even_count % 2 == 0 and odd_count == 1 else False
