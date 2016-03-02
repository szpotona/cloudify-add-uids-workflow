from cloudify.decorators import workflow
from cloudify.workflows import ctx


@workflow
def run(**kwargs):
    for node in ctx.nodes:
        ctr = 1
        ctx.logger.info('Show node properties')
        ctx.logger.info(str(node.properties))
        type = node.properties.get('type', 'notinstance')
        for instance in node.instances:
            ctx.logger.info('Show instance')
            ctx.logger.info(str(instance._node_instance['runtime_properties']))
            instance._node_instance['runtime_properties']['id'] = type + \
                                                                  str(ctr)
            ctx.logger.info(str(instance._node_instance['runtime_properties']))
            ctr += 1
