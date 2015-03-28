#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double fill_tetrahedron(int num)
{
	double volume = sqrt(2) * pow(num, 3) / 12;
	double litres = volume / 1000;
	return litres;
}

int main()
{
	int length;
	do
	{
		cout << "Please insert the edge length of a Regular tetrahedron in centimeters" << endl;
		cout << "Length: ";
		cin >> length;

	} while (length < 0);

	double litres = fill_tetrahedron(length);
	cout << setiosflags(ios::fixed) << setprecision(2) << litres << endl;
	return 0;
}

