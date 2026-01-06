# Vector search on Linux(Unix) manual pages
vector search on man pages

Install tensorflow and run:
```
 man rsync | python man_vec_search.py --query "recursive"
```

sample output:
```
1. Score: 1.0000: --recursive).
--------------------
    help to make the transfer possible.  However, it does introduce a delay before the start of the transfer, and  this
    delay  might cause the transfer to timeout (if --timeout was specified).  It also forces rsync to use the old, non-
    incremental recursion algorithm that requires rsync to scan all the files in the transfer into memory at once  (see
--> --recursive).
    --delete-during, --del
    Request  that  the file-deletions on the receiving side be done incrementally as the transfer happens.  The per-di‐
    rectory delete scan is done right before each directory is checked for updates, so it behaves like a more efficient

2. Score: 0.9171: recursive option.
--------------------
    the transfer (i.e. which files are hard-linked together), just its efficiency (i.e. copying the  data  for  a  new,
    early  copy  of  a hard-linked file that could have been found later in the transfer in another member of the hard-
    linked set of files).  One way to avoid this inefficiency is to disable incremental recursion using  the  --no-inc-
--> recursive option ...

```
