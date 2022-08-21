//	{{{3 //	vim: set tabstop=4 modeline modelines=10:
//	vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//	{{{2
#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <string>
#include <iomanip>
#include <sstream>
#include <climits>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <tuple>
#include <set>
#include <algorithm>
#include <numeric>
#include <cstdlib>
using namespace std;
//	Ongoings:
//	{{{
//	Ongoing: 2022-08-21T21:47:55AEST not even(?) (see worklog) [...] (how much work is) 'zip' (as in) 'for (auto& [digits, check] : zip(input_values, input_checks))'(?)
//	Ongoing: 2022-08-21T21:49:25AEST (one the subject of 'zip()' (could one just place the 'const auto& x = v[i]' in (one of the 3 parts of the) for loop <header>?) (and where?))
//	Ongoing: 2022-08-21T22:36:22AEST 'const auto&' or(?) 'auto const&'(?) [...] (not 'auto& const') (refer<ing> to const-pointer-to-const? <plz know>)
//	Ongoing: 2022-08-21T22:44:28AEST utility functions (these have come up before) (hackerrank/effective-c++): print_vector(), get_type<T>(), vector_to_string(), (and then, things needed by/for the problem: split/join? (std?))
//	Ongoing: 2022-08-21T23:05:09AEST (problem) (for our <atoi> function) 1 <= digits.length <= 100 (presumedly '100' is a lie?) (python just-works, what is needed here?)
//	Ongoing: 2022-08-21T23:09:10AEST make it work ((then) make it elegent)
//	Ongoing: 2022-08-21T23:17:01AEST silencing the error in 'get_type_name<T>()' (requires setting C++ version) (do we not have C++17 set for YCM universally?)
//	Ongoing: 2022-08-21T23:24:37AEST making 'join()' work with delim=''(?)
//	Ongoing: 2022-08-22T00:22:03AEST The real hard work is done by 'stol()' (is solution using it valid as per leetcode (with the 100 digits)?) [...] no
//	}}}
//	(hackerrank) ltrim(), rtrim(), split(), join(), printVector(), printMap(), print2DVector()
//	{{{
string ltrim(const string &str) {
//	{{{
    string s(str);
    auto it = std::find_if(s.begin(), s.end(),
                    [](char c) {
                        return !std::isspace<char>(c, std::locale::classic());
                    });
    s.erase(s.begin(), it);
    return s;
}
//	}}}
string rtrim(const string &str) {
//	{{{
    string s(str);
    auto it = std::find_if(s.rbegin(), s.rend(),
                    [](char c) {
                        return !std::isspace<char>(c, std::locale::classic());
                    });
    s.erase(it.base(), s.end());
    return s;
}
//	}}}
vector<string> split(const string &str, const char delim=' ') {
//	{{{
    vector<string> tokens;
    string::size_type start = 0;
    string::size_type end = 0;
    while ((end = str.find(delim, start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));
        start = end + 1;
    }
    tokens.push_back(str.substr(start));
    return tokens;
}
//	}}}
template <typename T>
string join(const vector<T> words, const char delim=' ') {
	//	{{{
	string result = "";
	for (int i = 0; i < words.size(); ++i) {
		result += std::to_string(words[i]);
		if (i != words.size()-1) { result += delim; }
	}
	return result;
}
	//	}}}
string join(const vector<string> words, const char delim=' ') {
	//	{{{
	string result = "";
	for (int i = 0; i < words.size(); ++i) {
		result += words[i];
		if (i != words.size()-1) { result += delim; }
	}
	return result;
}
	//	}}}
string join(const vector<char> words, const char delim=' ') {
	//	{{{
	string result = "";
	for (int i = 0; i < words.size(); ++i) {
		result += words[i];
		if (i != words.size()-1) { result += delim; }
	}
	return result;
}
	//	}}}
template <typename T>
void printVector(string varname, const vector<T> words, const char delim=' ') {
	//	{{{
	string vector_str = join(words, delim);
	cerr << varname << "=(" << vector_str << ")\n";
}
	//	}}}
template <typename T>
void print2DVector(string varname, const vector<vector<T>> words, const char delim=' ') {
	//	{{{
	string result = "(";
	for (int i = 0; i < words.size(); ++i) {
		result += "(";
		string loop_result = join(words[i], ',');
		result += loop_result;
		result += ")";
		if (i != words.size()-1) {
			result += ", ";
		}
	}
	result += ")\n";
	cerr << varname << "=" << result;
}
	//	}}}
template <typename A, typename B>
void printMap(string varname, const map<A,B> m, const char delim=' ') {
	//	{{{
	string m_str = "";
	for (auto const &x: m) {
		m_str += std::to_string(x.first);
		m_str += ":";
		m_str += std::to_string(x.second);
		m_str += delim;
	}
	m_str.pop_back();
	cerr << varname << "=(" << m_str << ")\n";
}
	//	}}}
