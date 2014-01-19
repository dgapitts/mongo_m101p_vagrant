# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|

  config.vm.define "m101p" do |m101p|
    m101p.vm.box = "precise32"
    #m101p.vm.boot_mode = :gui
    m101p.vm.box_url = "http://files.vagrantup.com/precise64.box"
    m101p.vm.forward_port 5656, 5656
    m101p.vm.host_name = "m101p"
    m101p.vm.provision :shell, :path => "provision.sh"
  end

end
