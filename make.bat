pyinstaller --onefile --distpath ./dist 13ColoniesAdif.py

copy README.txt dist\README.txt
cd dist

python ..\makeZip.py

cd ..

