import os
os.system('speedtest-cli')
print()


# pip install speedtest-cli
import speedtest
st = speedtest.Speedtest()

while True:
    # print(st.download())
    print(st.upload())