//	}}}
//	(effective-c++) get_type_name<T>(), is_lvalue()
//	{{{
//	LINK: https://stackoverflow.com/questions/281818/unmangling-the-result-of-stdtype-infoname
#include <string_view>
template <typename T>
constexpr auto get_type_name() -> std::string_view {
#if defined(__clang__)
    constexpr auto prefix = std::string_view{"[T = "};
    constexpr auto suffix = "]";
    constexpr auto function = std::string_view{__PRETTY_FUNCTION__};
#elif defined(__GNUC__)
    constexpr auto prefix = std::string_view{"with T = "};
    constexpr auto suffix = "; ";
    constexpr auto function = std::string_view{__PRETTY_FUNCTION__};
#elif defined(__MSC_VER)
    constexpr auto prefix = std::string_view{"get_type_name<"};
    constexpr auto suffix = ">(void)";
    constexpr auto function = std::string_view{__FUNCSIG__};
#else
# error Unsupported compiler
#endif
    const auto start = function.find(prefix) + prefix.size();
    const auto end = function.find(suffix);
    const auto size = end - start;
    return function.substr(start, size);
}
template<typename T>
constexpr bool is_lvalue(T&& x) {
	return std::is_lvalue_reference<T>{};
}
//	}}}
//	python solution:
//	{{{
//class Solution:
//
//    #   runtime: beats 98%
//    def plusOne_naive(self, digits: List[int]) -> List[int]:
//        digits = [ str(x) for x in digits ]
//        digits = int(''.join(digits)) 
//        result = [ int(x) for x in str(digits+1) ]
//        return result
//
//s = Solution()
//test_functions = [ s.plusOne_naive, ]
//input_values = [ [1,2,3], [4,3,2,1], [9], ]
//input_checks = [ [1,2,4], [4,3,2,2], [1,0], ]
//assert len(input_values) == len(input_checks)
//for f in test_functions:
//    for digits, check in zip(input_values, input_checks):
//        print("digits=(%s)" % digits)
//        result = f(digits)
//        print("result=(%s)" % result)
//        assert check == result, "Check failed"
//    print()
//	}}}

//	Continue: 2022-08-21T23:47:31AEST implement 'string2digits()'
//	Continue: 2022-08-22T00:29:37AEST create valid solution (valid as per leetcode submission) (stol solution fails, throws out_of_range -> can't hold excessively 

vector<char> string2digits(const string& s) {
	return {};
}

class Solution {
public:
	vector<int> plusOne_naive(vector<int>& digits) 
	{
		//	convert vector<int> to vector<char>
		vector<char> digits_char;
		for (const auto& d: digits) {
			char d_char = d + '0';
			digits_char.push_back(d_char);
		}
		//printVector("digits_char", digits_char);

		//	convert vector<char> to string
		string digits_str = this->join(digits_char);
		//cerr << "digits_str=(" << digits_str << ")\n";

		//	convert string to int
		long digits_long = stol(digits_str);
		//cerr << "digits_long=(" << digits_long << ")\n";

		//	add 1
		long result_long = digits_long + 1;
		//cerr << "result_long=(" << result_long << ")\n";

		//	convert int to string <(or int -> vector<int> directly)>
		string result_str = std::to_string(result_long);
		//cerr << "result_str=(" << result_str << ")\n";

		//	convert string to vector<int>
		vector<int> result = this->split(result_str);
		return result;
	}

	vector<int> split(const string &str) {
		vector<int> result;
		for (const char& c: str) {
			int d = c - '0';
			result.push_back(d);
		}
		return result;
	}

	string join(const vector<char> words) {
		string result = "";
		for (int i = 0; i < words.size(); ++i) {
			result += words[i];
		}
		return result;
	}

};


vector<vector<int>> input_values = { {1,2,3}, {4,3,2,1}, {9}, };
//	failing input value: [7,2,8,5,0,9,1,2,9,5,3,6,6,7,3,2,8,4,3,7,9,5,7,7,4,7,4,9,4,7,0,1,1,1,7,4,0,0,6]
vector<vector<int>> input_checks = { {1,2,4}, {4,3,2,2}, {1,0}, };

int main() 
{
	assert (input_values.size() == input_checks.size());
	Solution s;

	for (int i = 0; i < input_values.size(); ++i) {
		vector<int>& digits = input_values[i];
		vector<int>& check = input_checks[i];
		printVector("digits", digits);
		vector<int> result = s.plusOne_naive(digits);
		printVector("result", result);
		assert (check == result);
	}
	cerr << "\n";

	return 0;
}

