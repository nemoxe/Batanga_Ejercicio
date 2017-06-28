node 'nginx.devops.com' {

	include nginx

}

node 'redis.devops.com' {

	include redis

}

node 'php.devops.com' {

	include php
	include sample-app

}
