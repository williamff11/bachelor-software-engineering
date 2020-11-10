import psutil
import psutil
import psutil

dic_interfaces = psutil.net_if_addrs()

print(psutil.cpu_percent())

disco = psutil.disk_usage('.')

print("Total:", disco.total, "B")
print("Em uso:", disco.used, "B")
print("Livre:", disco.free, "B")

print("Total:", round(disco.total/(1024*1024*1024), 2), "GB")
print("Em uso:", round(disco.used/(1024*1024*1024), 2), "GB")
print("Livre:", round(disco.free/(1024*1024*1024), 2), "GB")

print("Percentual de Disco Usado:", disco.percent)
