#Vagrantfile para creacion de cluster sample-app

vms = [

{:hostname => 'nginx.devops.com', :ip => '10.127.0.10', :box => 'ubuntu/trusty64', :ram => 512, :cpus => 2, :port_host => 3000, :port_guest => 80,},
{:hostname => 'php.devops.com', :ip => '10.127.0.20', :box => 'ubuntu/trusty64', :ram => 1024, :cpus => 1,},
{:hostname => 'redis.devops.com', :ip => '10.127.0.30', :box => 'ubuntu/trusty64', :ram => 256, :cpus => 1,},

]

Vagrant.configure("2") do |config|
	vms.each do |create_vm|
		config.vm.define create_vm[:hostname] do |vm_config|
			vm_config.vm.box = create_vm[:box]
			vm_config.vm.hostname = create_vm[:hostname]
			vm_config.vm.network :private_network, ip: create_vm[:ip]
			memory = create_vm[:ram] ? create_vm[:ram] : 256;
			cpu = create_vm[:cpus] ? create_vm[:cpus] : 1;
			vm_config.vm.provider :virtualbox do |cust|
				cust.customize [
					'modifyvm', :id,
					'--name', create_vm[:hostname],
					'--memory', memory.to_s,
					'--cpus', cpu.to_s
						]
			end

			if create_vm[:port_host]
			vm_config.vm.network :forwarded_port, guest: create_vm[:port_guest], host: create_vm[:port_host]
			end
			
			vm_config.vm.provision :shell, :inline => "apt-get update --fix-missing"

			vm_config.vm.provision :puppet do |puppet|
				puppet.manifests_path = 'provision/manifests'
				puppet.module_path = 'provision/modules'
			end
		end
	end
end
