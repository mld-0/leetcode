
class Solution:

    #   Brute force solution - time limit exceded
    def longestPalindrome_First(self, s: str) -> str:
        result = ""
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                loop_str = s[i:j]
                print("loop_str=(%s)" % loop_str)
                if self.is_palindrome(loop_str):
                    if len(loop_str) > len(result):
                        result = loop_str
        return result
 
    def is_palindrome(self, s: str, start: int, end: int, palindromes: list) -> bool:
        result = s == s[::-1]
        return result


    #   Dynamic programming solution - time limit exceded?
    def longestPalindrome(self, s: str) -> str:
         #   longest palindrome is given by s[start:end]
        start = 0  
        end = 1 
        #   table[i][j] -> True if s[i:j+1] is a palindrome
        table = [[False for x in range(len(s))] for y in range(len(s))]
        #   All substring of length 1 are palindromes
        i = 0
        while (i < len(s)):
            table[i][i] = True
            i += 1
        #   Substrings of length 2 are palindromes if start/end letter match
        i = 0
        while i < (len(s) - 2 + 1):
            if (s[i] == s[i+1]):
                table[i][i+1] = True
                start = i
                end = start + 2
            i += 1
        #   Substrings of length k are palindromes if start/end letter match, 
        #   and table[start][end] describes a palindrome
        k = 3
        while k <= len(s):
            i = 0
            while i < (len(s) - k + 1): 
                j = i + k - 1  #  end index of substring:
                if (s[i] == s[j] and table[i+1][j-1] == True):
                    table[i][j] = True
                    if k > end-start:
                        start = i
                        end = j + 1
                i += 1
            k += 1
        return s[start:end]


    #   LINK: https://leetcode.com/problems/longest-palindromic-substring/discuss/900639/Python-Solution-%3A-with-detailed-explanation-%3A-using-DP
    def longestPalindrome_Ans(self, s: str) -> str:
       longest_palindrom = ''
       dp = [[0]*len(s) for _ in range(len(s))]
       #filling out the diagonal by 1
       for i in range(len(s)):
           dp[i][i] = True
           longest_palindrom = s[i]
       # filling the dp table
       for i in range(len(s)-1,-1,-1):
	   		# j starts from the i location : to only work on the upper side of the diagonal 
           for j in range(i+1,len(s)):  
               if s[i] == s[j]:  #if the chars mathces
                   # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                   #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                   if j-i ==1 or dp[i+1][j-1] is True:
                       dp[i][j] = True
                       # we also need to keep track of the maximum palindrom sequence 
                       if len(longest_palindrom) < len(s[i:j+1]):
                           longest_palindrom = s[i:j+1]
               
       return longest_palindrom 


s = Solution()

text = "cbbd"
check = "bb"
result = s.longestPalindrome_Ans(text)
print("result=(%s)" % result)
assert(result in check)

text = "a"
check = "a"
result = s.longestPalindrome_Ans(text)
print("result=(%s)" % result)
assert(result in check)

text = "ac"
check = [ "a", "c" ]
result = s.longestPalindrome_Ans(text)
print("result=(%s)" % result)
assert(result in check)

text = "nmxyncuzlwhiobggiowtjexyzbzyhuqmpnyyimazcrnhrnkydxnioqhtchnnoqhuezypyxiepdvyesihlvbuzctptsaowfllxfdqvbwyitsegpbarqqpcrrvemwkglouhhtuxjdeppatdiiwhwvrqxqjcmzhuwurlqrshlsjyxksfjmhykyhcbpmrbsmbrrjwndjsgqdrafidmelnobhtpblozbzttpzheeffwysfrrwtewjnmqoyrvfxmgcmdoadagatwyocixggwppnmtrnfrbiijwojpetuqwknvtqgspuogrbqqptsrljjiaalmqlchlszflyixxpnkttzbrvhzrjzfbpuquuyzwhattxvoqpzieguwvmlrggrlmvwugeizpqovxttahwzyuuqupbfzjrzhvrbzttknpxxiylfzslhclqmlaaijjlrstpqqbrgoupsgqtvnkwqutepjowjiibrfnrtmnppwggxicoywtagadaodmcgmxfvryoqmnjwetwrrfsywffeehzpttzbzolbpthbonlemdifardqgsjdnwjrrbmsbrmpbchykyhmjfskxyjslhsrqlruwuhzmcjqxqrvwhwiidtappedjxuthhuolgkwmevrrcpqqrabpgestiywbvqdfxllfwoastptczubvlhiseyvdpeixypyzeuhqonnhcthqoinxdyknrhnrczamiyynpmquhyzbzyxejtwoiggboihwlzucnyxmn"
check = ""
result = s.longestPalindrome_Ans(text)
print("result=(%s)" % result)


text = "fjnfkfbfeuujctmyttwidcrdjtkfoaylsceqqzzmkpyvljkwcxxtmxiwkrgoahxztuppnvxhyionhpakvjoizdzcqxuyaidjadrhfhuhbncijokbthvuigjytipgygnonhgkpvsqimxpslmptieumhunjlafttjstaxnivrpqcxrgocvaicpwfnmtkgbjnbfopxaiduqihomrdmhzzyzddytiqdjzmmqwmeyoqnttmiujobihdifkbntpphjhgxzbjpulnokvceohloltyosddbopgkllcxzzkfzmkywxlpkdjlorgorxzownuajjzcxuhyqexfklssbtralzlvdbtxapccipvvgjtusfsanvnyehpkwirygqogtsicwycgnajwekuzffhlsvfgqwpbuinwhvpqxjhamhxayicchmxmurakhzhoghnupohaqanduhjkegggpyetwebcjgavpspfjaoakjkktaxwehpyqvsczhbbhzcsvqyphewxatkkjkaoajfpspvagjcbewteypgggekjhudnaqahopunhgohzhkarumxmhcciyaxhmahjxqpvhwniubpwqgfvslhffzukewjangcywcistgoqgyriwkpheynvnasfsutjgvvpiccpaxtbdvlzlartbsslkfxeqyhuxczjjaunwozxrogroljdkplxwykmzfkzzxcllkgpobddsoytlolhoecvkonlupjbzxghjhpptnbkfidhibojuimttnqoyemwqmmzjdqityddzyzzhmdrmohiqudiaxpofbnjbgktmnfwpciavcogrxcqprvinxatsjttfaljnuhmueitpmlspxmiqsvpkghnongygpityjgiuvhtbkojicnbhuhfhrdajdiayuxqczdziojvkaphnoiyhxvnpputzxhaogrkwixmtxxcwkjlvypkmzzqqecslyaofktjdrcdiwttymtcjuuefbfkfnjf"
result = s.longestPalindrome_Ans(text)
print("result=(%s)" % result)
