from collections import OrderedDict
def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0:
        return 5*len(cities)
    cache = OrderedDict()
    for city in cities:
        key = city.lower()
        if key in cache:    #cache hit
            answer+=1
            cache.move_to_end(key)
        else:       #cache miss
            answer+=5
            if len(cache)>=cacheSize:
                cache.popitem(last=False)
            cache[key]=True
            
        
    return answer