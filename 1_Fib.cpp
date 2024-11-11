#include <iostream>
using namespace std;

int fibonacciIterative(int n) {
    if (n <= 1)
        return n;

    int a = 0, b = 1, fib;
    for (int i = 2; i <= n; i++) {
        fib = a + b;
        a = b;
        b = fib;
    }
    return b;
}

int fibonacciRecursive(int n) {
    if (n <= 1)
        return n;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

int main() {
    int n;
    cout << "Enter the number of terms: ";
    cin >> n;

    cout<<"fibonacci_recursive :";
    for(int i=0;i<n;++i){
        cout<<fibonacciRecursive(i)<< " "; 
    }
    cout<<endl;
    cout<<"fibonacci_iterative :";
    for(int i=0;i<n;++i){
        cout<<fibonacciIterative(i)<< " ";   
    }
    return 0;
}