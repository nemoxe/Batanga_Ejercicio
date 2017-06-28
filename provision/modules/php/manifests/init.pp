class php {

#	package {'epel-release':

#		ensure => 'installed',
		
#		}
		
	package { 'php5-fpm':
		
#		require => Package['epel-release'],
		ensure => 'installed',
		
		}

	file { '/etc/php5/fpm/pool.d/www.conf':
	
		ensure => file,
		mode => '0644',
		content => template('php/www.conf.erb'),
		require => Package['php5-fpm'],
		notify => Service['php5-fpm']
		
		}

	service { 'php5-fpm':

		ensure => running,
		enable => true,
		hasrestart => true,
		hasstatus  => true,
		
		}
		

	file { ['/usr/share/nginx/','/usr/share/nginx/www/']:

		ensure => directory,
		mode => '0644',
	     
	     }



	file {'/usr/share/nginx/www/info.php':

		ensure => file,
		mode => '0644',
		source => 'puppet:///modules/php/info.php'

	     }

}
