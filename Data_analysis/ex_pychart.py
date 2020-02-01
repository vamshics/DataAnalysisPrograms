import matplotlib.pyplot as plt
slices=[50,20,15,15]
depts=['Production','Sales','HR','Finance']
Cols=['green','blue','pink','gold']
#plt.pie(slices,labels=depts,colors=Cols)
plt.pie(slices,labels=depts,colors=Cols,startangle=90,shadow=True)
plt.title("amazon.com")
plt.legend()
plt.show()
