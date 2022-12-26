m=''.join(('{0:07b}'.format(ord(c),'b')for c in input()))
o=''.join((' 0 'if x[0]=='1'else' 00 ')+'0'*sum(1 for c in x)for x in''.join(m[i]if m[i-1]==m[i]else';'+m[i]for i in range(len(m))).split(';')if x)
print(o[1:])