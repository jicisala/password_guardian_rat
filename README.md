# 加密鼠
版本：0.5
作者：Upgrade（570492547@qq.com）

注意：使用前需要先安装requests.txt下的加密模块

## 软件描述：
该软件提供密码管理的一条龙服务，主要用于密码的生成以及密码的加密保存，加密方式为MD5结合AES，将你准备的加密密码的MD5运算作为AES加密的密钥，对其它密码进行加密，从而实现通过一个密码管理你的其他所有密码的目标（前提是不要泄露这个加密密码）。

## 软件特点：
1，该软件对加密后生成的加密文本以及其它信息以一个可以自定义的可读文件进行存储，这样做有诸多好处，一是方便迁移与备份，仅仅只需要备份加密文本，即可保证密码永不丢失，并且可以很方便的进行多点备份，二是支持多用户使用，只要对方不知道你的加密密码，那么即使你知道了对方的密码加密文本，也无法解开。

密码的生成：本程序自带密码生成，可以生成任意长度的随机密码，并可对包含的数字，字母，符号等进行自定义。

密码的保存：需要保存的密码可以使用生成的随机密码，也可以使用自己准备的密码，然后按照要求写入描述以及加秘密密码，加密密码很重要，要是忘了，保存的密码将无法解密。

密码的获取：将会把目前所有的密码以及其描述列举出来，可以通过id进行选择，然后输入加密密码进行解密。

# password_guardian_rat
Author: Upgrade(570492547@qq.com)
Version: 0.5

Note: requires.txt needs to be installed before use this software.

## Software description：

The software provides a one-stop service of password management, which is mainly used for password generation and password encryption. 

The encryption method is MD5 combined with AES. The MD5 operation of your prepared encryption password is used as the AES encryption key to encrypt other passwords, so as to achieve the goal of managing all your other passwords through one password (on the premise that you do not disclose this encryption password)

## Software features：

The software can store the encrypted text and other information in a user-defined readable file, which has many advantages. First, it is convenient for migration and backup. Just need to backup the encrypted text, it can ensure that the password will never be lost, and it is convenient for multi-point backup. Second, it supports multi-user use, as long as the other party does not know your encryption Password, so even if you know the other party's password encrypted text, also can't unlock.

## Software functions:

Password generation: This program comes with password generation, can generate random password of any length, and can customize the numbers, letters, symbols, etc

Password saving: the password to be saved can use the generated random password or the password prepared by yourself, and then write the description and encrypt the secret password according to the requirements. It is very important to encrypt the password. If you forget, the saved password will not be decrypted

Password acquisition: all current passwords and their descriptions will be listed, which can be selected by ID, and then input the encrypted password to decrypt