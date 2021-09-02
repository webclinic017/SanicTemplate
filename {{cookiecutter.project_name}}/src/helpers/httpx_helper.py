# cookiecutter_flag {%- if cookiecutter.enable_httpx == 'True' %}
# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
FileName: request_handler
Description: Request 异步客户端
Author: {{cookiecutter.maintainer}}
Email: {{cookiecutter.email}}
CreateTime: {% now 'local' %}
"""
import asyncio

from helpers.abstract_helper import AbstractHttpxClient


class HttpxClient(AbstractHttpxClient):

    def __init__(self):
        super().__init__(timeout=10, retry=5, status_retry=True)
        self.session.headers.update({"User-Agent": "Sanic HttpClient Test"})

    async def example_func(self):
        resp = await self.post("https://httpbin.org/post", json={"foo": "bar"})
        return resp.json()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = loop.run_until_complete(HttpxClient())
    res = loop.run_until_complete(client.example_func())
    loop.run_until_complete(client.close())
    print(res)
# cookiecutter_flag {%- endif %}
