git init �������� ����� ����������
git status ������ ������ ����������, ���� �����
touch _filename.py_ - �������� ����
git add  _filename.py_ - ������ ���� �� ����������
git add *.py - ������ ���� �� ���������� �� ���� .py
git add _foldername_/* - ������ �� ���� ����� _foldername_

git rm filename     ��������� ����� � �������

git branch ��� ������� ���� ������ �� ������� ����, � ������ �r ������ ���� � ���������� ���������.

git commit - m "comment" - �������� ����
git log - ���������� ���
git config --global user.email "ilya.lb1@gmail.com" - �������� ����� ������
git config --global user.name "ilya_goncharov" - �������� ��'� ������

ssh-keygen - �������� �������� ����
$ cat ~/.ssh/id_rsa.pub - ���������� �������� ����
$ cat ~/.ssh/id_rsa ���������� ��������� ����
git branch -M main - ������ ������� �� ����

$ git remote add origin git@github.com:GoncharovIS/test_repository.git - ��������� ��������� ����������

$ git remote -v - ���������� �������� ����������

git remote remove origin - �������� ����������

git pull - �������� ���� � ������� ���� ����

git push - ��������� �� ������ ���� 

git push origin master - ���� 1 ���

git push --set-upstream origin master ��� git push -u origin master - ���� �������� ������� � ����� ������

$ git clone git@github.com:GoncharovIS/UPython.git ./lessons/ - ������� ���������� � ����� �������

cd .. - ������� � ������


����� ��� ��������� �������� �����, ����� �� ��������� ������� diff � ������� -uN ��������, ��� �� ���� ������:

diff -uN test.txt test1.txt:

git add *
git add .
git add --o
git commit -a