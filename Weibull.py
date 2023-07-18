import numpy as np
from scipy.stats import weibull_min
import matplotlib.pyplot as plt
from scipy.special import gamma

flow_state = 'stable'

#三参数weibull分布
#自由流对应参数
Weibull_para = {
    'free' : {
        'shape':11.48,
        'scale':77.6,
        'location':20.7
    },
    'stable': {
        'shape':4.021,
        'scale':88,
        'location':-12.71
    },
    'unstable': {
        'shape':2.937,
        'scale':28,
        'location':-4.779
    }
}

speed_range = {
    'free':{
        'start': 20,
        'end': 2000
    },
    'stable':{
        'start':0,
        'end':150
    },
    'unstable':{
        'start':0,
        'end':150
    }
}

shape = Weibull_para[flow_state]['shape']           #形状参数
scale = Weibull_para[flow_state]['scale']            #比例参数
location = Weibull_para[flow_state]['location']         #位置参数

# 计算三参数Weibull分布的概率密度函数（PDF）
#weibull分布
def weibull_pdf(x,shape,scale,location):
    
    return weibull_min.pdf((x - location) / scale, shape) / scale

#车速分布函数
def velocity_distribution(shape,scale,location):
    start = speed_range[flow_state]['start']
    end = speed_range[flow_state]['end']
    x = np.linspace(start,end,10000)

    # 计算累积分布函数（CDF）
    cdf = np.cumsum(weibull_pdf(x,shape,scale,location))
    cdf /= cdf[-1]

    u = np.random.random(10000)
    

    # 使用逆函数将随机数转换为符合给定分布的数据
    return np.interp(u, cdf, np.linspace(start, end, len(cdf)))

samples1 = velocity_distribution(shape,scale,location)
samples2 = velocity_distribution(shape,scale*1.2,location)
#for i in range(200):
    #samples.append(velocity_distribution())

print(sum(samples1)/len(samples1))
print(sum(samples2)/len(samples2))
# 绘制生成的数据的直方图
plt.subplot(2, 1, 1)  # 创建第一个子图
plt.hist(samples1, bins=30, density=True, alpha=0.7)
plt.xlabel('x')
plt.ylabel('Probability')


plt.subplot(2, 1, 2)  # 创建第二个子图
plt.hist(samples2, bins=30, density=True, alpha=0.7)
plt.xlabel('x')
plt.ylabel('Probability')


plt.grid(True)
plt.show()

ave = 88*gamma(1+(1/4.021))-12.71
print(ave)