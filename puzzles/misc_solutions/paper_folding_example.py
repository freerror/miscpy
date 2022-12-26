raw = """\
onssoe rnynmw   
i c i f eodnsres
lis  .eann ,a ke
 sfwienw irt uae
I rhaAp w  eoet 
 lomr. ahsyta  t
xb shifrmocwpsle
foo ekognsi eui 
ps,eh erisltslss
fswt, so  h oai 
elaI pu cop. hsh
ckne oeihnwhldah
j  m syoytehylhn
f aon m diIelmee
etahtt ncre ieht
gfreti nimt eeos\
""".split("\n")

plans = [[list(raw[i]) for i in range(len(raw))]]

# n = int(input())
# plans = [[list(input()) for i in range(n)]]

while (k := len(plans[0][0]) // 2) > 0:
    # rotate
    plans = [list(zip(*plan))[::-1] for plan in plans]
    # fold
    plans = [plan[k:] for plan in plans] + [plan[:k][::-1] for plan in plans[::-1]]

message = "".join([plan[0][0] for plan in plans[::-1]])
print(message)
