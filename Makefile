gitbig:
	find . -size +10M
	echo du -a ./ | sort -n -r | head -n 20
	for file in `find . -size +10M`; do ls -lh $$file; done


token: 
	./token.sh



publish: token
	git config --global user.email tonybutzer@gmail.com
	git config --global user.name tonybutzer
	git config --global push.default simple
	git add .
	git commit -m "automatic git update from Makefile"
	git push

jup:
	docker run -it -p 80:8888 -v `pwd`:/home/jovyan/ tbutzer/jupyter-rise jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml'

