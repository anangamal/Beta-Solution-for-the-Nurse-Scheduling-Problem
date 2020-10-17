from tkinter import *
from random import *
from re import *
def generation(stn, GENES, pops):
    population=[]; popi=[]
    for j in range(0, pops, 1):
        popi=[]
        for i in range(0, stn, 1):
            posi=randint(0, stn-1)
            popi.insert(i, GENES[posi])
        population.insert(j, popi) 
    return population
def selection(stn, population, pops):
    parents=[]; parent=[]
    for i in range(0, pops, 1):
        parent=[]
        for j in range(0, stn, 1):
            posi=randint(0, stn-1)
            parent.insert(j, population[posi])
        parents.insert(i, parent) 
    return parents
def crossover(parents):
       children=[]; parent1=[]; parent2=[]; child1=[]; child2=[]
       for i in range(1, len(parents), 2):
              parent1=parents[i-1]; parent2=parents[i]
              for j in range (0, (len(parents)//2), 1):
                     child1.insert(j, parent1[j])
                     child2.insert(j, parent2[j])
              for j in range ((len(parents)//2), len(parent1), 1):
                     child1.insert(j, parent2[j])
                     child2.insert(j, parent1[j])
              children.insert(i, child1)
              children.insert((i+1), child2)
       return children
def mutation(children, GENES):
    for i in range(0, len(children), 1):
        posi1=randint(0, len(GENES)-1)
        posi2=randint(0, len(GENES)-1)
        children[i].insert(posi1, GENES[posi2])
    return children
def fitness(child, ds, ns, lns, nps):
    fiti=0
    for i in range(0, ds, 1):
        if nps[child[i]-1]=='day':
            fiti=fiti+1
    for i in range(ds, ns, 1):
        if nps[child[i]-1]=='night':
            fiti=fiti+1
    for i in range(ns, lns, 1):
        if nps[child[i]-1]=='late night':
            fiti=fiti+1
    return fiti
def msg():
    root.destroy()
root=Tk(); top=Frame(root)
sta=StringVar(); ho=StringVar(); pop=StringVar()
nur=StringVar(); soc=StringVar(); top.pack()
Label(top, text="Greetings!").pack(side=TOP)
Label(top, text="Please, enter the hospital's staff number: ").pack(side=TOP)
SN=Entry(top, textvariable=sta); SN.pack(side=TOP)
Label(top, text="Please, enter the population size: ").pack(side=TOP)
PS=Entry(top, textvariable=pop); PS.pack(side=TOP)
Label(top, text="Please, enter the hospital's preferences: ").pack(side=TOP)
HP=Entry(top, textvariable=ho); HP.pack(side=TOP)
Label(top, text="Please, enter the nurses' preferences: ").pack(side=TOP)
NP=Entry(top, textvariable=nur); NP.pack(side=TOP)
Label(top, text="Please, enter the stopping condition, if none exists, enter 0: ").pack(side=TOP)
SC=Entry(top, textvariable=soc); SC.pack(side=TOP)
done=Button(top, text='Press when done', command=msg); done.pack(side=BOTTOM)
top.mainloop()
stn=int(sta.get()); hp=str(ho.get()); pops=int(pop.get()); np=str(nur.get());
sc=str(soc.get()); GENES=list(range(1, stn+1, 1)); nps=[]; beg=[]; end=[]
shi=[int(x.group()) for x in re.finditer(r'\d+', hp)]; nnp=list(np)
ds=shi[0]; ns=shi[1]; lns=shi[2]; j=0; k=0
for i in range(0, len(nnp), 1):
    if nnp[i]==':':
        beg.insert(j, i)
        j=j+1
    elif nnp[i]==',':
        end.insert(k, i)
        k=k+1
    else:
        continue
j=0; left=0; right=0; mat='0'
for it in range(0, len(beg) if len(beg)>len(end) else len(end), 1):
    left=beg[j]; right=end[j]; mat=nnp[left:right]
    nps.insert(it, mat)
    j=j+1
nps.remove(" "); nps=str(nps)
if sc=='0':
    length=0
    while length!=sum(ds, ns, lns):
        for i in range(1, len(children), 2):
            fit1=(children[i-1], ds, ns, lns, nps)
            fit2=(children[i], ds, ns, lns, nps)
            if fit1>=fit2:
                length=len(children[i-1])
                children.pop(children[i])
            else:
                length=len(children[i])
                children.pop(children[i-1])
else:
    con=[int(y.group()) for y in re.finditer(r'\d+', sc)]
    if len(con)==1:
        gen=con[0]
        while gen:
            for i in range(1, len(children), 2):
                fit1=(children[i-1], ds, ns, lns, nps)
                fit2=(children[i], ds, ns, lns, nps)
            if fit1<=fit2:
                children.pop(children[i-1])
            else:
                children.pop(children[i])
    else:
        pick=children[0]
        while pick!=sc:
            for i in range(1, len(children), 2):
                if children[i]==sc:
                    pick=children[i]
                    break
                else:
                    continue
for i in range(0, len(children), 1):
            print(children[i])
