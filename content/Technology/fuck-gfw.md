Title: 翻墙
Date: 2014-6-24
Category: Technology
Tags: Technology, SSHTunnel, Squid, Proxy, Linux
Slug: fuck-gfw
Author: Chifeng
Summary: 第一篇技术文章就介绍这个，实在是很无奈，但是不学会翻墙实在是太多事情不能做。本文主要介绍一个简单的翻墙方式SSHTunnel+Proxy

我曾经试过多种方式，早些年L2TP/PPTP/OpenVPN、甚至于普通的Squid Proxy都还能用，不幸的是现在都被封了。目前来看，如果你不加一层SSL的话，基本上是不可能翻出去了。
我自己正在使用的一种简单的翻墙方式，如下

##### 要求：

   * 有一台在海外的云主机，比如：Linode、DigitalOcean
   * 了解一点Linux技术，SSH Tunnel、Squid和Firefox浏览器的代理设置

----------------------------------------------------
<p>
然后分以下3步走，来完成翻墙工作

第一步，在你的VM上，设置一个Squid代理服务器
</p>

<pre><code>
apt-get -y install squid
</code></pre>

###### 编辑/etc/squid3/squild.conf，内容如下
<pre>
<code>
acl SSL_ports port 443
acl Safe_ports port 80		# http
acl Safe_ports port 21		# ftp
acl Safe_ports port 443		# https
acl Safe_ports port 70		# gopher
acl Safe_ports port 210		# wais
acl Safe_ports port 1025-65535	# unregistered ports
acl Safe_ports port 280		# http-mgmt
acl Safe_ports port 488		# gss-http
acl Safe_ports port 591		# filemaker
acl Safe_ports port 777		# multiling http
acl CONNECT method CONNECT
http_access deny !Safe_ports
http_access deny CONNECT !SSL_ports
http_access allow localhost manager
http_access deny manager
http_access allow localhost
http_access deny all
http_port 3128
coredump_dir /var/spool/squid3
refresh_pattern ^ftp:		1440	20%	10080
refresh_pattern ^gopher:	1440	0%	1440
refresh_pattern -i (/cgi-bin/|\?) 0	0%	0
refresh_pattern (Release|Packages(.gz)*)$      0       20%     2880
refresh_pattern .		0	20%	4320
</code>
</pre>

<pre><code>
#service squid3 restart
</code></pre>


##### 第二步，然后在本机创建一个脚本~/ssh_tunnel.sh，如下内容
<pre><code>
\#!/bin/sh
ssh -NfL 3128:127.0.0.1:3128 chifeng@hostname.domain.com
\#修改hostname.domain.com为你自己的域名，另外登陆这儿走public key认证
</code></pre>

执行一下这个脚本，SSH Tunnel就建立起来了
<pre><code>
sh ~/ssh_tunnel.sh
</code></pre>

##### 第三步，设置Firefox的代理为localhost:3128即可


这样访问国内网站，使用Chrome/Safari，访问海外网站使用Firefox即可。根据SSH协议本身的安全性，目测这种翻墙方式很难被封掉，除非不容许SSH协议通过


当然还有一种更简单的方式，直接花钱购买相关的SSL VPN服务，比如： EUREKAVPT https://eurekavpt.com 一年300元的价格，物超所值!


BTW, 看到老黄已经在研究Proxy直接变为TCP的路由了，高端！！如果搞定，那就太方便了！

