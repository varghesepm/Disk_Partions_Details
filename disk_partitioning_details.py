try:
    import pysftp
except:
    print()
    print("pytsftp , module Not Found")
    print("Install: pip3 install pysftp")
sys.exit(1)

dps = psutil.disk_partitions()

fmt_str = "{:<8} {:<7} {:<7}"
print(fmt_str.format("Drive", "Type", "Opts"))

for dp in dps:
    print(fmt_str.format(dp.device, dp.fstype, dp.opts))
