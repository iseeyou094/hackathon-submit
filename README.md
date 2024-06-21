------------
当时比较希望用 0G 构建一个去中心化的代理服务，这样人们可以更方便地使用 web3
主要用到 clash 的一些代码，但还处于半成品阶段。



DAPP trying to build a software with 0G tech.

- Inbound: HTTP, HTTPS, SOCKS5 server, TUN device
- Outbound: Shadowsocks(R), VMess, Trojan, Snell, SOCKS5, HTTP(S), Wireguard
- Rule-based Routing: dynamic scripting, domain, IP addresses, process name and more
- Fake-IP DNS: minimises impact on DNS pollution and improves network performance
- Transparent Proxy: Redirect TCP and TProxy TCP/UDP with automatic route table/rule management
- Proxy Groups: automatic fallback, load balancing or latency testing
- Remote Providers: load remote proxy lists dynamically
- RESTful API: update configuration in-place via a comprehensive API
