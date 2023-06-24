//	{{{3
//	vim: set tabstop=4 modeline modelines=10:
//	vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
//	{{{2
#include <iostream>
#include <vector>
#include <tuple>
#include <string>
#include <vector>
#include <assert.h>
#include <limits.h>
using namespace std;
//	Continue: 2022-09-05T22:58:26AEST main(), time each outer loop
//	Continue: 2022-09-05T23:14:08AEST remaining solutions, (AddPower2, BinaryLongDivision) (and whether Bitshift version of former is different enough to justify being a seperate example)

//	Implement integer division without using the '*', '/', or '%' operators, and >32-bit types, avoiding overflow.
//	Constraints: (dividend,divisor) = [-2**31, 2**31-1], divisor != 0

//	Substitute operations:
//		a * -1			-a
//		a / 2**n		a >> n
//		a * 2**n		a << n
//		a += a			a *= 2 			a <<= 1

//	Overflow is platform specific behaviour -> any solution in which overflow occurs is not portable.

//	Note: 'abs(INT_MIN) > INT_MAX'
//	There are more negative integers than positive integers. 

int f_ref(int dividend, int divisor) {
	return dividend / divisor;
}

//	Ongoing: 2022-09-05T22:32:51AEST can't handle {INT_MIN,INT_MIN} case -> that was the 'dividend - divisor <= 0' line (the solution is 'divisor >= dividend')
int f_iterative(int dividend, int divisor) {
	//	Overflow case:
	if (dividend == INT_MAX && divisor == -1) {
		return INT_MAX;
	}
	//	Converting inputs to negative allows coverage of the largest possible range of numbers (to avoid overflow).
	//	We store the number of inputs that were previously negative to allow us to determine correct sign of result.
	int count_negatives = 2;
	if (dividend > 0) {
		--count_negatives;
		dividend = -dividend;
	}
	if (divisor > 0) {
		--count_negatives;
		divisor = -divisor;
	}

	//	How many times can we fit 'divisor' into 'dividend'
	int result = 0;
	while (divisor >= dividend) { 	// (dividend - divisor <= 0) 
		dividend -= divisor;
		--result;
	}

	//	Return result with correct sign
	if (count_negatives != 1) {
		return -result;
	}
	return result;
}


//	Can't handle negative divisor
int f_simple_iterativePower2(int dividend, int divisor) {
	int result = 0;
	while (dividend >= divisor) {
		int powerOf2 = 1;
		int temp = divisor;
		while (temp + temp < dividend) {
			temp <<= 1;
			powerOf2 <<= 1;
		}
		result += powerOf2;
		dividend -= temp;
	}
	return result;
}


int f_iterativePower2(int dividend, int divisor) {
	//	Overflow case:
	if (dividend == INT_MAX && divisor == -1) {
		return INT_MAX;
	}
	//	Converting inputs to negative allows coverage of the largest possible range of numbers (to avoid overflow).
	//	We store the number of inputs that were previously negative to allow us to determine correct sign of result.
	int count_negatives = 2;
	if (dividend > 0) {
		--count_negatives;
		dividend = -dividend;
	}
	if (divisor > 0) {
		--count_negatives;
		divisor = -divisor;
	}

	//	How many times can we fit 'divisor' into 'dividend'
	//	sum(n) for each 'temp = divisor * 2**n' we can fit into 'dividend'
	int result = 0;
	while (dividend <= divisor) {		//	(divisor >= dividend), (dividend - divisor <= 0) 
		int powerOf2 = -1;
		int temp = divisor;
		while (temp + temp >= dividend && temp >= INT_MIN/2) {
			temp <<= 1;					//	temp += temp
			powerOf2 <<= 1;				//	powerOf2 += powerOf2
		}
		result += powerOf2;
		dividend -= temp;
	}

	//	Return result with correct sign
	if (count_negatives != 1) {
		return -result;
	}
	return result;
}


//	Can't handle negative divisor
int f_simple_iterativeAddPower2s(int dividend, int divisor) {
	vector<int> doubles;
	vector<int> powersOfTwo;
	int powerOfTwo = 1;
	while (divisor <= dividend) {
		powersOfTwo.push_back(powerOfTwo);
		doubles.push_back(divisor);
		powerOfTwo += powerOfTwo;
		divisor += divisor;
	}
	int result = 0;
	for (int i = doubles.size()-1; i >= 0; --i) {
		if (doubles[i] <= dividend) {
			result += powersOfTwo[i];
			dividend -= doubles[i];
		}
	}
	return result;
}


int f_iterativeAddPower2s(int dividend, int divisor) {
	if (dividend == INT_MIN && divisor == -1) {
		return INT_MAX;
	}
	//	Converting inputs to negative allows coverage of the largest possible range of numbers (to avoid overflow).
	//	We store the number of inputs that were previously negative to allow us to determine correct sign of result.
	int count_negatives = 2;
	if (dividend > 0) {
		--count_negatives;
		dividend = -dividend;
	}
	if (divisor > 0) {
		--count_negatives;
		divisor = -divisor;
	}

	vector<int> doubles;
	vector<int> powersOfTwo;
	int powerOfTwo = -1;
	while (divisor >= dividend) {
		doubles.push_back(divisor);
		powersOfTwo.push_back(powerOfTwo);
		if (divisor < INT_MIN/2) {
			break;
		}
		divisor <<= 1;			//	divisor += divisor
		powerOfTwo <<= 1;		//	powerOfTwo += powerOfTwo
	}
	int result = 0;
	for (int i = doubles.size()-1; i >= 0; --i) {
		if (doubles[i] >= dividend) {
			result += powersOfTwo[i];
			dividend -= doubles[i];
		}
	}

	//	Return result with correct sign
	if (count_negatives != 1) {
		return -result;
	}
	return result;

}


int f_iterativeAddPower2sBitshift(int dividend, int divisor) {
	return 0;
}


int f_BinaryLongDivision(int dividend, int divisor) {
	return 0;
}


vector<function<int(int,int)>> test_functions = { f_ref, f_iterative, f_iterativePower2, f_iterativeAddPower2s, };
vector<string> test_functions_names = { "f_ref", "f_iterative", "f_iterativePower2", "f_iterativeAddPower2s", };

vector<tuple<int,int>> input_values = { {10,3}, {7,-3}, {INT_MAX,INT_MAX}, {INT_MIN,INT_MIN}, };
vector<int> input_checks = { 3, -2, 1, 1, };

int main()
{
	assert(sizeof(int) == 4);
	assert(INT_MAX == 2147483647);
	assert(INT_MIN == -2147483648);
	assert(input_values.size() == input_checks.size());
	assert(test_functions.size() == test_functions_names.size());

	for (int i = 0; i < test_functions.size(); ++i) {
		auto f = test_functions[i];
		auto f_name = test_functions_names[i];
		cout << f_name << ":\n";
		for (int j = 0; j < input_values.size(); ++j) {
			int dividend = get<0>(input_values[j]);
			int divisor = get<1>(input_values[j]); 
			cout << "dividend=(" << dividend << "), divisor=(" << divisor << ")\n";
			int check = input_checks[j];
			int result = f(dividend, divisor);
			cout << "result=(" << result << ")\n";
			assert(result == check && "Check comparison failed");
		}
		cout << "\n";
	}

	return 0;
}

