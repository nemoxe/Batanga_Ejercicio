class nginx {

#	package {'epel-release':
		
#		ensure => instaled,

#		}


	package { 'nginx':
		
#		require => Package['epel-release'],		
		ensure => 'installed',
 
		}

	file { '/etc/nginx/sites-available/default':

		ensure => file,
		mode => '0644',
		content => template('nginx/default.erb'),
		require => Package['nginx'],
		notify => Service['nginx'],

		}

	service { 'nginx':

		ensure => running,
		enable => true,
		hasrestart => true,
		hasstatus  => true,

		}
	}
