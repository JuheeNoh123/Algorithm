def solution(wallpaper):
    answer = []
    folders=[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j]=='#':
                folders.append((i,j))
    #print(folders)
    folders.sort()
    lux = folders[0][0]
    rdx=folders[-1][0]+1
    folders.sort(key=lambda x: x[1])
    #print(folders)
    luy = folders[0][1]
    rdy=folders[-1][1]+1
    answer=[lux,luy,rdx,rdy]
    return answer