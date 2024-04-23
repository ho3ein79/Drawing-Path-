import time
s = time.time()
# khat = [(1,2),(1,5),(1,12),(4,1),(1,13),(2,6),(2,3),(2,7),(13,2),(13,4),(4,3),(3,8),(3,9),(3,13),(4,10),(4,11),(5,6),(7,8),(9,10),(11,12)]
# khat = [(1,2),(1,4),(1,5),(1,6),(2,5),(2,7),(2,3),(3,7),(3,4),(3,8),(3,9),(4,8),(4,6),(6,8),(8,9),(1,3)]
# khat = [(1,2),(1,5),(2,5),(2,3),(2,4),(3,4),(4,9),(4,5),(4,15),(4,11),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9),(9,10),(9,11),(10,11),(11,12),(11,13),(11,15),(12,13),(13,14),(13,15),(14,15)]
khat = [(1,3),(1,6),(2,3),(2,4),(3,4),(3,6),(3,5),(4,5),(4,7),(5,6),(5,8),(6,8),(7,8),(5,9),(7,9),(8,9)]
level_geremz = {
1 : [],
2 : [],
3 : [],
4 : [],
5 : [],
6 : [],
7 : [],
8 : [],
9 : [],
10 : [],
11 : [],
12 : [],
13 : [],
14 : [],
15 : [],
16 : [],
17 : [],
18 : [],
19 : [],
20 : [],
21 : [],
22 : [],
23 : [],
24 : [],
25 : [],
26 : [],
27 : [],
28 : [],
29 : [],
30 : [],
}
list_asli = []





# adad= []
# for item in khat:
#     if item[0] not in adad: adad.append(item[0])
#     if item[1] not in adad: adad.append(item[1])
# print(adad)    

# dic = {}
# while True:
#     shoro = 1
#     li = []
#     for item in khat:
#        if item[0] == shoro or item[1] == shoro: 
#         li.append(item)
#     dic[shoro] = li 
#     print(dic)
#     break  

def  rah_mojod(nogte,lis):
  tedad_rah_tarsim_az_nogte = []
  for item in lis:
    if item[0] == nogte or item[1] == nogte: 
      tedad_rah_tarsim_az_nogte.append(item)
  # print(f"nokte {nogte} = ",tedad_rah_tarsim_az_nogte)    
  return  len(tedad_rah_tarsim_az_nogte)  



def chek(item,level):

  x = (item[0], item[1]) 
  y = (item[1], item[0])
  if x  in  list_asli or y  in  list_asli or x in level_geremz[level] or y  in level_geremz[level]:
    # print('False')
    return False

  else:
    # print('True')
    return True


def chek_nokte(nogte_poya,level) :
  # print(f'nogte poya = {nogte_poya},level = {level}' )
  if rah_mojod(nogte_poya,khat) != rah_mojod(nogte_poya,list_asli) + len(level_geremz[level]):
    # print(f'True = chek nokte ba nokte {nogte_poya} va level {level}',rah_mojod(nogte_poya,khat),rah_mojod(nogte_poya,list_asli) + len(level_geremz[level]))
    # print(level_geremz)
    return True
    
  else: 
    # print(f'False = chek nokte ba nokte {nogte_poya} va level {level}',rah_mojod(nogte_poya,khat),rah_mojod(nogte_poya,list_asli) + len(level_geremz[level]))
    # print(level_geremz)
    return False  

def bargasht(level):
  level_geremz[level].clear()  
  try:
   level_geremz[level - 1].append(list_asli[-1])
   list_asli.pop(-1)
  except:
  #  print('fdgdfgdfg')
   pass

  
nogat = [1]
nn = len(nogat)
shoro = nogat[0]
nogte_poy = shoro
def halge(nogte_poya): 
 global max
 level = 1
 i = 0
 max = []
 l = 0
 while len(khat) > len(max) or len(nogat) == 0:
  i += 1 
  # if level == 2 and i != 2:
  # if chek_nokte[shoro,level] == False:  
        # print("tamam")
        # break
  if level == 0: level = 1 
  if chek_nokte(nogte_poya,level):
    # print('nokte  poya =',nogte_poya)
    for item in khat:
      if item[0] == nogte_poya or item[1] == nogte_poya: 
          if chek(item,level): 
          #  print(f"shod = {item}")  
           list_asli.append(item)
           item = item
           if level > l:
            l = level
            max.clear()
            max.extend(list_asli)
           level += 1
           if item[0] == nogte_poya:  
            nogte_poya = item[1]
           elif item[1] == nogte_poya: 
            nogte_poya = item[0]   
          #  print("n = ",nogte_poya) 
           
      else:
        # print(f"nashod = {item}")   
        pass  
  else:
      # print("hhhhhhhhhhhhhhhhhhhhhh")
      try:
        if list_asli[-1][0] == list_asli[-2][0] or list_asli[-1][0] == list_asli[-2][1] : 
          nogte_poya = list_asli[-1][0]
        else: 
          nogte_poya = list_asli[-1][1]
      except:
        nogte_poya = nogat[0]
      if level == 1 :
        nogat.pop(0)
        try:
         nogte_poya = nogat[0]
         level_geremz[1].clear()
        except:   
           break    
        # print(f'nogte poya = {nogte_poya} , {level_geremz}')
      # if len(nogat) == 0 :  
        # print("tamam")         
        # break    
      bargasht(level)  
      level -= 1
 if len(max) == len(khat):
            print("Success :)")   
            print(f"Total number of lines drawn so far: {nn} ",i)  
            print(f'Drawing Path = {max} level = {l}')
 else:
            print("Failure:|")   
            print(f"Total number of lines drawn so far: {nn} ",i)
            print(f'Drawing Path = {max} level = {l}')   
 
      

       
  # print(list_asli,level)  




halge(nogte_poy)
print(time.time() - s )

   