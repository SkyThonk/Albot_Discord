def valo_validity_check(str):
    if '#' in str:
        li = str.split('#')
        if len(li) == 2:
            if len(li[1]) == 4:
                if li[1].isnumeric():
                    if ' ' in  li[0]:
                        l2 = li[0].split()
                        l2 = ''.join(l2)
                        if l2.isalpha() or l2.isalnum():
                            return True
                        else:
                            return False
                    else:
                        if li[0].isalpha() or li[0].isalnum():
                            return True
                        else:
                            False       
            else:
                return False
        else:
            return False
    else:
        return False
