# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => template('my_module/wp-settings.php.erb'),
}

exec { 'fix-wordpress':
  command     => '/usr/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path        => ['/usr/bin', '/bin'],
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}

