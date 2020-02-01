

import matplotlib.pyplot as plt
import pandas as pd

empdata={"empid":[1001,1002,1003,1004,1005],"ename":["Ganesh","kondal","vamshi","varma","krishna"],
"doj":["10-10-2017","01-02-2016","2-1-2016","3-5-2018","06-05-2013"],"sal":[20000,8900,21000,1800.20,8900.37]}
df=pd.DataFrame(empdata)
x=df['empid']
x=df['ename']
y=df['sal']
plt.bar(x,y, label='empdata',color='red')
plt.xlabel('Employee ids')
plt.ylabel('Employee Salaries')
plt.title("MiCROSOFT")
plt.legend()
plt.show()
