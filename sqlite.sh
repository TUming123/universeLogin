wget https://www.sqlite.org/2020/sqlite-autoconf-3310100.tar.gz
tar xvzf sqlite-autoconf-*
cd sqlite-autocon*
./configure --prefix=/usr/local
make
make install