#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import defaultdict
from functools import cache
from typing import List, Optional

class Solution:
    """word_a is a predecessor of word_b iff the latter can be formed from the former by inserting a single letter. Determine the length of the longest sequence of words where each word is a predecessor of the previous that can be formed from the strings in `words` (in any order)"""

    #   memory limit exceded
    def longestStrChain_i(self, words: List[str]) -> int:
        #   {{{

        def is_predecessor(wordA: str, wordB: str) -> bool:
            if len(wordA) + 1 != len(wordB):
                return False
            l = 0
            r = 0
            while l < len(wordA):
                if wordA[l] == wordB[r]:
                    l += 1
                if l != r and l != r + 1:
                    return False
                r += 1
            return True

        @cache
        def build_sequences(word: str) -> List[List[str]]:
            if word not in successors:
                return [ [], ]
            result = []
            for sucessor in successors[word]:
                sucessor_sequences = build_sequences(sucessor)
                for sucessor_sequence in sucessor_sequences:
                    temp = [ sucessor, *sucessor_sequence ]
                    result.append(temp)
            return result

        words = list(set(words))
        words.sort(key = lambda x: len(x))
        successors = defaultdict(list)
        for i, wordA in enumerate(words):
            for j, wordB in enumerate(words):
                if i == j:
                    continue
                if is_predecessor(wordA, wordB):
                    successors[wordA].append(wordB)
        sequences = dict()
        result = 0
        for wordA in successors:
            sequences = build_sequences(wordA)
            max_length = max( [ len(x) for x in sequences ] )
            result = max(result, max_length)
        return 1 + result
        #   }}}


    #   runtime: beats 6%
    def longestStrChain_ii(self, words: List[str]) -> int:
        #   {{{

        def is_predecessor(wordA: str, wordB: str) -> bool:
            if len(wordA) + 1 != len(wordB):
                return False
            l = 0
            r = 0
            while l < len(wordA):
                if wordA[l] == wordB[r]:
                    l += 1
                if l != r and l != r + 1:
                    return False
                r += 1
            return True

        @cache
        def build_sequences(word: str) -> int:
            if word not in successors:
                return 0
            result = 0
            for sucessor in successors[word]:
                result = max(result, 1 + build_sequences(sucessor))
            return result

        successors = defaultdict(list)
        for i, wordA in enumerate(words):
            for j, wordB in enumerate(words):
                if i == j:
                    continue
                if is_predecessor(wordA, wordB):
                    successors[wordA].append(wordB)
        result = 0
        for wordA in successors:
            result = max(result, build_sequences(wordA))
        return result + 1
        #   }}}


    #   runtime: beats 35%
    def longestStrChain_iii(self, words: List[str]) -> int:

        def is_predecessor(wordA: str, wordB: str) -> bool:
            if len(wordA) + 1 != len(wordB):
                return False
            l = 0
            r = 0
            while l < len(wordA):
                if wordA[l] == wordB[r]:
                    l += 1
                if l != r and l != r + 1:
                    return False
                r += 1
            return True

        @cache
        def build_sequences(word: str) -> int:
            if word not in successors:
                return 0
            result = 0
            for sucessor in successors[word]:
                result = max(result, 1 + build_sequences(sucessor))
            return result

        words_by_len = defaultdict(list)
        for word in set(words):
            words_by_len[len(word)].append(word)
        successors = defaultdict(list)
        for l in words_by_len:
            for wordA in words_by_len[l]:
                if l+1 not in words_by_len:
                    continue
                for wordB in words_by_len[l+1]:
                    if is_predecessor(wordA, wordB):
                        successors[wordA].append(wordB)
        result = 0
        for wordA in successors:
            result = max(result, build_sequences(wordA))
        return result + 1


    def longestStrChain_ans_LongestIncreasingSubsequence(self, words: List[str]) -> int:
        raise NotImplementedError()


    def longestStrChain_ans_DP_TopDown(self, words: List[str]) -> int:
        raise NotImplementedError()


    def longestStrChain_ans_DP_BottomUp(self, words: List[str]) -> int:
        raise NotImplementedError()


