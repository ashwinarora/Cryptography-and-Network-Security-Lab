#include<iostream>
#include<string.h>
#include<cmath>
using namespace std;

string encrypt(string text, int key) {
	string cipher = "";
	int l = text.length();
	for(int i = 0; i < l; i++) cipher += ((text[i] + key - 65) % 26 + 65);
	return cipher;
}

string decrypt(string cipher, int key) {
	string text = "";
	int l = cipher.length();
	for(int i = 0; i < l; i++) {
		int difference = (cipher[i] - key - 65) % 26;
		if(difference < 0) difference = 26 + difference;
		text += (difference + 65);
	}
	return text;
}

int main() {
	string text = "", encrypted = "", decrypted = "";
	int key;

	// text = "CRYPTO";
	// key = 5;

	cout << "\nEnter plain-text: ";
	cin >> text;
	cout << "Enter key: ";
	cin >> key;

	encrypted = encrypt(text, key);
	cout << "\nEncrypted text: " << encrypted << "\n";
	decrypted = decrypt(encrypted, key);
	cout << "\nDecrypted text: " << decrypted << "\n\n";
}
