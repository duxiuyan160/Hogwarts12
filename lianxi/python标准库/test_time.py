import time

def test_time():
    # print(time.asctime())  #国外时间格式
    # print(time.time()) #时间戳
    # print(time.localtime()) #时间戳转换成元组
    # print(time.strftime("%Y-%m-%d", time.localtime())) #针时间戳转换成日期格式

    #获取两天前/三天后的时间
    now_timestam = time.time()
    two_day_before = now_timestam - 60*60*24*2
    three_day_after = now_timestam + 60*60*24*3
    print(time.strftime("%Y年%m月%d日 %H时%M分%秒",time.localtime(two_day_before)))
    print(time.strftime("%Y年%m月%d日 %H时%M分%秒",time.localtime(three_day_after)))
