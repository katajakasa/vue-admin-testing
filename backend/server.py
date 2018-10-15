from aiohttp import web
import math


def build_qs(args: dict):
    out = "&".join(["{}={}".format(k, v) for k, v in args.items() if v])
    return "?" + out if out else ""


def table_response(items: list,
                   total: int,
                   page: int = 1,
                   per_page: int = 15,
                   order_by: str = None,
                   filter_by: str = None):
    last_page = math.ceil(total / per_page)
    next_page_qs = build_qs({'page': page + 1, 'sort': order_by, 'filter': filter_by})
    prev_page_qs = build_qs({'page': page - 1, 'sort': order_by, 'filter': filter_by})
    return web.json_response({
        'data': items,
        'current_page': page,
        'total': total,
        'per_page': per_page,
        'last_page': last_page,
        'from': page * per_page,
        'to': (page + 1) * per_page,
        'next_page_url': '/{}'.format(next_page_qs) if page < last_page else None,
        'prev_page_url': '/{}'.format(prev_page_qs) if page > 1 else None
    })


def get_paging_qs(request):
    page = int(request.rel_url.query.get('page', 1))
    per_page = int(request.rel_url.query.get('per_page', 15))
    order_by = str(request.rel_url.query.get('sort', ''))
    filter_by = str(request.rel_url.query.get('filter', ''))
    return page, per_page, order_by, filter_by


async def handler_root(request):
    page, per_page, order_by, filter_by = get_paging_qs(request)
    start = (page-1) * per_page
    end = start + per_page
    r = table_response(request.app['items'][start:end], 200, page, per_page, order_by, filter_by)
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r


async def make_app():
    app = web.Application()
    app['items'] = []
    for m in range(200):
        app['items'].append({
            'id': m,
            'kek': 'Item {}'.format(m+1)
        })
    app.add_routes([
        web.get('/', handler_root)
    ])
    return app


if __name__ == '__main__':
    web.run_app(make_app(), port=9000)
