# Vector search on Linux(Unix) manual pages
vector search on man pages

Install tensorflow and search on man page using the following pattern:
```
man [command] | python3 man_vec_search.py --query "your query"
```

Example:
```
$ man rsync | python man_vec_search.py --query "remote shell connection"
```

```
    1. Score: 0.6935: shell connection, use the --remote-option (-M) option:
    --------------------
        specified) and non-user extended attributes (if --xattrs was specified).
        This is a good way to backup data without using a super-user, and to store ACLs from incompatible systems.
        The --fake-super option only affects the side where the option is used.  To affect the remote  side  of  a  remote-
    --> shell connection, use the --remote-option (-M) option:
        rsync -av -M--fake-super /src/ host:/dest/
        For a local copy, this option affects both the source and the destination.  If you wish a local copy to enable this
        option just for the destination files, specify -M--fake-super.  If you wish a local copy to enable this option just
```
<details>
  <summary>more</summary>

    2. Score: 0.6276: after the remote-shell or daemon connection is established.
    --------------------
        live changes happening to it and you want to make sure that root-level read or write actions of  system  files  are
        not  possible.   While you could alternatively run all of rsync as the specified user, sometimes you need the root-
        level host-access credentials to be used, so this allows rsync to drop root for the copying part of  the  operation
        --> after the remote-shell or daemon connection is established.
        The option only affects one side of the transfer unless the transfer is local, in which case it affects both sides.
        Use  the  --remote-option  to  affect  the remote side, such as -M--copy-as=joe.  For a local transfer, the lsh (or
        lsh.sh) support file provides a local-shell helper script that can be used to allow a "localhost:" or  "lh:"  host-

    3. Score: 0.5979: USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION
    --------------------
        daemon) on the targethost (%H).
        Note  also  that  if  the RSYNC_SHELL environment variable is set, that program will be used to run the RSYNC_CONNECT_PROG
        command instead of using the default shell of the system() call.
    --> USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION
        It is sometimes useful to use various features of an rsync daemon (such as named modules) without  actually  allowing  any
        new  socket  connections into a system (other than what is already required to allow remote-shell access).  Rsync supports
        connecting to a host using a remote shell and then spawning a single-use "daemon" server that expects to read  its  config
    --------------------
