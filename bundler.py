import base64
import sys

def pack(s):
   encoded = base64.b64encode(s)
   s = ""
   for a in encoded:
      v = ((ord(a) << 4) & 0xF0) + ((ord(a) & 0xF0) >> 4)
      s = s + "\\x%02x" % v
   return s

if len(sys.argv) < 2:
   print "usage: %s [module_1] [module_2] ... [module_n] app" % (sys.argv[0])
   sys.exit(1)

cnt = 0
for fname in sys.argv[1:]:
   cnt += 1
   f = open(fname)
   print "ff%d=\"%s\"" % (cnt, pack(fname))
   sys.stdout.write("f%d=\"" % (cnt))
   sys.stdout.write(pack(f.read()))
   sys.stdout.write("\"")
   print

print ""
print "import sys"
print "import base64"
print "import types"

print "def dd(s):"
print " v = \"\""
print " for b in s: v = v + \"%c\" % (((ord(b) << 4) & 0xF0) + (((ord(b) & 0xF0) >> 4)))"
print " return base64.b64decode(v)"

for a in range(1, cnt):
   print "md = dd(ff%d)[:-3]" % (a)
   print "mod%d = types.ModuleType(md)" % (a)
   print "sys.modules[md] = mod%d" % (a)
   print "exec(dd(f%d), mod%d.__dict__)" % (a,a)

print "eval(compile(dd(f%d), '<string>', 'exec'))" % (cnt)
