# https://www.google.com/search?q=python+threading+tutorial&rlz=1C1GCEA_enIN914IN914&oq=python+thrad&aqs=chrome.2.69i57j0i10i457j0i10l6.7614j0j4&sourceid=chrome&ie=UTF-8#kpvalbx=_BF2uX5zfItKe9QPgyqKwBg10

import concurrent.futures


def myFun(msg):
    #print('Hi '+ msg)
    return "Hi " + msg

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = executor.submit(myFun,'sat')
#     results1 = executor.submit(myFun,'suvi')
#     print(results.result())
#     print(results1.result())

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [ executor.submit(myFun, 'sat'+str(i)) for i in range(10)]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())


with concurrent.futures.ThreadPoolExecutor() as executor:
    names = ['sat', 'suvi', 'Arathana']
    results = executor.map(myFun, names)
    for result in results:
        print(result)

print('list comperhension')
yl = [1, 2, 3, 4, 5, 6]
r = [y for y in yl if y % 2 == 0]
print(r)
