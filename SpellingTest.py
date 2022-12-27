import sys

def spelling_test(s, l):
    in_list = []
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            spelling_test_helper(s, l, i, j, in_list)
    
    string = ""
    for item in in_list:
        string += item

    if string == s:
        return True

    return False


def spelling_test_helper(s, l, start_index, end_index, in_list):
    if s[start_index:end_index] in l:
        in_list.append(s[start_index:end_index])
        l.remove(s[start_index:end_index])

        if end_index + 1 != len(s):
            end_index += 1
            return spelling_test_helper(s[start_index:end_index], l, start_index, end_index, in_list)
        
        else:
            return spelling_test_helper(s[start_index:], l, start_index, end_index, in_list)
    
    else:
        return False
        
        


def main():
    s = input()
    lines = sys.stdin.readlines()

    print(spelling_test(s, [line.replace('\n', '') for line in lines]))

if __name__ == "__main__":
    main()
