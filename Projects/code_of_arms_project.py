###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################



q1 = codesters.Square (100, 100, 200, 'Pink')
q2 = codesters.Square (-100, 100, 200, 'LightPink')
q3 = codesters.Square (-100, -100, 200, 'Violet')
q4 = codesters.Square (100, -100, 200, 'PeachPuff')


s1 = codesters.Sprite("cardinal", 100, 100)
s1.set_size(0.8)
s2 = codesters.Sprite("Ness", -100,-100)
s2.set_size(0.4)
s3 = codesters.Sprite("Pigeon (1)", 100, -100)
s3.set_size(0.2)
s4 = codesters.Sprite("sans", -100, 100)
s4.set_size(0.3)


message1 = codesters.Text("Calvin Cristopher Krebs Caffee", 0, 220, "LightPink")
message2 = codesters.Text("Soren is my bestie", 0, -220, "white")

stage.set_background("ssbb (1)")