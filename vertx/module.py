from osv.modules import api

_vertx_home = "/usr/vertx"

_classpath = [_vertx_home + "/conf"]
_classpath.append( "%s/lib/*" % _vertx_home )

_logging_config = [
    "-Djava.util.logging.config.file=%s/conf/logging.properties" % _vertx_home
]

default = api.run_java(
        classpath=_classpath,
        args=_logging_config + [
            "-Dvertx.home=%s" % _vertx_home,
            "-Dvertx.clusterManagerFactory=org.vertx.java.spi.cluster.impl.hazelcast.HazelcastClusterManagerFactory",
            "org.vertx.java.platform.impl.cli.Starter", "-ha"
        ])
