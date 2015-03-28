#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

double fill_tetrahedron(int num)
{
	double volume = sqrt(2) * pow(num, 3) / 12;
	double litres = volume / 1000;
	return litres;
}

int tetrahedron_filled(vector<int> tetrahedrons, int water)
{
	//Sorting the vector containing the length of the edges
	sort(tetrahedrons.begin(), tetrahedrons.end());

	//New vector containing an information about the litres
	vector<double> tetrahedronsLiters;

	//Filling the vector
	for (vector<int>::iterator it = tetrahedrons.begin(); it < tetrahedrons.end(); it++)
	{
		double currentTetrahedronLitres = fill_tetrahedron(*it);
		tetrahedronsLiters.push_back(currentTetrahedronLitres);
	}

	int maxTetrahedronsFilled = 0;
	for (vector<double>::iterator it = tetrahedronsLiters.begin(); it < tetrahedronsLiters.end(); it++)
	{
		if (*it > water)
		{
			return maxTetrahedronsFilled;
		}
		else
		{
			water = water - (int)round(*it);
			maxTetrahedronsFilled++;
		}
	}
	return maxTetrahedronsFilled;
}

int main()
{
	int numberOfTetrahedrons;
	do
	{
		cout << "Please enter number of tetrahedrons you`d like to fill: ";
		cin >> numberOfTetrahedrons;

	} while (numberOfTetrahedrons < 0);

	int litresAvailable;
	do
	{
		cout << "Please enter the litres you have: ";
		cin >> litresAvailable;
	} while (litresAvailable < 0);

	vector<int> edges(numberOfTetrahedrons);
	for (int i = 0; i < edges.size(); i++)
	{
		cout << "Please enter the length of the edge of tetrahedron number ("<< i + 1 << "): ";
		cin >> edges[i];
	}

	int maxFilledTetrahedrons = tetrahedron_filled(edges, litresAvailable);
	cout << "Maximum number of tetrahedrons that can be field with " << litresAvailable << " liters of water: ";
	cout << maxFilledTetrahedrons << endl;

	return 0;
}
