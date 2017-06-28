class sample-app {


	package { 'php5-redis':
		
		ensure => installed,
		notify => Service['php5-fpm'],
		
		}

	file { '/usr/share/nginx/www/index.php':
		
		ensure => file,
		mode => '0644',
		source => 'puppet:///modules/sample-app/index.php'
		
		}

	file { '/usr/share/nginx/www/settings.php':
	
		ensure => file,
		mode => '0644',
		source => 'puppet:///modules/sample-app/settings.php'

		}

	}
