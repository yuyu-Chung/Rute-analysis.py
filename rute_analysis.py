# 本程式檔針對 已下載之路線收運資料，進行Pandas 應用整理 

import pandas as pd
import numpy as np

# 第一步驟讀取檔案，直接應用pandas "read_excel" 物件，但電腦須先行下載第三方套件:xlrd，無須import。下載方式: pip install xlrd
# xlrd latest version is 2.01， only support xls。
# if the file is not xls, it is xlsx，the solutions have two:
# 1.step1: install openpyxl (pip install openpyxl) step2: change coding->("檔案路徑",encoding="big5"(若檔案中有中文字，建議增加此一設定),engine="openpyxl")
# 2.install older version of xlrd: pip install xlrd ==1.2.0

#data_test = pd.read_excel("C:/Users/莊馥羽/Desktop/程式練習/202107組程式學習團/data-explore/2021_rute_data/lagi2-003 (1).xlsx",encoding="big5",engine="openpyxl")
#print(data_test)

def rawdata():
    data_8 = pd.read_excel(r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data\lagi2-003.xls", encoding="big5")
    data_7 = pd.read_excel(r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data\lagi2-003 (1).xls", encoding="big5")
    data_6 = pd.read_excel(r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data\lagi2-003 (2).xls", encoding="big5")
    data_5 = pd.read_excel(r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data\lagi2-003 (3).xls", encoding="big5")
    data_4 = pd.read_excel(r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data\lagi2-003 (4).xls", encoding="big5")
    data_3 = pd.read_excel(r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data\lagi2-003 (5).xls", encoding="big5")
    data_2 = pd.read_excel(r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data\lagi2-003 (6).xls", encoding="big5")
    data_1 = pd.read_excel(r"C:\Users\莊馥羽\Desktop\程式練習\202107組程式學習團\data-explore\2021_rute_data\lagi2-003 (7).xls", encoding="big5")

    # 母體資料讀取完畢後，因所有資料 columns 皆相同，故應用concat(垂直增加row)合併所有資料
    data =pd.concat([data_8,data_7,data_6,data_5,data_4,data_3,data_2,data_1],join="outer")
    # 用column[順序]，設定成索引，因順序欄位為車輛gps訊號發射定點，定點編號之數量排序。
    data_r1 = data.set_index(data["順序"])
    # 先針對垃圾車資料做分析，故將資收車相關資料全部先刪除
    data_r2 = data_r1.drop(labels = ["資收車車號","資收車到達時間","延遲時間(分)","預估到達時間"],axis=1)

    return data_r2


# 依上述整理過後的資料，輸入不同路線，以取得特定路線資料做分析，並將取得的資料再行整理，成為具使用價值之新DataFrame
def rute(data_r2,rute_name):
    # 限定特定路線資料
    data_1 = data_r2[data_r2["路線名稱"]==rute_name]

    # 將本年度周一、四的日期篩選出來，針對周一、四收運狀況做分析 (&:交集;|:聯集)
    # 依網路教學，先做一個遮罩(data_2)，再把遮罩套入母體，即會篩選出條件資料。
    data_2 = (data_1["日期"]=="2021-08-16")|(data_1["日期"]=="2021-08-12")|(data_1["日期"]=="2021-08-09")|(data_1["日期"]=="2021-08-05")|(data_1["日期"]=="2021-08-02")|(data_1["日期"]=="2021-07-29")|(data_1["日期"]=="2021-07-26")|(data_1["日期"]=="2021-07-22")|(data_1["日期"]=="2021-07-19")|(data_1["日期"]=="2021-07-15")|(data_1["日期"]=="2021-07-12")|(data_1["日期"]=="2021-07-08")|(data_1["日期"]=="2021-07-05")|(data_1["日期"]=="2021-07-01")|(data_1["日期"]=="2021-06-28")|(data_1["日期"]=="2021-06-24")|(data_1["日期"]=="2021-06-21")|(data_1["日期"]=="2021-06-17")|(data_1["日期"]=="2021-06-14")|(data_1["日期"]=="2021-06-10")|(data_1["日期"]=="2021-06-07")|(data_1["日期"]=="2021-06-03")|(data_1["日期"]=="2021-05-31")|(data_1["日期"]=="2021-05-27")|(data_1["日期"]=="2021-05-24")|(data_1["日期"]=="2021-05-20")|(data_1["日期"]=="2021-05-17")|(data_1["日期"]=="2021-05-13")|(data_1["日期"]=="2021-05-10")|(data_1["日期"]=="2021-05-06")|(data_1["日期"]=="2021-05-03")|(data_1["日期"]=="2021-04-29")|(data_1["日期"]=="2021-04-26")|(data_1["日期"]=="2021-04-22")|(data_1["日期"]=="2021-04-19")|(data_1["日期"]=="2021-04-15")|(data_1["日期"]=="2021-04-12")|(data_1["日期"]=="2021-04-08")|(data_1["日期"]=="2021-04-05")|(data_1["日期"]=="2021-04-01")|(data_1["日期"]=="2021-03-29")|(data_1["日期"]=="2021-03-25")|(data_1["日期"]=="2021-03-22")|(data_1["日期"]=="2021-03-18")|(data_1["日期"]=="2021-03-15")|(data_1["日期"]=="2021-03-11")|(data_1["日期"]=="2021-03-08")|(data_1["日期"]=="2021-03-04")|(data_1["日期"]=="2021-03-01")|(data_1["日期"]=="2021-02-25")|(data_1["日期"]=="2021-02-22")|(data_1["日期"]=="2021-02-18")|(data_1["日期"]=="2021-02-04")|(data_1["日期"]=="2021-02-01")|(data_1["日期"]=="2021-01-28")|(data_1["日期"]=="2021-01-25")|(data_1["日期"]=="2021-01-21")|(data_1["日期"]=="2021-01-18")|(data_1["日期"]=="2021-01-14")|(data_1["日期"]=="2021-01-11")|(data_1["日期"]=="2021-01-07")|(data_1["日期"]=="2021-01-04")
     #                         1                         2                                3                             4                              5                              6                             7                              8                             9                              10                            11                             12                             13                            14                            15                             16                             17                             18                            19                             20                             21                            22                             23                            24                             25                             26                            27                             28                            29                             30                             31                             32                            33                             34                            35                             36                            37                             38                             39                            40                             41                            42                             43                             44                             45                            46                             47                             48                            49                             50                             51                             52                            53                            54                             55                             56                            57                             58                             59                            60                             61                             62             
    data_3 = data_1[data_2]

    # 因母體excel row 的設定是gps定位點，再將每天日期data重複加於後面，ex: 1  大興西路      2021-08-18  
    #                                                                  2  大興西路二段  2021-08-18
    # 故將母體資料用 順序欄位最大值做切割(切一筆列數)，總天數為切割次數，即可順利取得每日資料。
    max_n = data_3["順序"].max()

    d_8_16 = data_3[0:max_n]
    d_8_12 = data_3[max_n:max_n*2]
    d_8_9 = data_3[max_n*2:max_n*3]
    d_8_5 = data_3[max_n*3:max_n*4]
    d_8_2 = data_3[max_n*4:max_n*5]
    d_7_29 = data_3[max_n*5:max_n*6]
    d_7_26 = data_3[max_n*6:max_n*7]
    d_7_22 = data_3[max_n*7:max_n*8]
    d_7_19 = data_3[max_n*8:max_n*9]
    d_7_15 = data_3[max_n*9:max_n*10]
    d_7_12 = data_3[max_n*10:max_n*11]
    d_7_8 = data_3[max_n*11:max_n*12]
    d_7_5 = data_3[max_n*12:max_n*13]
    d_7_1 = data_3[max_n*13:max_n*14]
    d_6_28 = data_3[max_n*14:max_n*15]
    d_6_24 = data_3[max_n*15:max_n*16]
    d_6_21 = data_3[max_n*16:max_n*17]
    d_6_17 = data_3[max_n*17:max_n*18]
    d_6_14 = data_3[max_n*18:max_n*19]
    d_6_10 = data_3[max_n*19:max_n*20]
    d_6_7 = data_3[max_n*20:max_n*21]
    d_6_3 = data_3[max_n*21:max_n*22]
    d_5_31 = data_3[max_n*22:max_n*23]
    d_5_27 = data_3[max_n*23:max_n*24]
    d_5_24 = data_3[max_n*24:max_n*25]
    d_5_20 = data_3[max_n*25:max_n*26]
    d_5_17 = data_3[max_n*26:max_n*27]
    d_5_13 = data_3[max_n*27:max_n*28]
    d_5_10 = data_3[max_n*28:max_n*29]
    d_5_6 = data_3[max_n*29:max_n*30]
    d_5_3 = data_3[max_n*30:max_n*31]
    d_4_29 = data_3[max_n*31:max_n*32]
    d_4_26 = data_3[max_n*32:max_n*33]
    d_4_22 = data_3[max_n*33:max_n*34]
    d_4_19 = data_3[max_n*34:max_n*35]
    d_4_15 = data_3[max_n*35:max_n*36]
    d_4_12 = data_3[max_n*36:max_n*37]
    d_4_8 = data_3[max_n*37:max_n*38]
    d_4_5 = data_3[max_n*38:max_n*39]
    d_4_1 = data_3[max_n*39:max_n*40]
    d_3_29 = data_3[max_n*40:max_n*41]
    d_3_25 = data_3[max_n*41:max_n*42]
    d_3_22 = data_3[max_n*42:max_n*43]
    d_3_18 = data_3[max_n*43:max_n*44]
    d_3_15 = data_3[max_n*44:max_n*45]
    d_3_11 = data_3[max_n*45:max_n*46]
    d_3_8 = data_3[max_n*46:max_n*47]
    d_3_4 = data_3[max_n*47:max_n*48]
    d_3_1 = data_3[max_n*48:max_n*49]
    d_2_25 = data_3[max_n*49:max_n*50]
    d_2_22 = data_3[max_n*50:max_n*51]
    d_2_18 = data_3[max_n*51:max_n*52]
    d_2_4 = data_3[max_n*52:max_n*53]
    d_2_1 = data_3[max_n*53:max_n*54]
    d_1_28 = data_3[max_n*54:max_n*55]
    d_1_25 = data_3[max_n*55:max_n*56]
    d_1_21 = data_3[max_n*56:max_n*57]
    d_1_18 = data_3[max_n*57:max_n*58]
    d_1_14 = data_3[max_n*58:max_n*59]
    d_1_11 = data_3[max_n*59:max_n*60]
    d_1_7 = data_3[max_n*60:max_n*61]
    d_1_4 = data_3[max_n*61:max_n*62]

    # 再將切割出來的每日資料，將"垃圾車到達時間"欄位資料抽出，新增至整理後的DataFrame
    data = d_8_16.rename(columns={"垃圾車到達時間":"8/16"})
    data["8/12"] = d_8_12["垃圾車到達時間"]
    data["8/9"] = d_8_9["垃圾車到達時間"]
    data["8/5"] = d_8_5["垃圾車到達時間"]
    data["8/2"] = d_8_2["垃圾車到達時間"] 
    data["7/29"] = d_7_29["垃圾車到達時間"] 
    data["7/26"] = d_7_26["垃圾車到達時間"] 
    data["7/22"] = d_7_22["垃圾車到達時間"] 
    data["7/19"] = d_7_19["垃圾車到達時間"] 
    data["7/15"] = d_7_15["垃圾車到達時間"] 
    data["7/12"] = d_7_12["垃圾車到達時間"] 
    data["7/8"] = d_7_8["垃圾車到達時間"] 
    data["7/5"] = d_7_5["垃圾車到達時間"]
    data["7/1"] = d_7_1["垃圾車到達時間"] 
    data["6/28"] = d_6_28["垃圾車到達時間"] 
    data["6/24"] = d_6_24["垃圾車到達時間"] 
    data["6/21"] = d_6_21["垃圾車到達時間"] 
    data["6/17"] = d_6_17["垃圾車到達時間"] 
    data["6/14"] = d_6_14["垃圾車到達時間"] 
    data["6/10"] = d_6_10["垃圾車到達時間"] 
    data["6/7"] = d_6_7["垃圾車到達時間"] 
    data["6/3"] = d_6_3["垃圾車到達時間"] 
    data["5/31"] = d_5_31["垃圾車到達時間"] 
    data["5/27"] = d_5_27["垃圾車到達時間"] 
    data["5/24"] = d_5_24["垃圾車到達時間"] 
    data["5/20"] = d_5_20["垃圾車到達時間"] 
    data["5/17"] = d_5_17["垃圾車到達時間"]
    data["5/13"] = d_5_13["垃圾車到達時間"] 
    data["5/10"] = d_5_10["垃圾車到達時間"] 
    data["5/6"] = d_5_6["垃圾車到達時間"] 
    data["5/3"] = d_5_3["垃圾車到達時間"] 
    data["4/29"] = d_4_29["垃圾車到達時間"] 
    data["4/26"] = d_4_26["垃圾車到達時間"] 
    data["4/22"] = d_4_22["垃圾車到達時間"] 
    data["4/19"] = d_4_19["垃圾車到達時間"] 
    data["4/15"] = d_4_15["垃圾車到達時間"] 
    data["4/12"] = d_4_12["垃圾車到達時間"] 
    data["4/8"] = d_4_8["垃圾車到達時間"] 
    data["4/5"] = d_4_5["垃圾車到達時間"] 
    data["4/1"] = d_4_1["垃圾車到達時間"] 
    data["3/29"] = d_3_29["垃圾車到達時間"] 
    data["3/25"] = d_3_25["垃圾車到達時間"]
    data["3/22"] = d_3_22["垃圾車到達時間"] 
    data["3/18"] = d_3_18["垃圾車到達時間"] 
    data["3/15"] = d_3_15["垃圾車到達時間"] 
    data["3/11"] = d_3_11["垃圾車到達時間"] 
    data["3/8"] = d_3_8["垃圾車到達時間"] 
    data["3/4"] = d_3_4["垃圾車到達時間"] 
    data["3/1"] = d_3_1["垃圾車到達時間"] 
    data["2/25"] = d_2_25["垃圾車到達時間"] 
    data["2/22"] = d_2_22["垃圾車到達時間"] 
    data["2/18"] = d_2_18["垃圾車到達時間"]
    data["2/4"] = d_2_4["垃圾車到達時間"] 
    data["2/1"] = d_2_1["垃圾車到達時間"] 
    data["1/28"] = d_1_28["垃圾車到達時間"] 
    data["1/25"] = d_1_25["垃圾車到達時間"] 
    data["1/21"] = d_1_21["垃圾車到達時間"] 
    data["1/18"] = d_1_18["垃圾車到達時間"] 
    data["1/14"] = d_1_14["垃圾車到達時間"] 
    data["1/11"] = d_1_11["垃圾車到達時間"] 
    data["1/7"] = d_1_7["垃圾車到達時間"] 
    data["1/4"] = d_1_4["垃圾車到達時間"] 

    # 將日期欄位刪除
    data = data.drop(labels = ["日期"], axis=1)

    return data


# 再將整理過後的DataFrame，再行新增[平均到定位點時間](mean)、[每日到定點，時間誤差](std)、[到定位點須行駛時間](diff)
def mainvalue(data):
    mean_li = []
    std_li = []
    for i in range(1,(len(data.index)+1)):
        gps = data.loc[i,["8/16","8/12","8/9","8/5","8/2","7/29","7/26","7/22","7/19","7/15","7/12","7/8","7/5","7/1","6/28","6/24","6/21","6/17","6/14","6/10","6/7","6/3","5/31","5/27","5/24","5/20","5/17","5/13","5/10","5/6","5/3","4/29","4/26","4/22","4/19","4/15","4/12","4/8","4/5","4/1","3/29","3/25","3/22","3/18","3/15","3/11","3/8","3/4","3/1","2/25","2/22","2/18","2/4","2/1","1/28","1/25","1/21","1/18","1/14","1/11","1/7","1/4"]]
        rute = pd.to_datetime(gps)
        rute_f = rute-rute.dt.normalize()
        rute_mean = rute_f.mean()
        rute_std = rute_f.std()
        mean_li.append(rute_mean)
        std_li.append(rute_std)         

    mean_pd = pd.Series(mean_li)
    mean_diff = mean_pd.diff()
    data["mean"] = mean_li
    data["std"] = std_li
    data["time Consume"] = mean_diff

    print(data)

cq_1 = rawdata()
cq_2 = rute(cq_1,"中路區第四區")
cq_3 = mainvalue(cq_2)
