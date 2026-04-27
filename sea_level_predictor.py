import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. استيراد البيانات من الملف المطلوب
    df = pd.read_csv('epa-sea-level.csv')

    # 2. إنشاء مخطط مبعثر (Scatter Plot) للبيانات الأصلية
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10, label='Original Data')

    # 3. إنشاء خط التنبؤ الأول (باستخدام كل البيانات من 1880 إلى 2050)
    # نستخدم linregress للحصول على الميل (slope) والتقاطع (intercept)
    reg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_forecast1 = pd.Series([i for i in range(1880, 2051)])
    y_forecast1 = reg1.slope * x_forecast1 + reg1.intercept
    plt.plot(x_forecast1, y_forecast1, 'r', label='Best Fit Line 1 (1880-2050)')

    # 4. إنشاء خط التنبؤ الثاني (باستخدام البيانات الحديثة فقط من عام 2000 إلى 2050)
    df_recent = df[df['Year'] >= 2000]
    reg2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_forecast2 = pd.Series([i for i in range(2000, 2051)])
    y_forecast2 = reg2.slope * x_forecast2 + reg2.intercept
    plt.plot(x_forecast2, y_forecast2, 'green', label='Best Fit Line 2 (2000-2050)')

    # 5. إضافة التسميات والعناوين (ضرورية جداً لاجتياز الاختبارات)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # 6. حفظ الرسمة كصورة وإرجاع الكائن للتحقق
    plt.savefig('sea_level_plot.png')
    return plt.gca()
