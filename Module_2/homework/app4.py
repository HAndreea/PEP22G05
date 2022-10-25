"""
4. Declarați o variabila cu șirul: “Ananas”. Afișati șirul în următoarele feluri pe ecran:
- A
n
a
n
a
s
- Ana
nas
- An:ana:s
- Ana_na_s
- nananananananan (-> na na na na na na na n)
-
"""
sir = "Ananas"
print(sir[0],sir[1],sir[2],sir[3],sir[4],sir[5], sep = "\n")
print(sir[0:3], sir[3:], sep = "\n")
print(sir[0:2], sir[2:4],sir[5], sep = ":")
print(sir[0:3], sir[3:5],sir[5], sep = "_")
print(sir[1:3]*7 + sir[3])