# py22bin
simple helper tool to compile python2 code to a single binary


## requirements
`py22bin` requires `bash`, `python2`, `cython` and `gcc`

## usage
`py22bin` will bundle together a main file plus a set of modules into one python script and then compile it using cython. The output is the last parameter without the `.py` extension.
```
./py22bin.sh [module_1] [module_2] .. [module_n] app.py
```
e.g.

```
./py22bin.sh my_module.py my_app.py
```
produces a `my_app` binary that has `my_app.py` bundled as well as `my_module` bundled as a built-in python module.
