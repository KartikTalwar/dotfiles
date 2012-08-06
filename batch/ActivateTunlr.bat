:: Activate Tunlr DNS
:: Browse sites in 'Murica
netsh interface ipv4 add dnsservers name="Local Area Connection" 149.154.158.186
netsh interface ipv4 add dnsservers name="Local Area Connection" 199.167.30.144 index=2
netsh interface ipv4 add dnsservers name="Wireless Network Connection" 149.154.158.186
netsh interface ipv4 add dnsservers name="Wireless Network Connection" 199.167.30.144 index=2
ipconfig /flushdns