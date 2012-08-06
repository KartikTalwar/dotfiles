:: Deactivate Tunlr DNS
:: Switch to local settings
netsh interface ipv4 set dnsservers name="Local Area Connection" source=dhcp 
ipconfig /flushdns