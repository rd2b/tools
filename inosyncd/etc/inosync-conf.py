# directory that should be watched for changes
wpath = "/tmp/inosync"

# exclude list for rsync
rexcludes = [
      "/nosync",
]

# common remote path
rpath = "/tmp/"

# remote locations in rsync syntax
rnodes = [
      "rem01:" + rpath,
      "remiperso:" + rpath,
]

# limit remote sync speed (in KB/s, 0 = no limit)
#rspeed = 0

# event mask (only sync on these events)
#emask = [
#     "IN_CLOSE_WRITE",
#     "IN_CREATE",
#     "IN_DELETE",
#     "IN_MOVED_FROM",
#     "IN_MOVED_TO",
#]

# event delay in seconds (this prevents huge
# amounts of syncs, but dicreases the
# realtime side of things)
#edelay = 10

# rsync binary path
#rsync = "/usr/bin/rsync"
