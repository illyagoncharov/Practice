git init створити новий репозитор≥й
git status показуЇ статус репозитор≥ю, стан файл≥в
touch _filename.py_ - створити файл
git add  _filename.py_ - додати файл до в≥дстеженн€
git add *.py - додати файл до в≥дстеженн€ вс≥ фали .py
git add _foldername_/* - додаЇмо вс≥ фали папки _foldername_

git rm filename     ¬идаленн€ файлу з ≥ндексу

git branch без вказ≥вки ≥мен≥ виведе вс≥ локальн≥ г≥лки, а прапор Цr покаже г≥лки у в≥ддаленому репозитор≥њ.

git commit - m "comment" - зберегти файл
git log - подивитись лог
git config --global user.email "ilya.lb1@gmail.com" - створити емайл автора
git config --global user.name "ilya_goncharov" - створити ≥м'€ автора

ssh-keygen - стоврити публ≥чний ключ
$ cat ~/.ssh/id_rsa.pub - подивитись публ≥чний ключ
$ cat ~/.ssh/id_rsa подивитись приватний ключ
git branch -M main - зм≥нити майстер на мейн

$ git remote add origin git@github.com:GoncharovIS/test_repository.git - п≥дключити в≥ддалений репозитор≥й

$ git remote -v - ≥нформац≥€ стосовно п≥дключенн€

git remote remove origin - видалити п≥дключенн€

git pull - ст€гнути зм≥ни з сервера €ких немаЇ

git push - штовхнути на сервер зм≥ни 

git push origin master - заллЇ 1 раз

git push --set-upstream origin master або git push -u origin master - буде заливати пост≥йно з цього адресу

$ git clone git@github.com:GoncharovIS/UPython.git ./lessons/ - клонуЇмо репозитор≥й в папку лессонс

cd .. - перейти в корень


ћаючи два практично ≥дентичн≥ файли, можна за допомогою команди diff з ключами -uN зрозум≥ти, €ка м≥ж ними р≥зниц€:

diff -uN test.txt test1.txt:

git add *
git add .
git add --o
git commit -a