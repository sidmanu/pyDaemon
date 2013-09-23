#!/usr/bin/env python

import sys, time
from daemon import Daemon


class MyDaemon(Daemon):
	def run(self):
		while True:
			time.sleep(1)

if __name__ == "__main__":
	daemon = MyDaemon("/tmp/daemon-pidfile.pid")
	if (len(sys.argv) == 2):
		if sys.argv[1] == 'start':
			daemon.start()

		elif sys.argv[1] == 'stop':
			daemon.stop()

		elif sys.argv[1] == 'restart':
			daemon.restart()

		else:
			print "Unknown command!"
			sys.exit(2)
		
		sys.exit(0)	

	else:
		print "Usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)


