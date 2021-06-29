#!/usr/bin/env python
# coding: utf-8

# In[1]:


#keyboard layout including numbers
keySet = [['1','2','3','4','5','6','7','8','9','0','-'],
          ['q','w','e','r','t','y','u','i','o','p','['],
          ['a','s','d','f','g','h','j','k','l',';'],
          ['z','x','c','v','b','n','m',',']]


# In[2]:


#replaces character based on key
#key represents how many times the same character is replaced
#EG: for first replace(key = 0), give lhs key as result. if (key = 1) give rhs as result
def replaceChar(chx, chy, key): 
    if key == 0:
        if chy == 0:
            key+= 1
        else:
            return [keySet[chx][chy-1],key+1]
    if key == 1:
        if chy == len(keySet[chx]):
            key+= 1
        else:
            return [keySet[chx][chy+1],key+1]
    if key == 2:
        if chx == 0:
            key+= 1
        else:
            return [keySet[chx-1][chy],key+1]
    if key == 3:
        if chx == 3 or len(keySet[chx+1]) >= chy:
            key+= 1
        else:
            print(chx,chy)
            return [keySet[chx+1][chy],key+1] 
    if key == 4:
        return replaceChar(chx, chy, 0)
    


# In[3]:


def findIndex2D(c):
    for i, sublist in enumerate(keySet):
        if c in sublist:
            return [i,sublist.index(c)]
    return [-1,-1]


# In[4]:


def randomNotEmpty(usedRandoms, strInput, maxLen):
    chIndex = random.randint(0, maxLen-1)
    while(chIndex in usedRandoms or strInput[chIndex] == ' '):
        chIndex = random.randint(0, maxLen-1)
    return chIndex


# In[5]:


#Generates mistakes at random positions in given word/phrase
#refWord - word to be misspelled
#misCount, number of mistakes to be included
#targetCount - total number of misspelled words to be generated
#chRecord - maintains spelling mistake already included to avoid repetitions
import random
def randomMistakes(refWord, misCount, targetCount):
    if(misCount>len(refWord)):
        misCount = len(refWord)
    targetSet = []
    chRecord = {}

    for i in range(targetCount):
        currRandom = []
        newStr = refWord
        Eflag=False
        for j in range(misCount):
            chIndex = randomNotEmpty(currRandom, newStr, len(refWord))
            currRandom.append(chIndex)
            recordKey = refWord[chIndex]
            
            [x,y] = findIndex2D(refWord[chIndex])
            if x == -1:
                Eflag == True
                break
        
            
            if recordKey not in chRecord.keys():
                chRecord[recordKey] = 0
            [newChar, chRecord[recordKey]] = replaceChar(x,y,chRecord[recordKey])
            
            newStr = newStr[:chIndex] + newChar + newStr[chIndex + 1:]
        if(Eflag == False):
            targetSet.append(newStr)
    return targetSet


# In[6]:


randomMistakes('hotel taj vivanta',4,15)


# In[ ]:





# In[428]:



    


# In[ ]:





# In[ ]:




