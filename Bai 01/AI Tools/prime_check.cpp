#include <iostream>
#include <vector>

using namespace std;

bool is_prime(int n) {
    if (n < 2) {
        return false;
    }

    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    vector<int> primes;
    for (int x = 2; x <= n; ++x) {
        if (is_prime(x)) {
            primes.push_back(x);
        }
    }

    cout << "Cac so nguyen to <= " << n << " la: ";
    cout << "[";
    for (size_t i = 0; i < primes.size(); ++i) {
        cout << primes[i];
        if (i + 1 < primes.size()) {
            cout << ", ";
        }
    }
    cout << "]" << endl;

    return 0;
}
