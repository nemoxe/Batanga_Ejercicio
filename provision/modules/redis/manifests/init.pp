class redis {

#	package {'epel-release':

#		ensure => 'installed',

#		}


	package { 'redis-server':
	
#		require => Package['epel-release'],
		ensure => 'installed',
		
		}
		
	file { '/etc/redis/redis.conf':

		ensure => file,
		mode => '0644',
		content => template('redis/redis.conf.erb'),
		notify => Service['redis-server'],
	
		}
	
	service { 'redis-server':

		ensure => running,
		enable => true,
		hasrestart => true,
		hasstatus  => true,

		}
	}
