import soundcloud

__all__ = ('Client', 'resource')


class Client(soundcloud.Client):

    def get_all(self, url, offset=0, limit=200, **kwargs):
        resources = set()
        prev_offset = None
        while offset != prev_offset:
            resources.update(self.get(url, offset=offset, limit=limit, **kwargs))
            prev_offset, offset = offset, len(resources)
        return resources

resource = soundcloud.resource