def test_is_predecessor():
    #   {{{
    def is_predecessor(wordA: str, wordB: str) -> bool:
        if len(wordA) + 1 != len(wordB):
            return False
        l = 0
        r = 0
        while l < len(wordA):
            if wordA[l] == wordB[r]:
                l += 1
            if l != r and l != r + 1:
                return False
            r += 1
        return True
    inputs = [ ("a","b"), ("a","ba"), ("ba","bda"), ("bda","bdca"), ("xb","xbc"), ("xbc","cxbc"), ("cxbc","pcxbc"), ("pcxbc","pcxbcf"), ("abcd","dbqca"), ]
    checks = [ False, True, True, True, True, True, True, True, False, ]
    assert len(inputs) == len(checks), "input/check lists length mismatch"
    assert len(inputs) > 0, "No input"
    for (wordA, wordB), check in zip(inputs, checks):
        result = is_predecessor(wordA, wordB)
        assert result == check, "test_is_predecessor(): Check comparison failed"
    #   }}}
test_is_predecessor()

s = Solution()
test_functions = [ s.longestStrChain_i, s.longestStrChain_ii, s.longestStrChain_iii, s.longestStrChain_ans_LongestIncreasingSubsequence, s.longestStrChain_ans_DP_TopDown, s.longestStrChain_ans_DP_BottomUp, ]
#test_functions = [ s.longestStrChain_iii, ]

