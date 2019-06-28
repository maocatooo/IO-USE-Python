# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib import font_manager
plt.rcParams[u'font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False
my_font = font_manager.FontProperties(fname="/home/inhoo/gitdir/IO-USE-Python/Matplotlib-demo/STKAITI.TTF")

data = {'阿萨德': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
names = list(data.keys())
values = list(data.values())
# fig, axs = plt.subplots()
# bar = axs.bar(names, values)
# bar = axs.plot(names, values, kind = 'bar', )
# print bar
# bar.font.set_fontproperties(my_font)

name_list = [u"阿萨德","Tuesday","Friday","Sunday"]
num_list = [1.5,0.6,7.8,6]
plt.barh(range(len(num_list)), num_list,tick_label = name_list)
plt.legend(prop=my_font)
plt.ylabel(u"內容描述",fontproperties=my_font)

plt.show()