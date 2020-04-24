wget http://projects.unbit.it/downloads/uwsgi-latest.tar.gz
tar zxvf uwsgi-latest.tar.gz
cd uwsgi*/
python3 uwsgiconfig.py --build
python3 setup.py install
echo ln -s   uwsgi目录  /usr/bin/uwsgi