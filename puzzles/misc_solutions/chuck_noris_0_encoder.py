# TODO Full Ascii Support
# TODO get below 100 characters
n=f='';b,k=65,[]
m = input()
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
 k+=[i,f"{b:b}"]
 b+=1
for l in m:
 u=l.upper()
 x=k.index(u)
 n+=k[x+1]
 c='0'
 lz='0'
 e=''
for z in n:
 if z=='1':
  if lz=='1':
   c='0' # (['0',' 0 0'][z==lz==1])
  else:
   c=' 0 0'
 elif z=='0':
  if lz=='0':
   c='0' # (['0',' 00 0'][z==lz==0])
  else:
   c=' 00 0'
 lz=z
 e+=c
print(e[1:])
print(k)

# 26 Letters
# A     01000001
# B     01000010
# C     01000011
# D     01000100
# E     01000101
# F     01000110
# G     01000111
# H     01001000
# I     01001001
# J     01001010
# K     01001011
# L     01001100
# M     01001101
# N     01001110
# O     01001111
# P     01010000
# Q     01010001
# R     01010010
# S     01010011
# T     01010100
# U     01010101
# V     01010110
# W     01010111
# X     01011000
# Y     01011001
# Z     01011010