#   {{{
inputs = [ ["a","b","ba","bca","bda","bdca"], ["xbc","pcxbcf","xb","cxbc","pcxbc"], ["abcd","dbqca"], ["czgxmxrpx","lgh","bj","cheheex","jnzlxgh","nzlgh","ltxdoxc","bju","srxoatl","bbadhiju","cmpx","xi","ntxbzdr","cheheevx","bdju","sra","getqgxi","geqxi","hheex","ltxdc","nzlxgh","pjnzlxgh","e","bbadhju","cmxrpx","gh","pjnzlxghe","oqlt","x","sarxoatl","ee","bbadju","lxdc","geqgxi","oqltu","heex","oql","eex","bbdju","ntxubzdr","sroa","cxmxrpx","cmrpx","ltxdoc","g","cgxmxrpx","nlgh","sroat","sroatl","fcheheevx","gxi","gqxi","heheex"],
["biltnzk","jxwakrfxsifoj","uzdwyaxvcsr","sqqgkhwbf","tnoftkolx","ipmtvxcwe","zsucxrqkhahuo","qngglugvm","kvohqyedig","njoxacsnddwrg","vwtnxw","kjjourlrzpgeem","xcs","pfsgimurs","lsifyg","uzwyxcsr","muzdwcyanxvcstr","teqyrlhbvcv","rkga","tudezgzbnzb","uzwyaxvcsr","qvzkmgfulby","x","muzdwcyianxvcstr","koqyig","gl","aqcacmy","pmvwe","eskofqduddkhykr","pm","saxxd","ds","iemm","tudegzbz","yipsawmxbp","qyrlhbvcv","yxuhwkzvoczoz","zsucxqkahuo","kga","zwziivbijeiig","wffaheemjnjahzdd","zcxkahuo","djjjsulms","plxh","ffpasoizwhtu","zwziivijeii","fyvpzegautteiv","qszaitzfzv","uwoghcy","qqgkhwbf","eteqyrllhbvcvg","qknspkhngorof","qwvzkmgfuljbyz","grkte","grikrnwezryi","xjbpvekneaxn","cy","wnhnyqmpbsum","m","offqllgj","plxhib","omblqcoktkyf","pasw","prsngzx","offlj","rvvudgpixa","djjjjsulmmrs","gt","mpfsgimurs","cxkahuo","ipmtvxcwue","pqrbaoquxqemv","prqqv","tnoftfkolx","jfzzaw","rshquwmrboghccy","ebqhvwewzzmqif","rrd","dvjjjjqsulmmrs","pfsiurs","crnruydj","rvqgeqql","djsums","prbaquqemv","bs","dzytccvny","kce","llfv","jfzaw","qwvzkmgbfuljbyz","kgieph","hnympsum","ewv","vfgel","rklga","llzqbfv","gte","jckqurkg","qngglugm","tudgzbz","ipmvcwe","rr","kkcev","djjjjsulmrs","llqbfv","offqlgj","paswu","tlrlcnnrsrf","jcckqurkg","jjourlpgeem","nvl","shquwmrboghccy","vncfgelm","dgcdgjcksk","vvhvmibflb","juifgeqkaectlcj","scvdl","whcy","yipswmbp","wcy","hbqq","bsth","etjurltvpsuy","dzvytcccevnceyq","apqrbaoquxqemv","kvohuqyediyig","lenybbukzftz","ffpasoiuztwhtu","lzlhzqibfv","wfeemjnjahzdd","djsulms","xtudezgzbnzb","eemjhzdd","scavdil","guchrvaqbe","nvll","sxzfpzjmxvu","dytccvny","grikrnjwezryi","prng","ntvmcwwpzo","laqgcacyxmym","mglosifyg","nynvlqll","vwtn","lh","zhhxducgelhy","prg","kghierph","zsucxrqkhahuom","kvohqydig","eemjhzd","offiqcdllgji","dyc","toflx","dzvytccvney","ghvb","to","guchrvab","wyimthhfzndppwt","elbqhvwewzzmqif","hkghiyerph","hkghiyejrph","hlsioorugbsuu","c","kgierph","bstbghj","prbquqev","mpfsdgimurs","zfpjvu","zfpvu","yxuhwkzvoczfgoz","gel","ntvmcpzo","ekofqduddkhykr","ekofqdddhykr","rqeql","nhnympsum","xhoqlfolk","ipmtvxcwuje","wgmhjhdmnqot","bsh","rvncfgelm","hkahpbb","lzlzqibfv","xoqlfok","tnoftfkogwgplx","ekofqdddkhykr","zwiieii","ujfzzaw","jfzw","djsms","scavdpilj","tnoftfkoglx","ps","vwtnw","scavhdpilj","scayvhdpuilji","pdrshqngzx","crnrud","wmhjhdmnqot","wghmhjhdmnqot","vbyipsawmxbp","qknsapkhngorof","wymthhfzndppwt","wxcs","dzvytccevney","acacmy","dycy","teqyrllhbvcv","uzwyxcs","wmhjhdmnqt","qvzkmgfulbyz","qngglum","zhhxgdyukcgelhy","oj","iljes","bstbh","laqcacxmy","tofx","ke","yivkqoek","djjjsulmrs","lbirdzvttzze","l","zhhxgdukcgelhy","grikvrnjwezryi","bltz","npynvlqll","gvb","okzrs","urbarfkmnlxxn","qsyzaixtzfazv","dytcy","h","kohqyig","hgri","ojdxm","ujfdfzzaw","qyrhbvcv","ebqhvwewzmqif","uzwxcs","lebzf","ysijvkwqmoekromh","wffaeemjnjahzdd","crnrduyndj","ujfdmfzzaw","laqgcacyxmzgym","jjourlrpgeem","kvohqyediyig","lebukzf","zwiijeii","guchrvb","omoktkyf","hpgt","yikoek","ysijvkwqoekromh","tvpo","ysijvkqoekromh","xbgq","d","abmtk","ors","rnrd","xzrugvlzduaxhzc","njoxacjsnddwrg","yipswmxbp","xqsyzaixtzfazv","urbrfknlxxn","sxzfpjxvu","prbaquxqemv","dvjjjjsulmmrs","kviahvqu","urbfknx","qvmgfulby","yikqoek","zsucxrqkhfahuomm","koqyg","djss","moxpfsdgimlurs","qeql","urbrfknlxn","kgieh","qnspkhngorof","plxyhib","scyayvhdpuiljki","vvhvmbflb","lpzluhzqxibfv","kkcbev","hpzgty","nyvlqll","kvahvu","rklgja","ipmtavxcwuje","lbirdzvvttzze","psw","fpasoiwhtu","dgcdgjckk","qknhsapkhngorof","qszaixtzfazv","tvp","abmtvk","uwrboghcy","hbq","crnruyd","etjurltvsuy","etjurltyvpsuy","lenbukzf","teqyrllhbvcvg","ipmvwe","o","crnryduyndj","lbirdzvvqfttzze","tnoftfkowglx","ipmtavxcwujre","omlcoktkyf","rnperyemtmqh","bltnzk","sxzfpzjxvu","uzdwyaxvcstr","bq","rvvugpixa","laqcacxmym","wffeemjnjahzdd","fpvu","xjbpvekngeyaxbn","dzvytccevncey","qgly","scavdl","fw","tox","toftklx","prbaoquxqemv","ztrobzqiukdkcbv","yivkqoekr","feemjnjhzdd","plxhi","cp","fyvpzgauttei","prshqngzx","kplxyrhib","suwrboghcy","kviahvu","mvwe","dzvytccvny","hbqwq","prbquqemv","lzlhzqxibfv","ll","omblcoktkyf","toftlx","lpzlhzqxibfv","tudegzbnz","ddgcdgjcgkspk","kgih","xjbpvekneaxbn","suwrboghccy","zwiiijeii","dytccy","ympsum","jxwakfxsifoj","uwhcy","yxuhwkzvoczfoz","xzfpjvu","lenybbukzft","b","llqfv","laqgcacyxmgym","xq","scavdilj","zwziivbijaeiig","scyayvhdpuilji","amvevfulhsd","dss","tlrlcnnrs","uzwyaxcsr","qspkhngorof","etjurtvsuy","wgqhmhjhhdmnqot","tvmpo","tnoftklx","qgflby","mlosifyg","oqyg","gchvb","t","offqcdllgj","ziieii","zwziivbijeii","vp","lpb","fyvprzegauttejiv","vtn","amefulhsd","llf","muzdwyaxvcstr","zucxqkahuo","pfsgiurs","obstbghj","ipmqtavxcwuzjrbe","djjsulms","qvmgflby","ljpzluhzqxibfv","jjourlrzpgeem","zrugvlduaxhzc","xbpvkneaxn","ljpzluhzgqyxibfv","yivkqoekrh","laqcacyxmym","nyvll","muzdwcyaxvcstr","fyvpzegauttejiv","offlgj","vnfgelm","eteiqyrllhbvcvg","zsucxrqkhahuomm","ibiltnzk","rklgjae","fpasoizwhtu","t","zhhxdukcgelhy","fpasoiwu","xzfpjxvu","tlrlcnnrysrf","ojx","mpum","lxh","eturtvsuy","rklgbjaae","kahpbb","qngglugmfvmp","fielbqtcri","xzruogvlzduaxhzc","rshquwmrbtoghccy","nyvlll","lbirdzvvqttzze","dgcdgjckspk","vvhvmibfilb","dzvytcccevncey","g","vwe","zwxcs","k","jourlpgeem","cpk","cds","tlrlcnnrsr","ivemm","fgel","grktse","urbfknlxn","qwvzkmgfulbyz","xjbpvekngeaxbn","wphuutlgczfspyga","xbq","offqcdllgji","vbyipsakwmxbp","qyrhbvc","ygzpztbno","xhogqlfolk","ujffzzaw","xbnmgq","uwohcy","rnperyemqh","prbqqev","lenybukzf","mxpfsdgimurs","ga","hpt","moxpfsdgimurs","vb","offqcllgj","rklgbjae","lifg","ztrobzzqiukdkcbv","xoqok","cs","snaxxd","cdds","qknhsapkhngorohf","rvqgeql","rnperyemmqh","scavhdpuilji","urbfknlx","rvvugixa","ygzpztbndon","zrugvlzduaxhzc","shuwmrboghccy","mlsifyg","xhoqlfok","wfeemjnjhzdd","lbzf","wythhfzndppwt","mglqosifyg","ojxm","kvohuqyevdiyig","grte","prsngz","eteeiqyrllhbvcvg","dytccny","qngglugfvmp","kohqydig","fu","qgfly","tvmcpzo","tnoftfkowgplx","zruglduaxzc","yijvkqoekrh","xqsyzaixtzfdazv","ipmqtavxcwuzjre","omloktkyf","ympum","lzlzqbfv","pasowu","rvqeql","qngglugvmp","hkghierph","eemjhz","feemnjhzdd","c","yxpuhwkzvoczfgoz","dgcgjckk","lbz","yxuwkzvoczoz","zrugvlduaxzc","ntvmcwpzo","fzw","ygzpmztbndon","rvncfgxelm","mpm","tudezgzbnz","bltzk","ffpasoiuzwhtu","cd","r","okrs","byipsawmxbp","prsqngzx","wnhnyqmpsum","ipmqtavxcwujre","w","fpasoiwtu","plxyrhib","bstbhj","xbnmrgq","ipmtvcwe","urbfkn","nympsum","qtngglugmfvmpt","jckqurg","hgr","hpzgt","rvvxudgpixa","ysijvkqoekrh","lebkzf","guchvb","kvohqyediyg","amvefulhsd","suwmrboghccy","fvu","ibdiltnzk","rnrud","iem","urbarfknlxxn","ygzpztbnon","prsng","zcxqkahuo","ffpeasoiuztwhtu","laqcacmy","qszaitzfazv","xbngq","qvkmgfulby","scavhdpuilj","zsucxrqkahuo","v","qtngglugmfvmp","ysijvkqoekrmh","lfg","prqqev","pasoiwu","p","tvmcpo","kcev","im","crnrduydj","vfgelm","ddgcdgjckspk","ivqemm","ljpzluhzgqxibfv","lenybukzft","nhnyqmpsum","iljesr","hp","tqyrlhbvcv","eemnjhzdd","xbpvekneaxn","wghmhjhhdmnqot","uwboghcy","guchrvabe","xoqfok","fyvpzgautteiv","pg","zwiivijeii","qvgflby","lsifg"],
          ]
checks = [ 4, 5, 1, 9, 16, ]
#   }}}
inputs = [ ["a","b","ba","bca","bda","bdca"], ["xbc","pcxbcf","xb","cxbc","pcxbc"], ["abcd","dbqca"], ["czgxmxrpx","lgh","bj","cheheex","jnzlxgh","nzlgh","ltxdoxc","bju","srxoatl","bbadhiju","cmpx","xi","ntxbzdr","cheheevx","bdju","sra","getqgxi","geqxi","hheex","ltxdc","nzlxgh","pjnzlxgh","e","bbadhju","cmxrpx","gh","pjnzlxghe","oqlt","x","sarxoatl","ee","bbadju","lxdc","geqgxi","oqltu","heex","oql","eex","bbdju","ntxubzdr","sroa","cxmxrpx","cmrpx","ltxdoc","g","cgxmxrpx","nlgh","sroat","sroatl","fcheheevx","gxi","gqxi","heheex"], ]
checks = [ 4, 5, 1, 9, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for words, check in zip(inputs, checks):
        print(f"len(words)=({len(words)}), words=({words})")
        result = f(words)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

