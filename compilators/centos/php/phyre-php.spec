Name:           turbo-php
Version:        8.2
Release:        1%{?dist}
Summary:       Turbo PHP - Web server for TurboPanel

License:       GPL
URL:    https://turbopanel.com
Source0: http://de2.php.net/distributions/php-8.2.0.tar.gz

%description
Turbo PHP for executing turbo panel

%prep
# we have no source, so nothing here

%build
wget http://de2.php.net/distributions/php-8.2.0.tar.gz -O $RPM_SOURCE_DIR/php-8.2.0.tar.gz
tar -xzf $RPM_SOURCE_DIR/php-8.2.0.tar.gz -C $RPM_BUILD_DIR
cd php-8.2.0
./buildconf --force
./configure --prefix=/usr/local/turbo/php \
				--with-libdir=lib/$(arch)-linux-gnu \
				--enable-fpm --with-fpm-user=turboweb --with-fpm-group=turboweb \
				--with-openssl \
				--with-mysqli \
                --with-pdo-mysql=mysqlnd \
                --with-mysqli=mysqlnd \
                --with-pdo-sqlite \
                --with-pdo-pgsql \
				--with-gettext \
				--with-curl \
				--enable-intl \
				--with-zip \
				--with-zlib \
				--with-gmp \
				--with-sodium \
				--with-freetype \
			  	--enable-sockets \
				--enable-mbstring \
				--with-libdir=lib/$(arch)-linux-gnu
make -j 4
make install

/usr/local/turbo/php/bin/php -v
%make_install

wget https://raw.githubusercontent.com/TurboPanelDemo/TurboPanelPHP/main/compilators/debian/php/php-fpm.conf -O $RPM_BUILD_ROOT/usr/local/turbo/php/conf/php-fpm.conf

%files
/usr/local/turbo/php

%changelog
* Tue May 05 2024 Turbo PHP Packaging <turbo-nginx-packaging@turbopanel.com> - 8.2
- Initial release of Turbo PHP 8.2
