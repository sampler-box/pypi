bump:
	git pull origin master
	python bump.py $(app) $(version) https
	make commit

commit:
	git add -p
	git commit -m "$(shell cat commit_message.txt)"
	git push origin master

make install:
	pip install -r requirements.txt
