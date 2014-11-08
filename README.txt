CREDITS

The tmux-cssh.py python script is based on the bash script found on this blog:

http://perlstalker.vuser.org/blog/2013/09/24/cluster-ssh-with-tmux/



INSTALLATION

1. Add the commands in tmux.conf to ~/.tmux.conf (or copy them to that file if it doesn't exist)
2. Place tmux-cssh.py on your path and be certain it is executable
3. Fix the first line of tmux-cssh.py if you use a different path to execute python


USAGE

1. Create a cluster file at "~/.clusterssh/clusters" like this:

----- EXAMPLE CLUSTERS FILE -----
cluster1 user@host1 user@host2
cluster2 user2@host3 user2@host4
----- END EXAMPLE CLUSTERS FILE -----

An existing clusterssh clusters file should work.

2. Start tmux.
3. Type C-b M-s (Where C-b is <crtl>+b and M-s is <ESC> quickly followed by 's')
4. You will be prompted to enter the cluster name.  Type the cluster name from the clusters file, then press <ENTER>.
5. A new tmux window will be created with panels for each host in the cluster.
6. Use C-b M-a to toggle sending keystrokes to all panes on the window
7. Use C-b M-S to launch tmux-cssh with logging enabled (log messages written to filename specified in ~/.tmux.conf)
