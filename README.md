# password_guardian_rat
It`s a password manage tool.

Version: 0.3

Note: requires.txt needs to be installed before use this software.

## Software description：

The software is mainly used for the generation of password and the encryption of password.
The encryption method uses MD5 to encrypt AES. First, encrypt the encryption password you prepared with MD5 to obtain a string that can be used as AES public key, and then encrypt and decrypt the password with this string

## Software features：

The software does not use the database to store the encrypted password text, but uses a readable file for storage, which has many advantages. First, it is convenient for migration, just need to package the program, you can take it away, and it is convenient for multi-point backup. Second, it supports multi-user use. As long as the other party does not know your encryption password, then even if you know The other people's password which encrypts the text and cannot be untied

## Software functions:

Password generation: This program comes with password generation, can generate random password of any length, and can customize the numbers, letters, symbols, etc

Password saving: the password to be saved can use the generated random password or the password prepared by yourself, and then write the description and encrypt the secret password according to the requirements. It is very important to encrypt the password. If you forget, the saved password will not be decrypted

Password acquisition: all current passwords and their descriptions will be listed, which can be selected by ID, and then input the encrypted password to decrypt