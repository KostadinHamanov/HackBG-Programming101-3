#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>

using namespace std;

string caesar_encrypt(string str, int n)
{
	//Checking for non-alphabetical characters
	for (unsigned int i = 0; i < str.size(); i++)
	{
		if ((str[i] < 'A' || str[i] > 'Z') && (str[i] < 'a' || str[i] > 'z'))
		{
			exit(1);
		}
	}

	string encryptedString;

	//Start of encrypting
	for (unsigned int i = 0; i < str.size(); i++)
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
		{
			encryptedString.push_back((char)('A' + (str[i] + n - 'A') % 26));
		}
		if (str[i] >= 'a' && str[i] <= 'z')
		{
			encryptedString.push_back((char)('a' + (str[i] + n - 'a') % 26));
		}
	}
	return encryptedString;
}

int main()
{
	string inputStr;
	cout << "Please enter a string you`d like to encrypt: ";
	cin >> inputStr;

	int step;
	do
	{
		cout << "Please enter a step: ";
		cin >> step;

	} while (step < 0);

	string encryptedString = caesar_encrypt(inputStr, step);
	cout << encryptedString << endl;

	return 0;
}

