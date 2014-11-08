#!/usr/bin/python
import logging
import optparse
import os


def read_clusters_from_cssh_clusters_files():
    filename = os.path.expanduser(os.path.join("~",".clusterssh","clusters"))
    clusters = {}
    with open(filename, "r") as f:
        lines = [line.rstrip() for line in f]
    for line in lines:
        items = line.split()
        if len(items) > 1:
            clusters[items[0]] = items[1:]
    return clusters


def get_connections(cluster):
    clusters = read_clusters_from_cssh_clusters_files()

    if not clusters.has_key(cluster):
        raise Exception("Undefined cluster")

    return clusters[cluster]


def tssh(cluster):
    connections = get_connections(cluster)
    first_connection = True
    for connection in connections:
        ssh_command = "ssh %s" % connection
        if first_connection:
            logging.debug("Creating new window for: %s" % ssh_command)
            os.system('tmux new-window -n %s "%s"' % (cluster, ssh_command))
            first_connection = False
        else:
            logging.debug("Creating new pane for: %s" % ssh_command)
            os.system('tmux splitw "%s"' % ssh_command)
            os.system('tmux select-layout tiled')
    logging.debug("Turning on synchronize-panes...")
    os.system('tmux set-window-option synchronize-panes on')


def main():
    parser = optparse.OptionParser(usage="usage: %prog [options] cluster_name", version="%prog ALPHA")
    parser.add_option("-l", "--logfile", dest="logfile", default="/dev/null")
    (options, args) = parser.parse_args()

    logging.basicConfig(filename=options.logfile, level=logging.DEBUG)

    if len(args) != 1:
        parser.error("Missing cluster_name.")

    cluster = args[0]
    logging.debug("Start tssh to cluster_name: %s" % cluster)
    tssh(cluster)


if __name__=="__main__":
    main()

