# Vector search on Linux(Unix) manual pages
vector search on man pages

Install tensorflow and search on man page using the following pattern:
```
man [command] | python3 man_vec_search.py --query "your query"
```

Example:
```
$ man rsync | python man_vec_search.py --query "remote shell connection"
....

1. Score: 0.6935: shell connection, use the --remote-option (-M) option:
--------------------
    specified) and non-user extended attributes (if --xattrs was specified).
    This is a good way to backup data without using a super-user, and to store ACLs from incompatible systems.
    The --fake-super option only affects the side where the option is used.  To affect the remote  side  of  a  remote-
--> shell connection, use the --remote-option (-M) option:
    rsync -av -M--fake-super /src/ host:/dest/
    For a local copy, this option affects both the source and the destination.  If you wish a local copy to enable this
    option just for the destination files, specify -M--fake-super.  If you wish a local copy to enable this option just

2. Score: 0.6276: after the remote-shell or daemon connection is established.
--------------------
    ...
--> after the remote-shell or daemon connection is established.
    ...

3. Score: 0.5979: USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION
--------------------
    ...
--> USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION
    It is sometimes useful to use various features of an rsync daemon (such as named modules) without  actually  allowing  any
    ...
--------------------
```
